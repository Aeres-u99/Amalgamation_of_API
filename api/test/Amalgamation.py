import ipaddress as ipAddr
#from urllib.request import urlopen as uo
import flask 
from flask import request, jsonify, render_template 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def home():
    return '''
    <h1> Okay so the plan now is to study it well and proper</h1>
    <h2> dont rush thru things :) </h2>
    <h3> good, stage 1 cleared take your time and solve it one by one </h3>
    '''
@app.route('/api/all',methods=['GET'])
def api_all():
    return "implementing ..."

@app.route('/api/',methods=['GET'])
def api_id():
    if 'lat' or 'lon' or 'ip' in request.args:
        print(request.args)
        lat=float(request.args['lat'])
        lon=float(request.args['lon'])
        print(lat)
        print(lon)
            
    
    else:
        return render_template("home.html") 
    
    return "%f %f " % (lat,lon)
@app.route('/credits/',methods=['GET'])
def api_credits():
    return '''
    <h1>This page is meant to contain the credits information </h1>
    '''

app.run()

        

