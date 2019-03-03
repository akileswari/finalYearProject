import requests
import pandas as pd

def indian_rs():
    request=requests.get("http://apilayer.net/api/live?access_key=c23e69e95430b32a6d1e4b0fa372c24e&currencies=INR&format=1")
    content=pd.DataFrame(request.json())
    #print(content)
    inr=float(content['quotes'])
    return (inr)



#h=indian_rs()
#print(h)
# http://apilayer.net/api/live?access_key=c23e69e95430b32a6d1e4b0fa372c24e&currencies=USD,AUD,CAD,PLN,MXN&format=1