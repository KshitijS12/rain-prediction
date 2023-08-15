import pickle
import json
import numpy as np


def Reading_Artifacts():

    print('Loading Artifacts...')
    
    with open("../models/Rain_Prediction.pickle",'rb') as f:
        a = pickle.load(f)
        b = pickle.load(f)
        c = pickle.load(f)

    with open("../data/Columns.json",'r') as f:
        d = json.load(f)['Data Columns']
    
    print("...Artifacts Loaded")
    return a,b,c,d    
    
_scaling_model, _learning1_model, _learning2_model, _data_columns = Reading_Artifacts()

def Show_Columns():
    return _data_columns

def Predict(mT,MT,ppt, Evap, Sun, WSp, WS9, WS3, Hm9, Hm3,
            P9, Cld9, Cld3, Month,
            Loc, WD, WD9, WD3):
    i = np.zeros(len(_data_columns))
    
    
    i[0] = mT
    i[1] = MT
    i[2] = ppt
    i[3] = Evap
    i[4] = Sun
    i[5] = WSp
    i[6] = WS9
    i[7] = WS3
    i[8] = Hm9
    i[9] = Hm3
    i[10] = P9
    i[11] = Cld9
    i[12] = Cld3
    
    Month = Month.strip().lower()
    Loc = Loc.strip().lower()
    WD = WD.strip().lower()
    WD9 = WD9.strip().lower()
    WD3 = WD3.strip().lower()
    
    if(Month != 'apr'):
        k = _data_columns.index(Month)
        i[k] = 1
    
    if(Loc != 'adelaide'):
        l = _data_columns.index(Loc)
        i[l] = 1
    
    WD = 'w_' + WD
    if(WD != 'w_e'):
        m = _data_columns.index(WD)
        i[m] = 1
        
    WD9 = 'w9_' + WD9
    if(WD9 != 'w9_e'):
        n = _data_columns.index(WD9)
        i[n] = 1
        
    WD3 = 'w3_' + WD3
    if(WD3 != 'w3_e'):
        o = _data_columns.index(WD3)
        i[o] = 1
    
    
    [i[:13]] = _scaling_model.transform([i[:13]])   
    
    
    Res1 = _learning1_model.predict([i])[0]
    if(Res1 == 1):
        Res1 = "It will Rain Today"
    else:
        Res1 = "It will not Rain Today"
    
    Res2 = _learning2_model.predict([i])[0]
    if(Res2 == 1):
        Res2 = "It will Rain Tomorrow"
    else:
        Res2 = "It will not Rain Tomorrow"
    
    ResP1 = "Chances of Rain Today: " + str((round(_learning1_model.predict_proba([i])[0][1],
                 4) * 100)) + "%"
    
    ResP2 = "Chances of Rain Tomorrow: " + str((round(_learning2_model.predict_proba([i])[0][1],
                 4) * 100)) + "%"
    
    return Res1, ResP1, Res2, ResP2
    
   
'''  
a, b, c, d = Predict(19.0, 27.0, 1.0, 5.0, 9.5, 69.0, 18.0,
               32.5, 52, 54, 1000, 3,
               2, 'Apr', 'Albury', 'E', 'SSe', 'NNW')    


 
print('Forecast')
print('-'*9)
print(a)    
print(b) 
print("\n") 
print(c)
print(d)    
'''