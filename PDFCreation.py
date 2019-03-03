import os
import sys
from docx import Document
from docx.shared import Inches
import Word2PDF as pdf


def template(file):
    document = Document('F:\\PycharmProjects\\finalproject\\test.docx')
    print(document.paragraphs)
    target = "<placeholder"
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                print(cell.text)
                if target in cell.text:
                    mycell = cell.text
                    print(str(mycell))
                    arr = (str(mycell)).split('|')
                    cell.text = ""
                    run = cell.paragraphs[0].add_run().add_picture(file, width=Inches(1), height=Inches(1))
                    print(arr[2])
                    print(arr[1])
                    inline_shape = run
                    # document.save('test1.docx')
                    break
    for para in document.paragraphs:
        if target in para.text:
            print(para.text)
            mycell = para.text.split('|')
            para.text = ""
            para.add_run().add_picture(file, width=Inches(1), height=Inches(1))
            document.save('test1.docx')
    pdf.covx_to_pdf(file.filename)


