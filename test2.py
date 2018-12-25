import flask 
from flask import request, jsonify, render_template 
import ipaddress as tre
import api.parser.selectiveParser as sp
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
query_param= {
        "lat":"",
        "lon":"",
        "city":"",
        "pin":"",
        "ip":""
        }
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
    if 'city' in requests.args:
        city=requests.args['city']
        l['city'] = city
    if 'lat' in requests.args:
        lat = requests.args['lat']
        l['lat'] = lat
    if 'lon' in requests.args:
        lon = requests.args['lon']
        l['lon'] = lon
    if 'ip' in requests.args:
        ip = requests.args['ip']
        try:
            ipadd = tre.ip_address(ip)
            l['ip']=ip
        except:
            render_template("error.html")
    if 'pin' in requests.args['pin']:
        pin = requests.args['pin']
        l['pin'] = pin
    else:
        return render_template("error.html")

    print(requests.args)
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

        

