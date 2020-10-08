import httplib
import urllib

key = "7ZSLCJR2MDWPLT9A"
group = "L3-T-5"
email = "benbozec@cmail.carleton.ca"
id = "b"

def write_data_thingspeak():
 params = urllib.urlencode({'api_key': key, 'field1': group, 'field2': email, 'field3': id})
 conn= httplib.HTTPConnection("api.thingspeak.com:80")
 try:
  conn.request("POST", "/update", params) 
  print(reponse.status, response.reason)
  data = response.read()
  conn.close()
 except:
  print("connection failed")
if __name__ == '__main__':
 write_data_thingspeak()