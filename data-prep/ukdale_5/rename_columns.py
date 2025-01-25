import os
import pandas as pd

# Directory containing the CSV files
directory = '.'  # Change this to your directory path

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        
        # Check if 'primary_tv' column exists and rename it to 'tv'
        if 'primary_tv' in df.columns:
            df.rename(columns={'primary_tv': 'tv'}, inplace=True)
            df.to_csv(file_path, index=False)
            print(f"Updated column name in {filename}")
        else:
            print(f"No column named 'primary_tv' in {filename}")

print("Column renaming complete.")
