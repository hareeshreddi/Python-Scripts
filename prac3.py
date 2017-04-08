import socket
#socket.getaddrinfo('202.141.80.24', 3128)
import http.client, urllib.request, urllib.parse, urllib.error, base64,sys
import urllib.parse
import urllib.request
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{faf27a3b3c86412aab8b72447479b090}',
}
params = urllib.parse.urlencode({
})
a =int(input())
for i in range(0,a):
    str=input()
    body="{ 'url': str }"
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        y=data[0]["scores"]['neutral']
        d=data[0]["scores"]
        for key in d:
            x=data[0]["scores"][key]
            if x>y:
                y=x
        for name, value in d.iteritems():
            if value == y:
                print(name)
        print(getkey(x))       
        conn.close()
    except Exception as e:
        print(e.args)