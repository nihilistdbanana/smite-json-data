import json
import glob

files = glob.glob('../_gods/*.json')  # array listing paths to all json files in _gods

FIELDS = [
    'name',
    'release date',
    'pantheon',
    'role',
    'type',
    'basic attack type',
    'seasons',
]

RESULT = {}

for file in files:
    with open(file, 'r') as f:
        data = json.loads(f.read())
        key_fields = [key for key in data]

        #  if any value in FIELDS is not in the data or it's value is empty
        #  then add it to the missing_fields array
        missing_fields = [x for x in FIELDS if x not in key_fields or not data[x]]

        RESULT[file] = missing_fields


with open('result.json', 'w') as result_file:
    json.dump(RESULT, result_file)
