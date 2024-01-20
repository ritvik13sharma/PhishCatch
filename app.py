from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import json
import requests
import urllib


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    
    class IPQS:
        key = 'mK9YTxYFutT8HFg5njAqppNKdckapoZS'
        def malicious_url_scanner_api(self, url: str, vars: dict = {}) -> dict:
            url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
            x = requests.get(url, params = vars)
            print(x.text)
            return (json.loads(x.text))

    if __name__ == "__main__":        

        URL = msg

        strictness = 0

        additional_params = {
        'strictness' : strictness
            }

        ipqs = IPQS()
        result = ipqs.malicious_url_scanner_api(URL, additional_params)

        
        if 'success' in result and result['success'] == True:
            
            status=result['message']
            Unsafe=result['unsafe']
            IPadd=result['ip_address']
            spamming=result['spamming']
            malware=result['malware']
            Phishing=result['phishing']
            suspicious=result['suspicious']
            risk_sc=result['risk_score']
            
            def true_f(val):
                if(val==True):
                   return "True"
                else:
                   return "False"
            
            

            resp = MessagingResponse()

            resp.message("Account_name: "+"*RITVIK SHARMA*"+"\n\nProject:        "+"*PhishCatch*"+"\n\nStatus:         "+"*"+status+"*"+"\nUnsafe:        "+"*"+true_f(Unsafe)+"*"+"\nSpamming:  "+"*"+true_f(spamming)+"*"+"\nMalware:     "+"*"+true_f(malware)+"*"+"\nPhishing:     "+"*"+true_f(Phishing)+"*"+"\nSuspicious:  "+"*"+true_f(suspicious)+"*".format(msg))

            return str(resp)
        
        else:

            resp = MessagingResponse()            
            resp.message("Account_name: "+"*RITVIK SHARMA*"+"\n\nProject:        "+"*PhishCatch*"+"\n\nStatus:         "+"*Success*"+"\nUnsafe:        "+"*False*"+"\nSpamming:  "+"*False*"+"\nMalware:     "+"*False*"+"\nPhishing:     "+"*False*"+"\nSuspicious:  "+"*False*".format(msg))
            return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    