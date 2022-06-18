from flask import Flask , request

import Rain_Predict_Utility

app = Flask(__name__)

@app.route('/Data_Columns')
def Columns():
    C = {'Columns' : Rain_Predict_Utility.Show_Columns()}
    return C

@app.route('/Predict_Rain', methods = ['POST'])
def predict_rain():
    mT =  float(request.form['Minimum Temperature'])
    MT =  float(request.form['Maximum Temperature'])
    ppt =  float(request.form['Precipitation'])
    Evap =  float(request.form['Evaporation'])
    Sun =  float(request.form['Sunshine'])
    WSp =  float(request.form['Wind Gust Speed'])
    WS9 =  float(request.form['Wind Speed at 9am'])
    WS3 = float(request.form['Wind Speed at 3pm'])
    Hm9 = float(request.form['Humidity at 9am'])
    Hm3 = float(request.form['Humidity at 3pm'])
    P9 = float(request.form['Air Pressure at 9am'])
    Cld9 = int(request.form['Cloud Cover at 9am'])
    Cld3 = int(request.form['Cloud Cover at 3pm'])
    Month = request.form['Month']
    Loc = request.form['Location']
    WD = request.form['Wind Gust Direction']
    WD9 = request.form['Wind Direction at 9am']
    WD3 = request.form['Wind Direction at 3m']

    H = {'Predictions' : 
         Rain_Predict_Utility.Predict(mT,MT,ppt,Evap,
                                      Sun,WSp,WS9,WS3,Hm9,
                                      Hm3,P9,
                                      Cld9,Cld3,Month,
                                      Loc,WD,WD9,WD3)}
    return H


app.run()