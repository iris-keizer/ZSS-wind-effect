#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer(url="https://api.ecmwf.int/v1",key="e919a5492b2062f00b02d0fb2252d4b5",email="iris.keizer@knmi.nl")




for year in range(1980, 2020):
    server.retrieve({
        "class": "ei",
        "dataset": "interim",
        "date": f"{year}0101/{year}0201/{year}0301/{year}0401/{year}0501/{year}0601/{year}0701/{year}0801/{year}0901/{year}1001/{year}1101/{year}1201",
        "expver": "1",
        "grid": "0.125/0.125",
        "levtype": "sfc",
        "param": "165.128/166.128",
        "stream": "moda",
        "type": "an",
        "area": "55/0/50/10",
        "format": "netcdf",
        "target": f"/Users/iriskeizer/Documents/Zeespiegelscenarios/data/era interim/raw/interim_{year}-01-01to{year}-12-01_.nc",
        })
