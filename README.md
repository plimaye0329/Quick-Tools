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
