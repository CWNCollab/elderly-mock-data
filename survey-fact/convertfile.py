import csv
import json

def make_json(csvFilePath, jsonFilePath):
	data = {}
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for rows in csvReader:
			# Assuming a column named 'surveyFactId' to be the primary key
			key = rows['surveyFactId']
			data[key] = rows
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
csvFilePath = r'./data/survey.csv'
jsonFilePath = r'./data/survey.json'

make_json(csvFilePath, jsonFilePath)
         