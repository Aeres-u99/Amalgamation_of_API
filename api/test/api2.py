import json 
import flask as f
app = f.Flask(__name__)

@app.route('/')
def main():
    return "<h1>Homepage ASSHOLE</h1>"

@app.route('/api/')
def api(lat):
    lat=requests.args.get('lat')
    return "got lattitude as %d" % lat
app.run()
