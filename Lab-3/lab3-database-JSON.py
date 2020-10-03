from urllib.request import *
from urllib.parse import *
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa
# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7" # If it doesn’t work, get your own.
# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
 # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results
main_data = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (main_data["temp"], degreeSym ))
print ("Humidity: %d%%" % main_data["humidity"])
print ("Pressure: %d" % main_data["pressure"] )

wind_data = data["wind"]
print ("Wind : %d" % wind_data["speed"])

dbconnect = sqlite3.connect("mydatabase.db")
dbconnect.row_factory = sqlite3.Row
cursor = dbconnect.cursor()

cursor.execute('CREATE TABLE city_weather (city TEXT, temp NUMERIC, humidity NUMERIC, pressure NUMERIC, windSpeed  NUMERIC)')
cursor.execute('INSERT INTO city_weather values(?, ?, ?, ?, ?)', (city, main_data["temp"], main_data["humidity"],
                                                                  main_data["pressure"], wind_data["speed"]))
dbconnect.commit()
print ("Wind speed is %d" % wind_data['speed'])
