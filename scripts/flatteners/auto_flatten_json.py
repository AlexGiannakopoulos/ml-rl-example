import json 
import pandas as pd

def flatten_json(data, parent_key='', separator='_'):

    # Recursively flatten a nested Json directory

    # Parameter (inputs to the function)
    # data(dict): the nested Json object to flatten
    # parent_key(str): the prefix for nested keys
    # separator(Str): the symbol used to join parent and child keys

    # Return a flattened dictionary

    items = {} # Store the flattened key-value pairs

    # Loop through each key-value pair in the Json object
    for key, value in data.items():
        # build the new key name 
        # example: attributes + "_" + "BikeParking" --> attributes_BikeParking
        new_key = parent_key + separator + key if parent_key else key

        # if the value is a dictionary, recursively flatten it
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, separator))

        # if the value is a list, convert it to a string
        elif isinstance(value, list):
            items[new_key] = str(value)

        # otherwise, if it is a normal value, fetch the value and store it
        else:
            items[new_key] = value
    return items


def auto_flatten_file(input_file, output_file):
    # Read a json file, flatten each json record, save the result in a csv

    rows =[]

    # Read the input JSON file
    with open(input_file, 'r', encoding="utf-8") as f:       
        
        #process line by line
        for line in f:

            # convert json into a dict
            data = json.loads(line)

            # flatten the dict
            flat_record = flatten_json(data)
            
            # add the list of rows
            rows.append(flat_record)


    # Convert the flattened data to a DataFrame and save it as a CSV file
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)

    