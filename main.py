
from flask import Flask,request,jsonify
import pickle
import numpy as np

model = pickle.load(open('threats.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    Region = request.form.get('Region')
    Plateau  = request.form.get('Plateau')
    Earthquake_Richter = request.form.get('Earthquake_Richter')
    Hurricanes = request.form.get('Hurricanes')
    Typhoons = request.form.get('Typhoons')
    Tsunamis = request.form.get('Tsunamis')
    Lightning = request.form.get('Lightning')
    Active_Volcanoes = request.form.get('Active_Volcanoes')
    Floods = request.form.get('Floods')
    Tornadoes = request.form.get('Tornadoes')
    Temperature = request.form.get('Temperature')
    AQI = request.form.get('AQI')
    Sea_Levels = request.form.get('Sea_Levels')
    Radiation = request.form.get('Radiation')
    Population_Density = request.form.get('Population_Density')
    Emergency_Response_Capabilities = request.form.get('Emergency_Response_Capabilities')






    input_query = np.array([[Region,Plateau,Earthquake_Richter,Hurricanes,Typhoons,Tsunamis,Lightning,Active_Volcanoes,Floods,Tornadoes,Temperature,AQI,Sea_Levels,Radiation,Population_Density,Emergency_Response_Capabilities]])
  #  print(input_query)
    result = model.predict(input_query)

    return jsonify({"Percentage_Threat_Zone": str(result)})






if __name__  == '__main__':
    app.run(debug=True)

