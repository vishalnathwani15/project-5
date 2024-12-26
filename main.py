import pandas as pd
import glob # standard lib to set multiple file set in list
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("invoices/*.xlsx") # for result ['invoices\\10001-2023.1.18.xlsx', 'invoices\\10002-2023.1.18.xlsx', 'invoices\\10003-2023.1.18.xlsx']
# print(filepath)

for i in filepath:
    # print(df)
    pdf = FPDF(orientation="p", unit="mm",format="A4")
    pdf.add_page()
    name = Path(i).stem
    # invoice_name = name.split('-')[0]
    # date = name.split('-')[1]   ######################## we can write as per below also both are same
    invoice_name, date = name.split("-")
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice.no: {invoice_name}", ln=1)
    pdf.set_font(family="Arial", size=16, style="B")
    pdf.cell(w=50,h=8,txt=f"date: {date}", ln=3)

    df = pd.read_excel(i, sheet_name="Sheet 1")
    # Add a header
    colums = df.columns
    colums = [item.replace("_"," ").title() for item in colums]
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30, h=8, txt=colums[0], border=1)
    pdf.cell(w=70, h=8, txt=colums[1], border=1)
    pdf.cell(w=30, h=8, txt=colums[2], border=1)
    pdf.cell(w=30, h=8, txt=colums[3], border=1)
    pdf.cell(w=30, h=8, txt=colums[4], border=1, ln=1)

    # Add a product
    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=30,h=8,txt=str(row["product_id"]), border=1)
        pdf.cell(w=70,h=8,txt=str(row["product_name"]), border=1)
        pdf.cell(w=30,h=8,txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30,h=8,txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30,h=8,txt=str(row["total_price"]), border=1, ln=1)
    
    total_price = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30,h=8,txt="", border=1)
    pdf.cell(w=70,h=8,txt="", border=1)
    pdf.cell(w=30,h=8,txt="", border=1)
    pdf.cell(w=30,h=8,txt="", border=1)
    pdf.cell(w=30,h=8,txt=str(total_price), border=1, ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=28,h=25,txt=f"Total Price is {total_price}" , ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=28,h=8,txt="PythonHow")
    pdf.image("pythonhow.png",w=10,h=10)

   
    pdf.output(f"PDFs/{name}.pdf")

