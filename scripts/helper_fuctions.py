from io import BytesIO
import pandas as pd

def read_txt_file(filename):
    items = []
    with open(filename,  encoding = 'utf-8') as file:
        for line in file:
            items.append(line.rstrip())
    return items

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data