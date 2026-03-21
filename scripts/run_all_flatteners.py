import os # this library is python's standard library
          # work with files, navigate through folders and file,
          # create or remove dictionaries 
          # manipulate paths
          # read environment variables

from flatteners.auto_flatten_json import auto_flatten_file

# list all files in the data folder

files = os.listdir("data")

print(files)

# loop through all files

for file in files: 

    # only process json files
    if file.endswith(".json"):
        
        # build input path
        input_path = os.path.join("data", file)

        # create output csv
        output_name = file.replace(".json", "_flat.csv")

        # build output path
        output_path = os.path.join("output", output_name)

        # run auto flattener
        auto_flatten_file(input_path, output_path)