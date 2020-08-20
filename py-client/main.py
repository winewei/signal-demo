import requests
import logging, sys

API_URL = "http://api:8080/test"
CLIENT = "py3"

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s"
                    )

def test_call():
    for step in range(1,1001):
        for i in range(1,6):
            p = "client=" + CLIENT + "&" + "job=" + str(step) + "&" + "subJob=" + str(i)
            req = requests.get(url=API_URL,params=p)
            logging.info(req.text)

if __name__ == '__main__':
    test_call()