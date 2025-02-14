import os
import json
import zipfile

# Define folders
ip_folder = 'importFiles'  # Folder containing ZIP files
op_folder = 'jsons2'       # Folder where JSON files will be stored
ticker_file = "D:/NEU/SEM2/BigData/ASGN2/importFiles/TEST/ticker.txt"  # Path to ticker file

# Create the output folder if it doesn't exist
os.makedirs(op_folder, exist_ok=True)

# Dictionary to store CIK to Ticker mapping
ticker_mapping = {}

# Load ticker.txt and create mapping
if os.path.exists(ticker_file):
    with open(ticker_file, 'r', encoding='utf-8') as file:
        data = file.read().splitlines()
        
        # Ensure file has content
        if len(data) > 1:
            for row in data:
                values = row.split("\t")  # Assuming tab-separated values
                if len(values) >= 2:
                    ticker, cik = values[:2]  # Extract first two columns
                    cik = cik.strip().lstrip("0")  # Remove leading zeros
                    ticker_mapping[cik] = ticker.strip()

# Debugging: Print first 10 mappings to verify correct loading
print("Ticker Mapping Sample (First 10 Entries):", list(ticker_mapping.items())[:10])

# Process each ZIP file in the input folder
for file_nm in os.listdir(ip_folder):
    if file_nm.endswith('.zip'):
        zip_path = os.path.join(ip_folder, file_nm)

        # Create a subfolder in jsons2 for each ZIP file
        folder_name = os.path.splitext(file_nm)[0]  # Remove .zip extension
        zip_output_folder = os.path.join(op_folder, folder_name)
        os.makedirs(zip_output_folder, exist_ok=True)

        # Extract and process files inside the ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for zip_info in zip_ref.infolist():
                if zip_info.filename.endswith('.txt'):
                    with zip_ref.open(zip_info.filename) as file:
                        # Read and split lines
                        data = file.read().decode('utf-8').splitlines()

                        # Convert text into structured JSON (list of rows)
                        headers = data[0].split("\t")  # Assuming tab-separated headers
                        json_data = [
                            dict(zip(headers, row.split("\t"))) 
                            for row in data[1:] if len(row.split("\t")) == len(headers)
                        ]
                        
                        # Generate JSON filename and path
                        json_filename = os.path.splitext(os.path.basename(zip_info.filename))[0] + '.json'
                        json_path = os.path.join(zip_output_folder, json_filename)

                        # Save as JSON
                        with open(json_path, 'w', encoding="utf-8") as json_file:
                            json.dump(json_data, json_file, indent=4)

                        print(f"Converted: {zip_info.filename} -> {json_path}")

# Update sub.json files with ticker information
for folder in os.listdir(op_folder):
    folder_path = os.path.join(op_folder, folder)
    sub_json_path = os.path.join(folder_path, "sub.json")

    if os.path.exists(sub_json_path):
        with open(sub_json_path, "r", encoding="utf-8") as sub_file:
            sub_data = json.load(sub_file)

        for entry in sub_data:
            cik = str(entry.get("cik")).strip().lstrip("0")  # Convert to string and remove leading zeros
            entry["ticker"] = ticker_mapping.get(cik, "UNKNOWN")  # Assign ticker or mark as UNKNOWN
            
        # Debugging: Print first few entries after update
        print("Sample updated sub.json:", sub_data[:5])

        # Save updated JSON file
        with open(sub_json_path, "w", encoding="utf-8") as sub_file:
            json.dump(sub_data, sub_file, indent=4)

print(" All ZIP files have been converted, and tickers have been successfully added to sub.json!")
