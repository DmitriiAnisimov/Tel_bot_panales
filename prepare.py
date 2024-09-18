import pandas as pd
from datetime import datetime
import re

current_date = datetime.now().strftime('%Y-%m-%d')
# Load the CSV file into a pandas DataFrame
df = pd.read_csv(f'data/pampers/assembly_data/{current_date}_pampers.csv')


def determine_size(description):
    # Convert the description to lowercase to ensure case insensitivity
    description = description.lower()

    # Define regex pattern to handle different size descriptions, including 'recien nacido' and spelling variations
    size_pattern = r'\b(?:talle|talla)?\s?(xxxg|xxg|xg(?:d)?|g(?:de)?|m(?:ed)?|p(?:eq|equeño)?|rn|recien nacido|recién nacido|recien nacidos|recién nacidos|px)(\d*)\b'

    # Search for the pattern in the description
    match = re.search(size_pattern, description)
    if match:
        size = match.group(1)  # Extract the size designation
        # Normalize variations explicitly
        if 'gde' in size:
            size = 'G'  # Normalize 'Gde' to 'G'
        elif 'peq' in size or 'pequeño' in size or 'px' in size:
            size = 'P'  # Normalize 'Peq', 'Pequeño', and 'Px' to 'P'
        elif 'xgd' in size:
            size = 'XG'  # Normalize 'Xgd' to 'XG'
        elif 'med' in size:
            size = 'M'  # Normalize 'Med' to 'M'
        elif 'rn' in size or 'recien nacido' in size or 'recién nacido' in size or 'recien nacidos' in size or 'recién nacidos' in size:
            size = 'RN'  # Normalize 'RN' and variations of 'recien nacido' to 'RN'
        elif 'xxxg' in size:
            size = 'XXXG'  # Normalize 'XXXG' to 'XXXG'
        if match.group(2):  # Check if there are numbers immediately following the size
            size += match.group(2)  # Include the number with the size label if present
        return size.upper()  # Return the matched size, possibly with numbers, converted to uppercase

    return 'unknown'  # Return 'unknown' if no size indicator is found


def extract_quantity(description):
    # Pattern to find a number followed by various unit indicators with or without periods
    # (\d+) captures one or more digits (the quantity)
    # \s* allows for any whitespace (including none) between the number and the unit indicator
    # U[dn]i?\.{0,2} matches 'Ud', 'Un', 'Uni' with optional 'i' and up to 2 periods
    # Additionally, matches 'u', 'uni', or 'u.' at the end of a string
    # (\s|$) ensures it ends with a space or end of the string
    match1 = re.search(r'(\d+)\s*(U[dn]i?\.{0,2}|u|uni|u\.)(\s|$)',
                       description)

    if match1:
        # Return the first group of the match,
        # which is the number before the unit indicator, as an integer
        return int(match1.group(1))

    # If no match is found in the first pattern,
    # search for any quantity elsewhere in the description
    # The pattern (\d+) captures one or more digits (the quantity)
    match2 = re.search(r'(\d+)', description)
    if match2:
        # Return the first group of the match,
        # which is the number found in the description, as an integer
        return int(match2.group(1))

    return 1  # Return 0 if no match is found


def extract_brand(description):
    # Convert the description to lowercase for case-insensitive matching
    description_lower = description.lower()

    # Check if the word 'Pampers' is present in the description
    if 'pampers' in description_lower:
        return 'Pampers'
    # Check if the word 'Babysec' is present in the description
    elif 'babysec' in description_lower:
        return 'Babysec'
    # Check if the word 'Estrella' is present in the description
    elif 'estrella' in description_lower:
        return 'Estrella'
    # Check if the word 'Huggies' is present in the description
    elif 'huggies' in description_lower or 'haggies' in description_lower:
        return 'Huggies'
    # Check if the word 'Carrefour' is present in the description
    elif 'carrefour' in description_lower:
        return 'Carrefour'
    elif 'duffy' in description_lower:
        return 'Duffy'
    else:
        return 'Other'


# Apply the function to the 'description' column
df['brand'] = df['description'].apply(extract_brand)

# Apply the function to the 'Description' column
# to create a new column 'TwoBeforeU'
df['quantity'] = df['description'].apply(extract_quantity)


# Apply the function to the 'Description'
# column to create the new 'Size' column
df['size'] = df['description'].apply(determine_size)

# Convert the 'Price' column from str to float
df['price'] = df['price'].str.replace(",", ".").astype(float)

# Apply the function to each row to calculate 'unit_price'
df['unit_price'] = round(df['price'] / df['quantity'].astype(int))

# Remove rows where Quantity equals 1
df = df[df['quantity'] != 1]

# Save the modified DataFrame back to a CSV file (optional)
df.to_csv(f'data/pampers/to_db/{current_date}_prepared_csv_file.csv', index=False)

print(f"CSV file has been prepared and saved to 'data/pampers/to_db/{current_date}_prepared_csv_file.csv'")
