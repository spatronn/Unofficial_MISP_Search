import requests
from datetime import datetime
import schedule
import time



def fetchfeed():
    startTime = datetime.now()
    headers = {
        'Authorization': 'KEYKEYKEY',
        'Accept': 'application/json',
    }
    try:
        response = requests.post('https://misp.local/feeds/fetchFromAllFeeds', headers=headers, verify=False,timeout=10)
        response.close()
        print(response.content)
    except:
        return "Unexecpted Error..."
        print(requests.exceptions.RequestException)

    print("Elapsed Time : ", datetime.now() - startTime)

schedule.every().hour.at(":01").do(fetchfeed)

while True:
    schedule.run_pending()
    time.sleep(1)

