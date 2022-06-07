import csv
import json

def make_json(csvFilePath, jsonFilePath):
	data = []
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		[data.append(rows) for rows in csvReader]

	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))

csvFilePath = "./data/survey.csv"
jsonFilePath = "./data/survey.json"

make_json(csvFilePath, jsonFilePath)
 
