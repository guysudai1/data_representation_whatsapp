# Whatsapp data grapher 
The graphs generated by this script display whatsapp group data (messages sent by users with over 3000 messages and number of messages per day)

# Installation
In order to use this script you have 2 options: 
1. Install `matplotlib` directory with 
```
pip install matplotlib 
```
2. Use the `Pipfile` and `Pipfile.lock`:
2.1 (Skip if you have pipenv) Install pipenv with
```
pip install pipenv
```
2.2 execute (In the Pipfile directory)
```
python -m pipenv install
```

# Usage
1. Generate a whatsapp group's export into a txt file (without media)
2. Rename the export file to `chat_export.txt` (or modify the script to customize your own file name) and insert it into the script directory
3. Run `whatsapp_stats_redacted.py`
4. Run `analyze_data_redacted.py`

Hope you have fun with the scripts :)
