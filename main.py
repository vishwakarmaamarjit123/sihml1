
from flask import Flask,request,jsonify
import pickle
import pandas
import numpy as np

model = pickle.load(open('threats.pkl','rb'))
model1 = pickle.load(open('impacts.pkl','rb'))
earths = pickle.load(open('earth1.pkl','rb'))
eds = pickle.load(open('edss.pkl','rb'))



app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"


@app.route('/percentage', methods=['POST'])
def predict1():
    Region = request.form.get('Region')
    Plateau  = np.random.choice([0,1])
    Earthquake_Richter = request.form.get('Earthquake_Richter')
    Hurricanes = np.random.choice([0,1])
    Typhoons = np.random.choice([0,1])
    Tsunamis = np.random.choice([0,1])
    Lightning = np.random.choice([0,1])
    Active_Volcanoes = np.random.choice([0,1])
    Floods = np.random.choice([0,1])
    Tornadoes = np.random.choice([0,1])
    Temperature = request.form.get('Temperature')
    AQI = request.form.get('AQI')
    Sea_Levels = request.form.get('Sea_Levels')
    Radiation =    np.random.uniform(0,100)
    Population_Density = np.random.uniform(10, 1000)
    Emergency_Response_Capabilities = request.form.get('Emergency_Response_Capabilities')






    input_query = np.array([[Region,Plateau,Earthquake_Richter,Hurricanes,Typhoons,Tsunamis,Lightning,Active_Volcanoes,Floods,Tornadoes,Temperature,AQI,Sea_Levels,Radiation,Population_Density,Emergency_Response_Capabilities]])
  #  print(input_query)
    result = model.predict(input_query)

    return jsonify({"Percentage_Threat_Zone": str(result)})




@app.route('/impact', methods=['POST'])
def impact():
    Region = request.form.get('Region')
    pressure_kpa = request.form.get('pressure_kpa')
    Temperature = request.form.get('Temperature')
    AQI = request.form.get('AQI')
    toxic = request.form.get('toxic')
    flammability = request.form.get('flammability')
    humidityper = request.form.get('humidity-per')
    windspeed_mh = request.form.get('windspeed_mh')
    Radiation = np.random.uniform(0,100)
    volume_kl = request.form.get('volume_kl')
    releaserate_pou = request.form.get('releaserate_pou')
    rockdens_kgmc = request.form.get('rockdens_kgmc')






    input_queryty = np.array([[Region,pressure_kpa,Temperature,AQI,toxic,flammability,humidityper,windspeed_mh,Radiation,volume_kl,releaserate_pou,rockdens_kgmc]])
  #  print(input_query)
    result1 = model1.predict(input_queryty)

    return jsonify({"impactzone": str(result1)})


@app.route('/eds', methods=['POST'])
def edds():
   
    pressure_kpa = request.form.get('pressure_kpa')
    Temperature = request.form.get('Temperature')
    AQI = request.form.get('AQI')
    toxic = request.form.get('toxic')
    flammability = request.form.get('flammability')
    humidityper = request.form.get('humidity-per')
    windspeed_mh = request.form.get('windspeed_mh')
    Radiation = np.random.uniform(0,100)
    presence_flam_gas = request.form.get('presence_flam_gas')
    
   






    input_querytyy = np.array([[pressure_kpa,Temperature,AQI,toxic,flammability,humidityper,windspeed_mh,Radiation,presence_flam_gas]])
  #  print(input_query)
    result2 = eds.predict(input_querytyy)

    return jsonify({"eds_percent": str(result2)})





@app.route('/earth', methods=['POST'])
def earthss():
   
    Latitude = request.form.get('Latitude')
    Longitude = request.form.get('Longitude')
   
    
   






    input_querytyy1 = np.array([[Latitude,Longitude]])
  #  print(input_query)
    result2ea = earths.predict(input_querytyy1)

    return result2ea



    
       





if __name__  == '__main__':
    app.run(debug=True)

