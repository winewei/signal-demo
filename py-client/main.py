import requests
import logging
import signal, sys, os

API_URL = "http://api:8080/test"
CLIENT = "py3"

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s"
                    )

SI = True
def SI_STATUS(a,b):
    logging.info("Got signal: %s" % a)
    global SI
    SI = False

def test_call():
    for step in range(1,1001):
        signal.signal(signal.SIGTERM, SI_STATUS)
        logging.info("Thread PID： %s" % os.getpid())
        if SI:
            for i in range(1,6):
                signal.signal(signal.SIGUSR1, SI_STATUS)
                p = "client=" + CLIENT + "&" + "job=" + str(step) + "&" + "subJob=" + str(i)
                req = requests.get(url=API_URL,params=p)
                logging.info("req data: %s" % req.text)
        else:
            logging.info("Exit...")
            sys.exit()

if __name__ == '__main__':
    test_call()