import csv
from datetime import datetime, timedelta
import os

# Define file paths
yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
current_date = datetime.now().strftime('%Y-%m-%d')

yesterday_csv_file_path = f'data/pampers/{yesterday_date}_pampers.csv'

other_csv_file_paths = [f'carrefour/carrefour_data_pampers/{current_date}_Carrefour.csv',
                        f'jumbo/jumbo_data_pampers/{current_date}_Jumbo.csv',
                        f'dia/dia_data_pampers/{current_date}_Dia.csv',
                        f'farmacity/farmacity_data_pampers/{current_date}_Farmacity.csv']

today_csv_file_path = f'data/pampers/assembly_data/{current_date}_pampers.csv'


# Read data
# from a CSV file and return it as a list of rows
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read and skip the header row
        for row in reader:
            data.append(row)
    return data, header


# Write combined data to the new CSV file
def write_to_csv(data, header, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(header)
        # Write the data
        writer.writerows(data)


# Combine data from yesterday's file and other files
def combine_data(yesterday_file, other_files):
    combined_data = []
    header = None

    # Check if yesterday's file exists
    if os.path.exists(yesterday_file):
        yesterday_data, header = read_csv(yesterday_file)
        combined_data.extend(yesterday_data)
    else:
        # Assume any other file has a header we can use
        # if yesterday's file is absent.
        for other_file in other_files:
            if os.path.exists(other_file):
                data, header = read_csv(other_file)
                combined_data.extend(data)
                break  # Use the first file header as default

    # Read data from other files and combine them
    for file_path in other_files:
        if os.path.exists(file_path):
            data, _ = read_csv(file_path)
            combined_data.extend(data)

    return combined_data, header


# Main function to update today's CSV file
def update_today_file():
    # Combine data from yesterday's file and other files
    combined_data, header = combine_data(yesterday_csv_file_path,
                                         other_csv_file_paths)

    # Write combined data to today's file
    write_to_csv(combined_data, header, today_csv_file_path)

    print(f"Data has been updated and saved to {today_csv_file_path}")


# Call the function to update today's file
update_today_file()

print(f"Data has been updated and saved to {today_csv_file_path}")
