import http.client, urllib.request, urllib.parse, urllib.error, base64
a = input()
a=int(a)
i=1
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{069d3275f0b14875b705c655c2de077e}',
}
params = urllib.parse.urlencode({
})
for i in range(1,a):
    str=input()
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", str % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))