import requests

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Richmond,VA&destination=Washington,DC&mode=driving'
resp = requests.get(url)

print "API Response Status: " + str(resp.status_code)

print resp.json()




