import os

import joblib
import pandas as pd
from django.shortcuts import render

from .models import History

path=os.path.dirname(__file__)
model=joblib.load(open(os.path.join(path,'w_model.pkl'),'rb'))
label_encoder=joblib.load(open(os.path.join(path,'lbl.pkl'),'rb'))


# Create your views here.
def index(req):
    return render(req,"index.html")

def prediction(req):
    if req.method=="POST":
        temperature=req.POST['temperature']
        dew_point=req.POST['dew_point']
        humidity=req.POST['humidity']
        wind_speed=req.POST['wind_speed']
        visibility=req.POST['visibility']
        pressure=req.POST['pressure']
        parameters=["temperature","dew_point","humidity","wind_speed","visibility","pressure"]
        user_input=[temperature,dew_point,humidity,wind_speed,visibility,pressure]
        input_df=pd.DataFrame([user_input],columns=parameters)
        result=model.predict(input_df)[0]
        res=label_encoder.inverse_transform([result])[0]
        his=History(temperature=temperature,dew_point=dew_point,humidity=humidity,wind_speed=wind_speed,visibility=visibility,pressure=pressure,res=res)
        his.save()
        return render(req,"prediction.html",{"res":res})
    return render(req,"prediction.html")

def history(req):
    his=History.objects.all()
    return render(req,"history.html",{"his":his})