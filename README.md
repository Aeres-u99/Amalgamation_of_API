# Amalgamation-of-API
An amalgamation of Multiple API's for weather forecasting and then making it an API based service with the help of flask.

#Requirements: 

-- Python 3.4+ -- 

1]. Flask

2]. Json

3]. Requests Library (for urllib2)

Installing Flask: 

[code] pip3 install requests flask json [/code]

is what you mostly need. Here for the details

http://flask.pocoo.org/docs/1.0/installation/    

https://docs.python.org/3/library/json.html      

http://docs.python-requests.org/en/master/       

How to run:

1] cd path/to/the/folder/where/repo/is
2] cd api/
3] python3 test.py 

sample output: 

%> python3 test.py                                                                                                               296ms  Thu, Jan 10, 2019  8:56:36 AM
 * Serving Flask app "test" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 212-619-498


goto browser: (preferably Mozilla firefox as it displays json in kawaii way)
goto url: 127.0.0.1:5000/

use api documentation from here on to find out the required queries for testing.


**NOTE: read following document about deployment: http://flask.pocoo.org/docs/0.12/deploying/

