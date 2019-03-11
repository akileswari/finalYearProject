import os
import sys
import pythoncom
import win32com.client as client


def Ppt_to_pdf(filename,infilepath):
    """Convert a PPT .pptx to PDF"""

    infile = infilepath
    outfile = "F:\\PycharmProjects\\finalproject\\static\\"+filename+".pdf"
    formatType = 32
    pythoncom.CoInitialize()
    #powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint = client.Dispatch("Powerpoint.Application")
    deck = powerpoint.Presentations.Open(infile)
    deck.SaveAs(outfile, formatType) 
    deck.Close()
    powerpoint.Quit()


