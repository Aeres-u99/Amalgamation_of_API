import flask 
from flask import request, jsonify, render_template 
import ipaddress as tre
import selectiveParser as sp


app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
        {
            'id': 0,
            'title': 'A fire upon the deep',
            'first_sentence': 'The coldsleep itself was was dreamless',
            'year_published': '1992'},
        {
            'id': 1,
            'title': 'A fire upon the deep',
            'first_sentence': 'The coldsleep itself was was dreamless',
            'year_published': '1992'},
        {
            'id': 2,
            'title': 'A fire upon the deep',
            'first_sentence': 'The coldsleep itself was was dreamless',
            'year_published': '1992'},
        ]
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

    print(request.args)
    return jasonify(l)






    '''
        print(request.args)
        city=(request.args['city'])
        
    else:
        return render_template("api.html") 
    
    results= []

    for book in books:
        if book['id'] == id:
            results.append(book)
            results.append(request.args)
            results.append(request.remote_addr)
            results.append(request.environ['REMOTE_ADDR'])
    return jsonify(results)
@app.route('/testing/',methods=['GET'])
def api_credits():
    return '''
   
    
app.run(host='0.0.0.0')

        

