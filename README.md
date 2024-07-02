# SLMP Tagger :tada:

## Table of Content

[[_TOC_]]

## Project Overview

## Project Description

This project features a Python script designed to read data from an Excel file (.xlsx) and output a structured JSON format.
The JSON output can be seamlessly integrated into a common configurator, facilitating the easy addition of tags.
By utilizing environment variables for configuration, the script offers enhanced flexibility and ease of use.

## Requirements

Excel file (.xlsx) should have the following data column and format:

- `name`
- `address`
- `acquisition_mode`
- `data_type`
- `access_mode`
- `acquisition_cycle`

<div style="text-align:center">
  ![Alt Text](./images/tagSheet.png)
</div>

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine. You can use the following command if you're using Git:
HTTPS

```sh
git clone https://code.siemens.com/eh-prg-dev/slmp-tagger.git
```

SSH

```sh
git clone git@code.siemens.com:eh-prg-dev/slmp-tagger.git

```

Navigate to the project directory:

```sh
cd your_project_directory
```

### 2. Create and Activate a Virtual Environment

You can create and activate a virtual environment as follows:

#### For Windows:

```sh
python -m venv env
.\env\Scripts\activate
```

#### For macOS and Linux:

```sh
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the requirements.txt file:

```sh
pip install -r requirements.txt
```

### 4. Set Up the Environment Variables

Replace in inputs.env file with the values with your specific configuration:

```
EXCEL_FILE=xxxxx.xlsx
SHEET_NAME=xxxxx
IP_ADDRESS=x.x.x.x.x
PORT_NUMBER=xxxxx
```

- `EXCEL_FILE:` The name of your Excel file.
- `SHEET_NAME:` The sheet name within the Excel file.
- `IP_ADDRESS:` The IP address to be used in the JSON output.
- `PORT_NUMBER:` The port number to be used in the JSON output.

### 5. Running the Script

Ensure your environment is set up correctly, then run the script:

```sh
python tagger.py
```

If everything is set up correctly, the script will read the Excel file, process the data, and create an output.json file in the project directory.

### 6. Outputting JSON

The script writes the constructed JSON structure to output.json.

### 7. Usage

Using the output.json file.

- `Go to Common Configurator`
- `Click on Get Data`
- `Add data source`
- `Select the target data source and click Restore`
- `Select the output.json file`

### 8. Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
