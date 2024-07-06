import requests
import time

# Configuration
URL = "https://www.youtube.com/"  # URL of the application to check
CHECK_INTERVAL = 3  # in seconds

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{time.ctime()}: Application is UP. Status code: {response.status_code}")
        else:
            print(f"{time.ctime()}: Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{time.ctime()}: Application is DOWN. Error: {e}")

if __name__ == "__main__":
    while True:
        check_application_health(URL)
        time.sleep(CHECK_INTERVAL)
