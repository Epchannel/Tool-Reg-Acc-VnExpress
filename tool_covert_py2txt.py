import pandas as pd

def convert_excel_to_txt(excel_path, sheet_name, txt_path, delimiter='|'):
    # Load data from the specified sheet of the Excel file
    data = pd.read_excel(excel_path, sheet_name=sheet_name)
    
    # Assuming the first row is header by default; adjust if necessary
    data.columns = [col.strip() for col in data.columns]  # Clean column names if needed
    
    # Export to TXT file with specified delimiter
    data.to_csv(txt_path, sep=delimiter, index=False, header=False)

# Usage example:
convert_excel_to_txt('path_to_your_excel_file.xlsx', 'SheetName', 'output_file.txt')
