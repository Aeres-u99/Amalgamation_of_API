import json
from urllib.request import urlopen

api_url= "https://api.darksky.net/forecast/"
api_key= "19ea13cc0bfc2639b10f4b121939e17f"

def getData_by_lat_lon(lat,lon):
    lat=str(lat)
    lon=str(lon)
    query=api_url+api_key+"/"+lat+","+lon
    Client = urlopen(query)
    page= Client.read()
    Client.close()
    parsed_json = json.loads(page)
    return parsed_json

def getData_by_City(city_name):
    page= {
  "latitude": "",
  "longitude": "",
  "timezone": "null",
  "currently": {
    "time": "",
    "summary": "null",
    "icon": "null",
    "precipIntensity": "null",
    "precipProbability": "null",
    "temperature": "null",
    "apparentTemperature": "null",
    "dewPoint": "null",
    "humidity": "null",
    "pressure": "null",
    "windSpeed": "null",
    "windGust": "null",
    "windBearing": "null",
    "cloudCover": "null",
    "uvIndex": "null",
    "visibility": "null",
    "ozone": 215.41
  }
  ,
  "daily": {
    "summary": "",
    "icon": "clear-day"
  },
  "flags": {
    "sources": [
      "cmc",
      "gfs",
      "icon",
      "isd",
      "madis"
    ],
    "nearest-station": 1.099,
    "units": "us"
  },
  "offset": 5.5
}
    return page


def getData_by_Postalcode(postal_code):
    page= {
  "latitude": "",
  "longitude": "",
  "timezone": "null",
  "currently": {
    "time": "",
    "summary": "null",
    "icon": "null",
    "precipIntensity": "null",
    "precipProbability": "null",
    "temperature": "null",
    "apparentTemperature": "null",
    "dewPoint": "null",
    "humidity": "null",
    "pressure": "null",
    "windSpeed": "null",
    "windGust": "null",
    "windBearing": "null",
    "cloudCover": "null",
    "uvIndex": "null",
    "visibility": "null",
    "ozone": 215.41
  }
  ,
  "daily": {
    "summary": "null",
    "icon": "null"
  },
  "flags": {
    "sources": [
      "cmc",
      "gfs",
      "icon",
      "isd",
      "madis"
    ],
    "nearest-station": "null",
    "units": "null"
  },
  "offset": 5.5
}
    return page


def getData_by_ip(ip_address):
    page= {
  	"latitude": "",
  	"longitude": "",
  	"timezone": "null",
  	"currently": {
    "time": "",
    "summary": "null",
    "icon": "null",
    "precipIntensity": "null",
    "precipProbability": "null",
    "temperature": "null",
    "apparentTemperature": "null",
    "dewPoint": "null",
    "humidity": "null",
    "pressure": "null",
    "windSpeed": "null",
    "windGust": "null",
    "windBearing": "null",
    "cloudCover": "null",
    "uvIndex": "null",
    "visibility": "null",
    "ozone": "null"
  }
  ,
  "daily": {
    "summary": "",
    "icon": "clear-day"
  },
  "flags": {
    "sources": [
      "cmc",
      "gfs",
      "icon",
      "isd",
      "madis"
    ],
    "nearest-station": 1.099,
    "units": "us"
  },
  "offset": 5.5
}
    return page
   

