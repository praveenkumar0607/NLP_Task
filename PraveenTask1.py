import time
import requests

def call_openai_api(url, data, retries=3):
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return response
        else:
            if retries > 0:
                time.sleep(1)
                return call_openai_api(url, data, retries=retries-1)
            else:
                
                raise Exception("Maximum retries reached")
    except requests.exceptions.ConnectionError as e:
        
        print(f"ConnectionError: {e}")
        if retries > 0:
            time.sleep(1)
            return call_openai_api(url, data, retries=retries-1)
        else:
            raise Exception("Maximum retries reached")
try:
    result = call_openai_api("https://api.openai.com/v1/...", data={"input": "your_data"})
    print(result.json())
except Exception as e:
    print(f"Error: {e}")
