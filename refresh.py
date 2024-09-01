from dotenv import load_dotenv
import os
import requests

load_dotenv()

def wake_up_call():
    try:
        url_1 = os.getenv('URL1')
        url_2 = os.getenv('URL2')
        response = requests.get(f'{url_1}')
        if response.status_code == 200:
            print('Wake up call successful - 1')
        else:
            print('Wake up call failed - 1')
        response = requests.get(f'{url_2}')
        if response.status_code == 200:
            print('Wake up call successful - 2')
        else:
            print('Wake up call failed - 2')
    except Exception as e:
        print('Error occurred while making the API call', e)

if __name__ == "__main__":
    wake_up_call()
    
