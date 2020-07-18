# -*- coding: utf-8 -*-

import re
from pprint import pprint


def get_message(content):
	"""
	This function returns statistics from chat export in whatsapp
	
	Return:
	(time_stamp, date), name  / phone number, message 
	"""

	while content != "":
		# matched = re.search(groups_regex, content)
		try:
			if content[0] != "[":
				raise Exception("Skipping line")
			end_name = content.find(": ")
			if end_name == -1:
				raise Exception("Bad line")
				
			name = content[content.find("] ") + 2: end_name].strip()
			date, time = content[1: content.find(",")],\
						 content[content.find(",") + 2:content.find("]")]
						 
			yield (date, time), name
		except Exception as e:
			# print(e)
			pass
		finally:
			next_line = content.find("\n")
			if next_line == -1:
				break
			# Go to next line
			content = content[next_line + 1:]
			#print(name, date, time)
			


def main():
	stats = {}
	get_file_content = lambda filename: open(filename, "r", encoding="utf8")\
										.read()
	# Get chat_export.txt from whatsapp export chat option
	content = get_file_content("chat_export.txt")

	count = 0
	# Get number of lines for progress printing purposes
	length_all = len(content.split("\n"))
	for (date, time), name in get_message(content):
		if count % 500 == 0:
			print(f"Finished {(count / length_all) * 100:.2f}% / 100%")
		
		if date not in stats:
			stats[date] = {}
		
		if name not in stats[date]:
			stats[date][name] = 0 
			
		stats[date][name] += 1
		count += 1

	with open("stats_with_dates.txt", "w", encoding="utf8") as f:
		f.write(str(stats))

if __name__ == "__main__":
	main()
