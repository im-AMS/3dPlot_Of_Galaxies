from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np

points = 10
ra = np.random.randint(360, size=(points))
dec = np.random.randint(-90, 90, size=(points))
distance = np.random.randint(80, 150, size=(points))

data = SkyCoord(ra=ra * u.degree, dec=dec * u.degree, distance=distance * u.kpc)
# print(dec)
x=data.cartesian.x
y=data.cartesian.y
z=data.cartesian.z

print(x,y,z)

