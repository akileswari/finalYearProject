import os
import sys


import win32com.client as client

infile="F:\\PycharmProjects\\finalproject\\PDF Reporting\\test1.docx"
outfile="F:\\PycharmProjects\\finalproject\\PDF Reporting\out1.pdf"
wdFormatPDF = 17


def covx_to_pdf():
    """Convert a Word .docx to PDF"""

    # word = comtypes.client.CreateObject('Word.Application')
    word = client.DispatchEx("Word.Application")
    doc = word.Documents.Open(infile)
    doc.SaveAs(outfile, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

covx_to_pdf()
