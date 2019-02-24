import quandl
import pandas as pd
quandl.ApiConfig.api_key = "y6HGamWceWTnsqypSb5p"
import curr as cd

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


    iron=pd.DataFrame(quandl.get("COM/FE_TJN",rows=15))
    i_data=(inr*iron['Column 1'][14])/1000
    dif_i=round(((iron['Column 1'][14]-iron['Column 1'][13])/iron['Column 1'][13])*100,4)
    date_i = pd.Timestamp(iron.iloc[[14]].index.tolist()[0]).date()
    value_i = []
    d_i_lis = []
    for i in range(0, 15):
        t = str(pd.Timestamp(iron.iloc[[i]].index.tolist()[0]).date())
        d_i_lis.append(t)
        value_i.append(round(iron['Column 1'][i]))

    ni=pd.DataFrame(quandl.get("COM/FE_TJN", rows=15))
    ni_data=round((inr*ni['Column 1'][14])/1000,2)
    dif_n=round(((ni['Column 1'][14]-ni['Column 1'][13])/ni['Column 1'][13])*100,4)
    date_n = pd.Timestamp(copper.iloc[[14]].index.tolist()[0]).date()
    value_n = []
    d_n_lis = []
    for i in range(0, 15):
        t = str(pd.Timestamp(ni.iloc[[i]].index.tolist()[0]).date())
        d_n_lis.append(t)
        value_n.append(round(ni['Column 1'][i]))

    return(a_data,dif_a,c_data,dif_c,i_data,dif_i,ni_data,dif_n,date_c,date_a,date_i,date_n,value_c,d_c_lis,value_a,d_a_lis,value_i,d_i_lis,value_n,d_n_lis)








