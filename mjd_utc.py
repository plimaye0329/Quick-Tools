#!/usr/bin/env python3
"""
Usage: observation_time_converter.py -mjd <start_mjd> -s <start_second>

Converts the start Modified Julian Date (MJD) and start second of an observation to precise UTC time.

Options:
  -m --mjd <start_mjd>       Start Modified Julian Date (MJD) of the observation.
  -s --second <start_second>  Start second of the observation.

Author: Pranav Limaye
Institute: Max Planck Institute for Radio Astronomy
"""

import datetime
import sys
import getopt

def mjd_to_utc(mjd):
    """Convert Modified Julian Date (MJD) to UTC date."""
    return datetime.datetime(1858, 11, 17) + datetime.timedelta(days=mjd)

def precise_utc_time(start_mjd, start_second):
    """Calculate the precise UTC time of observation."""
    # Convert start second to fraction of a day
    fraction_of_day = start_second / (24 * 60 * 60)

    # Calculate precise MJD
    precise_mjd = start_mjd + fraction_of_day

    # Convert precise MJD to UTC time
    precise_utc = mjd_to_utc(precise_mjd)

    return precise_utc

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:s:", ["mjd=", "second="])
    except getopt.GetoptError:
        print(__doc__)
        sys.exit(1)

    start_mjd = None
    start_second = None

    for opt, arg in opts:
        if opt == "-h":
            print(__doc__)
            sys.exit(0)
        elif opt in ("-m", "--mjd"):
            start_mjd = float(arg)
        elif opt in ("-s", "--second"):
            start_second = float(arg)

    if start_mjd is None or start_second is None:
        print("Missing required arguments.")
        print(__doc__)
        sys.exit(1)

    # Calculate precise UTC time of observation
    observation_time = precise_utc_time(start_mjd, start_second)

    print("Time of Observation (UTC):", observation_time)

