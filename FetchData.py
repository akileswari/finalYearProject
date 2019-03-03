import quandl
import pandas as pd
quandl.ApiConfig.api_key = "y6HGamWceWTnsqypSb5p"
import DollarToINR as cd

def curr_rate():
    inr=cd.indian_rs()
    copper=pd.DataFrame(quandl.get("CHRIS/MCX_CU1",rows=15,))
    c_data=copper['Close'][14]
    dif_c=round(((copper['Close'][14]-copper['Close'][13])/copper['Close'][0])*100,4)
    date_c = pd.Timestamp(copper.iloc[[14]].index.tolist()[0]).date()
    value_c = []
    d_c_lis = []
    for i in range(0, 15):
        t = str(pd.Timestamp(copper.iloc[[i]].index.tolist()[0]).date())
        d_c_lis.append(t)
        value_c.append(round(copper['Close'][i]))

    alum=pd.DataFrame(quandl.get("CHRIS/MCX_AL1",rows=15))
    a_data=alum['Close'][14]
    dif_a=round(((alum['Close'][14]-alum['Close'][13])/alum['Close'][13])*100,4)
    date_a = pd.Timestamp(alum.iloc[[14]].index.tolist()[0]).date()
    value_a = []
    d_a_lis = []
    for i in range(0, 15):
        t = str(pd.Timestamp(alum.iloc[[i]].index.tolist()[0]).date())
        d_a_lis.append(t)
        value_a.append(round(alum['Close'][i]))

    gold=pd.DataFrame(quandl.get("LBMA/GOLD",rows=15))
    gold_data = round((inr * gold['USD (PM)'][14])/31.1035, 2)
    dif_g = round(((gold['USD (PM)'][14] - gold['USD (PM)'][13]) / gold['USD (PM)'][13]) * 100, 4)
    date_g = pd.Timestamp(gold.iloc[[14]].index.tolist()[0]).date()
    value_g = []
    d_g_lis = []
    for i in range(0, 15):
        t = str(pd.Timestamp(gold.iloc[[i]].index.tolist()[0]).date())
        d_g_lis.append(t)
        value_g.append(round((inr * gold['USD (PM)'][i])/31.1035, 2))


    silver=pd.DataFrame(quandl.get("LBMA/SILVER",rows=15))
    silver_data = round((inr * silver['USD'][14])/31.1035, 2)
    dif_s = round(((silver['USD'][14] - silver['USD'][13]) / silver['USD'][13]) * 100, 4)
    date_s = pd.Timestamp(silver.iloc[[14]].index.tolist()[0]).date()
    value_s = []
    d_s_lis = []
    for i in range(0, 15):
        t = str(pd.Timestamp(silver.iloc[[i]].index.tolist()[0]).date())
        d_s_lis.append(t)
        value_s.append(round((inr * silver['USD'][i])/31.1035, 2))

    return(a_data,dif_a,c_data,dif_c,silver_data,dif_s,gold_data,dif_g,date_c,date_a,date_s,date_g,value_c,d_c_lis,value_a,d_a_lis,value_s,d_s_lis,value_g,d_g_lis)





