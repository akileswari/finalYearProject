import os
import sys
import pythoncom
import win32com.client as client


def covx_to_pdf(filename):
    """Convert a Word .docx to PDF"""

    infile = "D:\\finalYearProject\\test1.docx"
    outfile = "D:\\finalYearProject\\static\\"+filename+".pdf"
    wdFormatPDF = 17
    pythoncom.CoInitialize()
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open(infile)
    doc.SaveAs(outfile, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()
