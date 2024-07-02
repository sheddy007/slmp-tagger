import os
from dotenv import load_dotenv
import pandas as pd
import json
import re


dotenv_path = 'inputs.env'

if not os.path.exists(dotenv_path):
    print(f"Error: {dotenv_path} file not found.")
    exit(1)

load_dotenv(dotenv_path)


def format_address(address):
    return re.sub(r"([A-Za-z])(\d)", r"\1 \2", address)


excel_file = os.getenv('EXCEL_FILE')
sheet_name = os.getenv('SHEET_NAME')
ip_address = os.getenv('IP_ADDRESS')
port_number_str = os.getenv('PORT_NUMBER')


missing_vars = []
if not excel_file:
    missing_vars.append('EXCEL_FILE')
if not sheet_name:
    missing_vars.append('SHEET_NAME')
if not ip_address:
    missing_vars.append('IP_ADDRESS')
if not port_number_str:
    missing_vars.append('PORT_NUMBER')


if missing_vars:
    print(f"Error: Missing environment variables: {', '.join(missing_vars)}")
    exit(1)

try:
    port_number = int(port_number_str)
except ValueError:
    print(f"Error: Invalid value for PORT_NUMBER: {port_number_str}")
    exit(1)

df = pd.read_excel(excel_file, sheet_name=sheet_name)


json_structure = {
    "configs": [
        {
            "$schema": "test",
            "config": {
                "connections": [
                    {
                        "parameters": {
                            "ipAddress": ip_address,
                            "portNumber": port_number
                        },
                        "datapoints": []
                    }
                ]
            }
        }
    ]
}


for index, row in df.iterrows():
    formatted_address = format_address(row['address'])
    datapoint = {
        "address": {
            "address_string": formatted_address
        },
        "name": row['name'],
        "access_mode": row['access_mode'],
        "parameters": {
            "acquisition_cycle": row['acquisition_cycle'],
            "acquisition_mode": row['acquisition_mode']
        },
        "data_type": row['data_type']
    }
    json_structure["configs"][0]["config"]["connections"][0]["datapoints"].append(datapoint)


json_output = json.dumps(json_structure, indent=4)


with open('output.json', 'w') as json_file:
    json_file.write(json_output)

print("JSON file created successfully.")
