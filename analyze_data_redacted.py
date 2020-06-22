import matplotlib.pyplot as plt
from pprint import pprint 
import datetime as dt
import matplotlib.dates as mdates

def main():
	# Acquire stats_with_dates.txt file from whatsapp_stats_redacted.py
	data = open("stats_with_dates.txt", "r", encoding="utf8").read()
	
	# 							*** WARNING  ***
	#
	# Don't run this in a production environment (if you're somehow considering it,
	# eval is a super dangerous function. this is only for personal purposes)
	#
	#							*** WARNING  ***
	data = eval(data)
	
	dates = data.keys()
	
	values = []
	for date in dates:
		values.append(len(values))
	
	fig, axs = plt.subplots(2)
	
	
	for index, ax in enumerate(axs.flat):
		# Set format value for x axis
		ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
		# Set interval for days in x axis
		ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))

		ylabel = "Number of messages" if index == 0 else "Number of messages (per day)"
		
		ax.set(xlabel="Date", ylabel=ylabel)

	
	# Dict to acquire number of messages according to date and phone number / name
	value_dict = {}
	
	count = 0
	for date in dates:
		name_times = data[date]
		for name, times in name_times.items():
			if name not in value_dict:
				value_dict[name] = []
				for i in range(len(dates)):
					value_dict[name].append(0)
			
			value_dict[name][count] = times
		count += 1
	
	FILTER_THRESHOLD = 3000 
	
	# Filter all people who have less than (or equal to) 3000 messages
	filtered_value_dict = dict(filter(lambda elem: sum(elem[1]) > FILTER_THRESHOLD, value_dict.items()))

	# Get sum until specific element in list
	generate_sum_until_elements = lambda tup: sum(tup[0][:tup[1]])
	
	# Dict with sum values instead of values per day
	sum_value_dict = {k: list(map(generate_sum_until_elements, [(v, index) for index, _ in enumerate(v) ])) for k, v in filtered_value_dict.items()}
	
	dates = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]
	
	for value1, value2 in zip(sum_value_dict.values(), filtered_value_dict.values()):
		axs[0].plot(dates, value1)
		axs[1].plot(dates, value2)
	
	# Create legend for phone numbers and lines
	fig.legend(sum_value_dict.keys())
		
	# Format date values properly
	fig.autofmt_xdate()
	fig.autofmt_xdate()
	
	fig.suptitle("Graph for message statistics")
	
	# Set graph to center 
	axs[0].margins(0)
	axs[1].margins(0)

	plt.show()
	
if __name__ == "__main__":
	main()