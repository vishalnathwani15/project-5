import pandas as pd
import glob # standard lib to set multiple file set in list
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("invoices/*.xlsx") # for result ['invoices\\10001-2023.1.18.xlsx', 'invoices\\10002-2023.1.18.xlsx', 'invoices\\10003-2023.1.18.xlsx']
# print(filepath)

for i in filepath:
    df = pd.read_excel(i, sheet_name="Sheet 1")
    # print(df)
    pdf = FPDF(orientation="p", unit="mm",format="A4")
    pdf.add_page()
    name = Path(i).stem
    invoice_name = name.split('-')[0]
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=50,h=0,txt=f"Invoice.no: {invoice_name}")
    pdf.output(f"PDFs/{name}.pdf")

