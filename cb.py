from geopy.geocoders import Nominatim as nom
import math

city = 'Chicago'

geolocator = nom(user_agent='blah')
coord = geolocator.geocode(city)
print(coord.latitude, coord.longitude)
olat = coord.latitude
olon = coord.longitude
thetao = 0.014457
deps = 0.0628319
epso = 2

bound = True

'''
for i in range(0, 20):
	tlat = olat + thetao*math.sin(epso)
	tlon = olon + thetao*math.cos(epso)
	test = geolocator.reverse(f'{tlat},{tlon}')
	print(test.address)
	if 'Chicago' in test.address:
		olat = tlat
		olon = tlon
	else:
		thetao = thetao/2
'''