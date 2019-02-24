
import requests
import pandas as pd
from datetime import datetime,timedelta


def news_feed(q):
    to_date=datetime.now().strftime ("%Y-%m-%d")
    f_date =(datetime.now() + timedelta(days=-5)).strftime("%Y-%m-%d")
    url ="https://newsapi.org/v2/everything?q=retail+"+q+"+metal+price&from="+f_date+"&to="+to_date+"&language=en&apiKey=1bffda1be46c4579923afde29a275b3d"
    response = requests.get(url)
    sam=pd.DataFrame(pd.DataFrame(response.json()['articles']))
    s=[]
    l=len(sam.index)
    if l==0:
        url = "https://newsapi.org/v2/everything?q=retail+" + q + "+metal+price&language=en&apiKey=1bffda1be46c4579923afde29a275b3d"
        response = requests.get(url)
        sam = pd.DataFrame(pd.DataFrame(response.json()['articles']))
        l = len(sam.index)
    if l>5:
        l=5
    for i in range(0,l):
        s.append([sam['url'][i],sam['title'][i]])
    return (s)