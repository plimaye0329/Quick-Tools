import argparse
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
from astropy.time import Time
import astropy.units as u
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Parse command line arguments
parser = argparse.ArgumentParser(description='Plot the visibility of a source. Author: Pranav Limaye, Max Planck Institute for Radio Astronomy')
parser.add_argument('ra', type=str, help='Right ascension of the source in hh:mm:ss format.')
parser.add_argument('dec', type=str, help='Declination of the source in dd:mm:ss format.')
parser.add_argument('date', type=str, help='Date of source visibility in YYYY-MM-DD format.')
args = parser.parse_args()

# Define your location (latitude, longitude, elevation)
your_location = EarthLocation(lat=50.52*u.deg, lon=6.88*u.deg, height=319*u.m)

# Define the specific date for which you want to plot the visibility
specific_date = args.date
start_time = Time(specific_date + "T00:00:00")
end_time = Time(specific_date + "T23:59:59")
time_range = Time(np.linspace(start_time.jd, end_time.jd, 100), format='jd')

# Convert RA and Dec from hh:mm:ss and degrees:mm:ss respectively to degrees
# Convert RA and Dec from hh:mm:ss and degrees:mm:ss respectively to degrees with proper units
source_coords = SkyCoord(ra=args.ra, dec=args.dec, unit=(u.hourangle, u.deg), frame='icrs')

# Convert the source coordinates to AltAz frame for your location
alt_az_frame = AltAz(obstime=time_range, location=your_location)
source_altaz = source_coords.transform_to(alt_az_frame)

# Plotting
quantity_support()
plt.figure(figsize=(10, 6))
plt.plot(time_range.datetime, source_altaz.alt, label='Source')
plt.axhline(20, color='k', linestyle='--', linewidth=1, label='elevation limit')
plt.xlabel('Time (UTC) on ' + specific_date)
plt.ylabel('Altitude (degrees)')
plt.title('Visibility of Source on ' + specific_date)
plt.legend(loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()
