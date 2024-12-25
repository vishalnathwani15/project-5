import pandas as pd
import glob # standard lib to set multiple file set in list

filepath = glob.glob("invoices/*.xlsx") # for result ['invoices\\10001-2023.1.18.xlsx', 'invoices\\10002-2023.1.18.xlsx', 'invoices\\10003-2023.1.18.xlsx']
# print(filepath)

for i in filepath:
    df = pd.read_excel(i, sheet_name="Sheet 1")
    print(df)

