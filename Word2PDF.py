import os
import sys
import pythoncom
import win32com.client as client
import comtypes.client

pythoncom.CoInitialize()
infile="F:\\PycharmProjects\\finalproject\\test1.docx"
outfile="F:\\PycharmProjects\\finalproject\\out1.pdf"
wdFormatPDF = 17


def covx_to_pdf():
    """Convert a Word .docx to PDF"""

    #word = comtypes.client.CreateObject('Word.Application')
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open(infile)
    doc.SaveAs(outfile, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
covx_to_pdf()

