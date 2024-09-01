from dotenv import load_dotenv
import os
import requests

load_dotenv()

def wake_up_call():
    try:
        url = os.getenv('URL')
        response = requests.get(f'{url}')
        if response.status_code == 200:
            print('Wake up call successful')
        else:
            print('Wake up call failed')
    except Exception as e:
        print('Error occurred while making the API call', e)

if __name__ == "__main__":
    wake_up_call()
    
