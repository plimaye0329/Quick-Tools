# MJD to UTC converter:
In some ```PSRFITS``` data files, the start MJD of observations are structured in the form of int(MJD) + seconds.
This is a quick code which takes these values and gives out the UTC time of the observation.
```
Usage: observation_time_converter.py -mjd <start_mjd> -s <start_second>

Converts the start Modified Julian Date (MJD) and start second of an observation to precise UTC time.

Options:
  -m --mjd <start_mjd>       Start Modified Julian Date (MJD) of the observation.
  -s --second <start_second>  Start second of the observation.

Author: Pranav Limaye
Institute: Max Planck Institute for Radio Astronomy
```

# Vis_Tool.py
This is a python script to visualize the source visibility. The script outputs visibility with reference to the local coordinates of the Effelsberg 100-m Radio Telescope. It is possible to change these coordinates to the preferred observatory by editing the coordinates in ```line 18``` .

```
usage: vis_tool.py [-h] ra dec date

Plot the visibility of a source. Author: Pranav Limaye, Max Planck Institute for Radio Astronomy

positional arguments:
  ra          Right ascension of the source in hh:mm:ss format.
  dec         Declination of the source in dd:mm:ss format.
  date        Date of source visibility in YYYY-MM-DD format.
```
Example Usage of the script:
```
python3 vis_tool.py "21:27:39" "+04:19:46" "2024-11-13"
```
