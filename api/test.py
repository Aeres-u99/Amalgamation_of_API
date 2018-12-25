import flask 
from flask import request, jsonify, render_template 
import ipaddress as tre
import selectiveParser as sp
import indivParse as ivp

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def home_main():
    return render_template("api.html")

@app.route('/index.html',methods=['GET'])
def home_main2():
    return render_template("api.html")

@app.route('/credits',methods=['GET'])
def home_credits():
    return render_template("api.html")

@app.route('/about-us',methods=['GET'])
def home_abtus():
    return render_template("api.html")
   
@app.route('/docs',methods = ['GET'])
def home_docs():
    return render_template("api.html")
    
@app.route('/api/sample/',methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/',methods=['GET'])
def api_id():
    l= {
        "lat":" ",
        "lon":" ",
        "city":" ",
        "pin":" ",
        "ip":" ",
        }
    
    if 'city' in request.args:
        city=request.args['city']
        l['city'] = city
        page = sp.parse_acc_city(l['city'])
        return jsonify(page)

    elif 'lat' in request.args:
        lat = request.args['lat']
        l['lat'] = lat
        if 'lon' in request.args:
            lon = request.args['lon']
            l['lon'] = lon
            page = sp.parse_acc_lat_lon(l['lat'],l['lon'])
            return jsonify(page)
        else:
            return "<h3>param_error: missing parameters</h3>"
    elif 'ip' in request.args:
        ip = request.args['ip']
        try:
            ipadd = tre.ip_address(ip)
            l['ip']=ip
            page = sp.parse_acc_ip(l['ip'])
            return jsonify(page)

        except:
            render_template("error.html")
    elif 'pin' in request.args:
        pincode = request.args['pin']
        l['pin'] = pincode
        page = sp.parse_acc_postal_code(pincode)
        return jsonify(page)

    else:
        return render_template("error.html")


@app.route('/api/sel/ds/',methods=['GET'])
def api_ds():
    l= {
        "lat":" ",
        "lon":" ",
        "city":" ",
        "pin":" ",
        "ip":" ",
        }
    
    if 'city' in request.args:
        city=request.args['city']
        l['city'] = city
        page = ivp.ds_parse_acc_city(l['city'])
        return jsonify(page)

    elif 'lat' in request.args:
        lat = request.args['lat']
        l['lat'] = lat
        if 'lon' in request.args:
            lon = request.args['lon']
            l['lon'] = lon
            page = ivp.ds_parse_lat_lon(l['lat'],l['lon'])
            print(page)
            return jsonify(page)
        else:
            return "<h3>param_error: missing parameters</h3>"
    elif 'ip' in request.args:
        ip = request.args['ip']
        try:
            ipadd = tre.ip_address(ip)
            l['ip']=ip
            page = ivp.ds_parse_acc_ip_add(l['ip'])
            return jsonify(page)

        except:
            render_template("error.html")
    
    elif 'pin' in request.args:
        pincode = request.args['pin']
        l['pin'] = pincode
        page = ivp.ds_parse_acc_postal_code(pincode)
        return jsonify(page)

    else:
        return render_template("error.html")


@app.route('/api/sel/ow/',methods=['GET'])
def api_ow():
    l= {
        "lat":" ",
        "lon":" ",
        "city":" ",
        "pin":" ",
        "ip":" ",
        }
    
    if 'city' in request.args:
        city=request.args['city']
        l['city'] = city
        page = ivp.ow_parse_acc_city(l['city'])
        return jsonify(page)

    elif 'lat' in request.args:
        lat = request.args['lat']
        l['lat'] = lat
        if 'lon' in request.args:
            lon = request.args['lon']
            l['lon'] = lon
            page = ivp.ow_parse_lat_lon(l['lat'],l['lon'])
            print(page)
            return jsonify(page)
        else:
            return "<h3>param_error: missing parameters</h3>"
    elif 'ip' in request.args:
        ip = request.args['ip']
        try:
            ipadd = tre.ip_address(ip)
            l['ip']=ip
            page = ivp.ow_parse_acc_ip_add(l['ip'])
            return jsonify(page)

        except:
            render_template("error.html")
    
    elif 'pin' in request.args:
        pincode = request.args['pin']
        l['pin'] = pincode
        page = ivp.ow_parse_acc_postal_code(pincode)
        return jsonify(page)

    else:
        return render_template("error.html")

@app.route('/api/sel/axu/',methods=['GET'])
def api_axu():
    l= {
        "lat":" ",
        "lon":" ",
        "city":" ",
        "pin":" ",
        "ip":" ",
        }
    
    if 'city' in request.args:
        city=request.args['city']
        l['city'] = city
        page = ivp.axu_parse_acc_city(l['city'])
        return jsonify(page)

    elif 'lat' in request.args:
        lat = request.args['lat']
        l['lat'] = lat
        if 'lon' in request.args:
            lon = request.args['lon']
            l['lon'] = lon
            page = ivp.axu_parse_lat_lon(l['lat'],l['lon'])
            print(page)
            return jsonify(page)
        else:
            return "<h3>param_error: missing parameters</h3>"
    elif 'ip' in request.args:
        ip = request.args['ip']
        try:
            ipadd = tre.ip_address(ip)
            l['ip']=ip
            page = ivp.axu_parse_acc_ip_add(l['ip'])
            return jsonify(page)

        except:
            render_template("error.html")
    
    elif 'pin' in request.args:
        pincode = request.args['pin']
        l['pin'] = pincode
        page = ivp.axu_parse_acc_postal_code(pincode)
        return jsonify(page)

    else:
        return render_template("error.html")

   
@app.route('/api/sel/wb/',methods=['GET'])
def api_wb():
    l= {
        "lat":" ",
        "lon":" ",
        "city":" ",
        "pin":" ",
        "ip":" ",
        }
    
    if 'city' in request.args:
        city=request.args['city']
        l['city'] = city
        page = ivp.wb_parse_acc_city(l['city'])
        return jsonify(page)

    elif 'lat' in request.args:
        lat = request.args['lat']
        l['lat'] = lat
        if 'lon' in request.args:
            lon = request.args['lon']
            l['lon'] = lon
            page = ivp.wb_parse_lat_lon(l['lat'],l['lon'])
            print(page)
            return jsonify(page)
        else:
            return "<h3>param_error: missing parameters</h3>"
    elif 'ip' in request.args:
        ip = request.args['ip']
        try:
            ipadd = tre.ip_address(ip)
            l['ip']=ip
            page = ivp.wb_parse_acc_ip_add(l['ip'])
            return jsonify(page)

        except:
            render_template("error.html")
    
    elif 'pin' in request.args:
        pincode = request.args['pin']
        l['pin'] = pincode
        page = ivp.wb_parse_acc_postal_code(pincode)
        return jsonify(page)

    else:
        return render_template("error.html")

  
app.run(host='0.0.0.0')
