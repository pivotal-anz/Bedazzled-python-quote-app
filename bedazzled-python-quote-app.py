import os
import pprint
import logging
from flask import Flask
from math import sqrt
import urllib, urllib2
  
app = Flask(__name__)
quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
quote_ret_val = ""

logging.basicConfig(level=logging.DEBUG)

def go_get_quote (quote_symbol):
    global quote_ret_val
    get_quote_url = quote_url + quote_symbol
    req = urllib2.Request(get_quote_url)
    req.add_header('User-Agent', 'Mozilla/5.0')
    response = urllib2.urlopen(req)
    quote_ret_val = response.read()
    print quote_ret_val 
    print "============oo============="
    print "retrieved quote from server"
    print "============oo============="
      

@app.route('/quote/<company_symbol>')
def get_quote(company_symbol):
    global quote_ret_val
    if len(quote_ret_val) == 0:
        go_get_quote(company_symbol)
        got_quote = 1


    #    tot = 0.00
    for i in range (0, 100000):
        tot = sqrt(i)
    #print tot
    return quote_ret_val

port = os.getenv('PORT', '5000')
print port 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))