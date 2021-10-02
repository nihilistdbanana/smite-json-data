import json
import glob


files = glob.glob('../_gods/*.json')  # array listing paths to all json files in _gods

# array of fields currently expected inside root of json
root_fields = ['name',
               'release date',
               'pantheon',
               'role',
               'type',
               'basic attack type',
               'seasons']



def check_missing_root_data(result_file="root_data_test_result.json"):
    '''
        This function will check all the root properties of the all JSON files inside _gods.
        For fields missing, it will append an entry per file to the res object in the following format:

        "filename.json" : ["property1","property2","property3"]
    '''

    result = {}

    for file_name in files:
        check_missing_root_data_for_file(file_name, result)

    with open('result.json', 'w') as result_file:
        json.dump(result, result_file)


def check_missing_root_data_for_file(input_file = None, res = {}):
    '''
        This function will check all the root properties of the JSON file provided.
        If there is any field missing, it will append an entry it to the res object in the following format

        "filename.json" : ["property1","property2","property3"]
    '''

    # variable to generate the json result in.
    with open(input_file, 'r') as file_to_read:

        data = json.loads(file_to_read.read())
        key_fields = [key for key in data]

        #  if any value in FIELDS is not in the data or it's value is empty
        #  then add it to the missing_fields array

        missing_fields = [x for x in FIELDS if x not in key_fields or not data[x]]

        res[input_file] = missing_fields



def main():
    check_missing_root_data()


if __name__ == "__main__":
    # execute only if run as a script
    main()
