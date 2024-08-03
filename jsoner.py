import json

# Read the JSON data from the file
with open('movies.json', 'r') as file:
    data = json.load(file)

# Format the JSON data
formatted_data = json.dumps(data, indent=4)

# Write the formatted data back to the file
with open('movies.json', 'w') as file:
    file.write(formatted_data)
