import pandas as pd
import sqlite3
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

# Specify the path to the CSV file
csv_file_path = f'data/pampers/to_db/{current_date}_prepared_csv_file.csv'

# Specify the path to the SQLite database file
sqlite_db_path = 'database/pampers.db'  # You can change this path as needed

# Specify the name of the table to be created in the database
table_name = 'pampers'

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert the 'Unit_price' column to numeric using `pd.to_numeric` with `errors='coerce'`
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

# Convert the 'Unit_price' column to integer, treating NaN as None
df['unit_price'] = df['unit_price'].astype('int')


df = df.drop_duplicates()

# Create an SQLite database connection

conn = sqlite3.connect(sqlite_db_path)

df.to_sql(table_name, conn, if_exists='append', index=False)

cursor = conn.cursor()

conn.commit()


# Inform the user that the data has been written to the SQLite database
print(f"Data has been written to the SQLite database: {sqlite_db_path}, Table: {table_name}")
