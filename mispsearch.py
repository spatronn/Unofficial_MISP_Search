import sys

import requests
from json import JSONDecodeError
import json
from datetime import datetime

startTime = datetime.now()

def search_misp_attributes(param_value):


    headers = {
        'Authorization': 'KEYKEYKEY',
        'Accept': 'application/json',
    }
    json_data = {
        'returnFormat': 'json',
        "limit": "5",
        'value': param_value,
    }
    try:
        response = requests.post('https://misp.local/attributes/restSearch', headers=headers, json=json_data,verify=False,timeout=10)
        response.close()
    except:
        return "Unexecpted Error..."
        print(requests.exceptions.RequestException)
        sys.exit()
    try:
        resp_dict = response.json()
        search_index = 1
        list = []
        for x in resp_dict['response']['Attribute']:
            param_category = (x['category'])
            param_type = (x['type'])
            param_comment = (x['comment'])
            param_value = (x['value'])
            param_info = (x['Event']['info'])
            results = ("Search Results:" + str(search_index) + "," + "category:" + param_category + "," + "type:" + param_type + "," + "comment:" + param_comment + "," + "value:" + param_value + "," + "Event Info:" + param_info)
            list.insert(search_index, results)
            search_index += 1

        return list

    except JSONDecodeError:
        print('Response could not be serialized')



print("Elapsed Time : ", datetime.now() - startTime)
