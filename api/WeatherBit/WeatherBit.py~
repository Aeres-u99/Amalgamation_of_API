import json 
import ipaddress as ip_
from urllib.request import urlopen as u



api_url = "https://api.weatherbit.io/v2.0/current?"
api_key = "8c3c69db6d6e49ea9797b2b622c153a9"

def api_call(url):
    client=u(url)
    page=client.read()
    client.close()
    return page


def getData_by_lat_lon(lat,lon):
    lat=str(lat)
    lon=str(lon)
    query=api_url+"lat="+lat+"&"+"lon="+lon+"&key="+api_key
    page=api_call(query)
    parsed_json=json.loads(page)
    return parsed_json


def getData_by_City(city_name):
    query=api_url+"city="+city_name+"&key="+api_key
    page= api_call(query)
    parsed_json=json.loads(page)
    return parsed_json


def getData_by_Postalcode(postal_code):
    postal_code = str(postal_code)
    query=api_url+"postal_code="+postal_code+"&key="+api_key
    page = api_call(query)
    parsed_json = json.loads(page)
    return parsed_json


def getData_by_ip(ip_address):
    ip_address=str(ip_address)
    query=api_url+"ip="+ip_address+"&key="+api_key
    page = api_call(query)
    parsed_json = json.loads(page)
    return parsed_json

def check_function(data,typeofdata):
    pass

def get_Currentstatus():
    pass

def get_Forecast():
    pass

