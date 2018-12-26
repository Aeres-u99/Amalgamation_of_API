import json 
import ipaddress as ip_
from urllib.request import urlopen as u

api_url = "https://api.apixu.com/v1/current.json?key="
api_key = ""



def get_Currentstatus():
    pass

def get_Forecast():
    pass

def api_call(url):
    client=u(url)
    page=client.read()
    client.close()
    return page


def getData_by_lat_lon(lat,lon):
    lat=str(lat)
    lon=str(lon)
    query=api_url+api_key+"&q="+lat+","+lon
    page=api_call(query)
    parsed_json=json.loads(page)
    return parsed_json


def getData_by_City(city_name):
    query=api_url+api_key+"&q="+city_name
    page= api_call(query)
    parsed_json=json.loads(page)
    return parsed_json


def getData_by_Postalcode(postal_code):
    postal_code = str(postal_code)
    query=api_url+api_key+"&q="+postal_code
    page = api_call(query)
    parsed_json = json.loads(page)
    return parsed_json


def getData_by_ip(ip_address):
    ip_address=str(ip_address)
    query = api_url+api_key+"&q="+ip_address
    page = api_call(query)
    parsed_json = json.loads(page)
    return parsed_json

def check_function(data,typeofdata):
    pass


