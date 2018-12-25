import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/',methods=['GET'])
def home():
    return "<h1>Amalgamation of Api</h1>This is a prototype API under construction"

@app.route('/api/coordinates/<str:lat_lon',methods=['GET'])
    def LatLon(): pass
@app.route('',methods=['GET'])
    def Docs(): pass
@app.route('',methods=['GET'])
    def Credits(): pass
@app.route('',methods=['GET'])
    def usage(): pass
@app.route('',methods=['GET'])
    def noLatLon(): pass 



app.run()
