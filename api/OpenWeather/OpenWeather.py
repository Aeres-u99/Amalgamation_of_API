import json
#import ipaddress as ip_
from urllib.request import urlopen as u


api_url="https://api.openweathermap.org/data/2.5/weather?"
api_key=""
subpart = "appid="
def api_call(url):
    client=u(url)
    page=client.read()
    client.close()
    return page

def getData_by_lat_lon(lat,lon):
    lat=str(lat)
    lon=str(lon)
    query = api_url+"lat="+lat+"&"+"lon="+lon+"&"+subpart+api_key
    page = api_call(query)
    parsed_json = json.loads(page)
    return parsed_json


def getData_by_City(city_name):
    query = api_url+"q="+city_name+"&"+subpart+api_key
    page = api_call(query)
    parsed_json=json.loads(page)
    return parsed_json


def getData_by_Postalcode(postal_code):
    postal_code = str(postal_code)
    query = api_url+"q="+postal_code+"&"+subpart+api_key
    page = api_call(query)
    parsed_json = json.loads(page)
    return parsed_json

def getData_by_ip(ip_address):
    ip_api_url = "http://ip-api.com/json/"
    ip_api_url+=ip_address
    page = api_call(ip_api_url)
    parsed_json = json.loads(page)
    lat = parsed_json['lat']
    lon = parsed_json['lon']
    ip_data = getData_by_lat_lon(lat,lon)
    return ip_data


def check_function(data,typeofdata):
    pass


