"""
Some simple coordinate transformations with SunPy
Adapted from https://github.com/sunpy/sunpy/blob/master/examples/units_and_coordinates/AltAz_Coordinate_transform.py
"""
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
from sunpy.coordinates import frames, get_sunearth_distance
import astropy.units as u


obstime = "2013-09-21 16:00:00"
c = SkyCoord(
    0 * u.arcsec,
    0 * u.arcsec,
    obstime=obstime,
    frame=frames.Helioprojective
)

Fort_Sumner = EarthLocation(
    lat=34.4900*u.deg,
    lon=-104.221800*u.deg,
    height=40*u.km
)

frame_altaz = AltAz(obstime=Time(obstime), location=Fort_Sumner)
sun_altaz = c.transform_to(frame_altaz)
print('Altitude is {0} and Azimuth is {1}'.format(
    sun_altaz.T.alt, sun_altaz.T.az))

distance = get_sunearth_distance(obstime)
b = SkyCoord(
    az=sun_altaz.T.az,
    alt=sun_altaz.T.alt,
    distance=distance,
    frame=frame_altaz
)
sun_helio = b.transform_to(frames.Helioprojective)
print('The helioprojective point is {0}, {1}'.format(
    sun_helio.T.Tx, sun_helio.T.Ty))
