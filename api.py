import requests
import json
from pprint import pprint











def getHoroscope(sign, date):
    params = (
        ('sign', sign),
        ('day', date),
        )


    data = requests.post('https://aztro.sameerkumar.website/', params=params)
    json_data = data.json()
    pprint(json_data)
    return(json_data)
