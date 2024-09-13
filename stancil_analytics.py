'''
This project works with imports, both Standard Library and External, 
creating a virtual environment, and working with data
'''

#Import Standard Library dependencies 

import csv
import json
import pathlib
import re
import logging
from collections import Counter

#Import External Library Dependencies 
import requests
import pandas as pd

#Import Local Modules 
import stancil_projsetup
import utils_stancil


# Configure logging to replace print statements and track program execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


#Function for writing TEXT data to file 

def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Try opening the file and writing the data to it
        with file_path.open('w', encoding='utf-8') as file:
            file.write(data)
        logging.info(f"Text data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing text file {file_path}: {e}")

#Define Function for saving Text data 

def fetch_and_write_txt_data(folder_name, filename, url, verify=True):
    """Fetch data from a URL and write it to a text file."""
    try:
        # Fetch the data from the URL, with SSL verification enabled
        response = requests.get(url, verify=True)  # Enable SSL verification
        response.raise_for_status()  # Raise HTTPError for bad responses
        response.encoding = 'utf-8'  # Ensure the response is interpreted as UTF-8
        write_txt_file(folder_name, filename, response.text) # Save the fetched data to a text file
    except requests.RequestException as e:
        # Log any errors encountered during data fetching
        logging.error(f"Failed to fetch data from {url}: {e}")


#Define Function for writing excel data to file

def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with open(file_path, 'wb') as file:
            file.write(data)
        logging.info(f"Excel data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing Excel file {file_path}: {e}")

#Define Function for saving Excel Data

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")


#Define Function for writing JSON Data to file

def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"JSON data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing JSON file {file_path}: {e}")

#Define Function for saving JSON Data 

def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")


#Define Function for writing CSV data to file 

def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        with file_path.open('w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        logging.info(f"CSV data saved to {file_path}")
    except IOError as e:
        logging.error(f"Error writing CSV file {file_path}: {e}")

#Define Function for saving CSV Data 

def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")
    

#Implement Function to Process Text Data (count words and unique words, save summary)

def process_text_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
         #Try opening the file and reading its contents
        with file_path.open('r', encoding='utf-8') as file:
            text = file.read()
    except IOError as e:
        # Log any errors encountered during file reading and exit the function
        logging.error(f"Error reading text file {file_path}: {e}")
        return

    try:
        # Extract words from the text and count occurrences
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = set(words)
        word_count = Counter(words)
        total_words = len(words)
        unique_word_count = len(unique_words)

        # Write the summary of word counts to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Total Words: {total_words}\n")
            output_file.write(f"Unique Words: {unique_word_count}\n")
            output_file.write(f"\nWord Frequency:\n")
            for word, count in word_count.most_common():
                output_file.write(f"{word}: {count}\n")
        logging.info(f"Text processing complete. Results saved to {output_path}")
    except Exception as e:
        logging.error(f"Error processing text data: {e}")


#Implement Function to process and extract data from Excel Files 

def process_excel_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        cs = pd.read_excel(file_path)
        summary = {
            'Total Rows': len(cs),
            'Total Columns': len(cs.columns),
            'Column Names': list(cs.columns),
            'Numeric Column Statistics': cs.describe().to_string()
        }

        # Write the summary to the output file
        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Summary of Excel Data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    output_file.write(f"{key}:\n{value}\n\n")
                else:
                    output_file.write(f"{key}: {value}\n")
        logging.info(f"Excel data processing complete. Results saved to {output_path}")
    except IOError as e:
        logging.error(f"Error reading Excel file {file_path}: {e}")
    except pd.errors.EmptyDataError:
        logging.error(f"Excel file is empty or not readable: {file_path}")
    except pd.errors.ExcelFileError as e:
        logging.error(f"Error reading Excel file {file_path}: {e}")

#Implement Function to process JSON Data and extract relevant information 

def process_json_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding='utf-8') as file:
            json_data = json.load(file)

        #Summarize the JSON data by counting the top-level keys and their types
        summary = {'Number of Items': len(json_data)}

        if isinstance(json_data, list) and len(json_data) > 0 and isinstance(json_data[0], dict):
            summary['Keys in JSON objects'] = list(json_data[0].keys())

        output_path = pathlib.Path(folder_name).joinpath(output_filename)
        with output_path.open('w', encoding='utf-8') as output_file:
            output_file.write(f"Summary of JSON Data:\n")
            for key, value in summary.items():
                if isinstance(value, str):
                    output_file.write(f"{key}:\n{value}\n\n")
                else:
                    output_file.write(f"{key}: {value}\n")
        logging.info(f"JSON data processing complete. Results saved to {output_path}")
    except IOError as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON data: {e}")

#Implement Function to process and extract data from CSV File with meaningful statistics

def process_csv_data(folder_name, input_filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(input_filename)
    try:
        with file_path.open('r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the header row
            column_summaries = ['Column Summary:'] + headers

            data = []
            for row in reader:
                data.append(tuple(row))

            # Summarize each column by counting non-empty entries
            column_counts = [0] * len(headers)
            for row in data:
                for i, value in enumerate(row):
                    if value:
                        column_counts[i] += 1

            # Write the summary to the output file
            output_path = pathlib.Path(folder_name).joinpath(output_filename)
            with output_path.open('w', encoding='utf-8') as output_file:
                output_file.write(f"Total Rows: {len(data)}\n")
                output_file.write(f"\nColumn Summaries:\n")
                for header, count in zip(headers, column_counts):
                    output_file.write(f"{header}: {count} entries\n")
            logging.info(f"CSV processing complete. Results saved to {output_path}")
    except IOError as e:
        logging.error(f"Error reading or writing CSV file: {e}")
    except csv.Error as e:
        logging.error(f"Error processing CSV data: {e}")

#Main Module for running code in terminal

def main():

    # Print byline from imported module
    print(f"Byline: {utils_stancil.byline}")
    
    # Define the prefix for the folders
    prefix = 'data-'

    # Define the folder names for each data type
    folder_names = ['txt', 'csv', 'excel', 'json']

    # Create folders using the prefixed naming
    result = stancil_projsetup.create_prefixed_folders(folder_names, prefix)
    print(result)

    # Define the base directory relative to the script's location
    base_dir = pathlib.Path(__file__).parent.joinpath('data')

    # Define URLs for data fetching
    txt_url = 'https://raw.githubusercontent.com/YunfeiMaSophie/Support-Vector-Machines-and-Spam-Classifier/master/emailSample2.txt'
    csv_url = 'https://raw.githubusercontent.com/vatsalkpatel/SampleCSV/main/Wage.csv'
    excel_url = 'https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fbharathirajatut%2Fsample-excel-dataset%2Fmaster%2Fasparas.xls&wdOrigin=BROWSELINK'
    json_url = 'http://api.open-notify.org/astros.json'

    # Define filenames for data storage
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Define full paths for each folder
    txt_folder = pathlib.Path(base_dir).joinpath(f'{prefix}txt')
    csv_folder = pathlib.Path(base_dir).joinpath(f'{prefix}csv')
    excel_folder = pathlib.Path(base_dir).joinpath(f'{prefix}excel')
    json_folder = pathlib.Path(base_dir).joinpath(f'{prefix}json')

    # Fetch and write data to files
    fetch_and_write_txt_data(txt_folder, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder, json_filename, json_url)

    # Process the fetched data
    process_text_data(txt_folder, txt_filename, 'results_txt.txt')
    process_csv_data(csv_folder, csv_filename, 'results_csv.txt')
    process_excel_data(excel_folder, excel_filename, 'results_xls.txt')
    process_json_data(json_folder, json_filename, 'results_json.txt')

    print("Data fetching and processing complete.")


if __name__ == "__main__":
    main()




