import os
import sys
from docx import Document
from docx.shared import Inches
import Word2PDF as pdf
import datetime


def template():
    document = Document('D:\\finalYearProject\\test.docx')
    print(document.paragraphs)
    target = "<placeholder"
    file = "D:\\finalYearProject\\static\\copper.jpg"
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                print(cell.text)
                if target in cell.text:
                    mycell = cell.text
                    print(str(mycell))
                    arr = (str(mycell)).split('|')
                    cell.text = ""
                    height=int(arr[2].split('>')[0])/96
                    width=int(arr[1])/96
                    run = cell.paragraphs[0].add_run().add_picture(file, width=Inches(height), height=Inches(width))
                    print(arr[2])
                    print(arr[1])
                    inline_shape = run
                    # document.save('test1.docx')
                    break
                if "{{date}}" in cell.text:
                    cell.text = ""
                    date=datetime.datetime.now().strftime("%Y-%m-%d")
                    run = cell.add_paragraph(date)
                    
    for para in document.paragraphs:
        if target in para.text:
            print(para.text)
            mycell = para.text.split('|')
            height=int(mycell[2].split('>')[0])/96
            width=int(mycell[1])/96
            para.text = ""
            para.add_run().add_picture(file, width=Inches(height), height=Inches(width))
            document.save('test1.docx')
    pdf.covx_to_pdf("abc")

	
template()
