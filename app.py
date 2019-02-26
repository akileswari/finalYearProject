import requests
import pandas as pd
from flask import Flask, render_template, request, session, make_response, json, send_file
import new as rate
import newsfeed as feed
import curr as cd
import export as docConv
import Word2PDF as pdf
import win32com.client as client
app = Flask(__name__)
app.secret_key="123"

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/dashboard')
def dashboard():
    al,a_d,cu,c_d,ir,i_d,ni,ni_d,d_c,d_a,d_i,d_n,val_c,d_c_lis,val_a,d_a_lis,val_i,d_i_lis,val_n,d_n_lis=rate.curr_rate()
    al_f=feed.news_feed("aluminium")
    cu_f = feed.news_feed("copper")
    ir_f = feed.news_feed("iron")
    ni_f = feed.news_feed("nickel")
    inr=cd.indian_rs()
    return render_template('dashb.html',al=al,cu=cu,ir=ir,ni=ni,a_d=a_d,c_d=c_d,i_d=i_d,ni_d=ni_d,al_f=al_f,cu_f=cu_f,ir_f=ir_f,ni_f=ni_f,d_c=d_c,
                           d_a=d_a,d_i=d_i,d_n=d_n,val_c=val_c,d_c_lis=d_c_lis,val_a=val_a,d_a_lis=d_a_lis,val_i=val_i,d_i_lis=d_i_lis,val_n=val_n,
                           d_n_lis=d_n_lis,inr=inr)

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    # document=Document("test.docx")
    # #document.add_paragraph('A plain paragraph having some ')
    # document.add_picture("F:\\PycharmProjects\\finalproject\\PDF Reporting\\image.jpg",width=Inches(2.0),height=Inches(2.0))
    # document.save("demo.docx")
    docConv.template()
    
    return send_file("F:\\PycharmProjects\\finalproject\\out1.pdf",mimetype='application/*',as_attachment=True,attachment_filename="output.pdf")

if __name__ == '__main__':
    app.run(port=4545, debug=True)



