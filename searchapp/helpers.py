      
import logging 
import requests


def perform_apicalls_for(api_link: str):
    try:
        api_response = requests.get(api_link, auth=()).json()
    except Exception as e:
        logging.debug("There was an exception. " + str(e))
    return api_response