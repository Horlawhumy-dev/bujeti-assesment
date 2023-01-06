import os
import requests
import logging
from datetime import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .helpers import perform_apicalls_for


API_URL = str(os.getenv('API_DOMAIN_URL'))
AF_COUNTRIES_URL =  API_URL + "continents/geonames:AF/urban_areas/"

class APIResponse:

    @staticmethod
    def send(message: str, status_code: int, data: list or dict, count: int, err: str=""):
        return Response(
            {
                "message": message,
                "status_code": status_code,
                "count": count,
                "data": data,
                "error": err
            }
        )


class GetAfricanCountries(APIView):

    permissions_classes = []

    def get(request, *args, **kwargs):
        
        try:
            api_response = requests.get(AF_COUNTRIES_URL, auth=()).json()
        except KeyError or Exception as e:
            logging.debug("There was an exception. " + str(e))
            APIResponse.send(
                message="Failed. There was an error in fetching the response.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                error=str(e)
            )
            
        if "_links" not in api_response:
            
            return APIResponse.send(
                message=f"KeyErorr. African country {country} not found or mis-spelt.",
                status_code=status.HTTP_400_BAD_REQUEST,
                count=0,
                data=[]
            )
            
        african_countries = api_response["_links"]["ua:items"]
        count = api_response["count"]
        
        logging.info(f"GET Request made to fetch list of African countries around {datetime.now()}")
        
        return APIResponse.send(
            message="Success. African Countries fetched.",
            status_code=status.HTTP_200_OK,
            count=count,
            data=african_countries,
        )


class GetAfricanCountriesUrbanArea(APIView):
    
    permissions_classes = []
    
    def get(self, request, country, *args, **kwargs):
        AF_COUNTRY_URBAN_URL = API_URL + f"urban_areas/slug:{country}/"
        
        try:
            api_response = requests.get(AF_COUNTRY_URBAN_URL, auth=()).json()
        except KeyError or Exception as e:
            logging.debug("There was an exception. " + str(e))
            APIResponse.send(
                message="Failed. There was an error in fetching the response.",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                error=str(e)
            )
        if "_links" not in api_response:
            
            return APIResponse.send(
                message=f"KeyErorr. African country {country} not found or mis-spelt.",
                status_code=status.HTTP_400_BAD_REQUEST,
                count=0,
                data=[]
            )
            
            
        salaries_link = api_response["_links"]["ua:salaries"]["href"]
        scores_link = api_response["_links"]["ua:scores"]["href"]
        images_link = api_response["_links"]["ua:images"]["href"]
        details_link = api_response["_links"]["ua:details"]["href"]
        
        all_salaries = perform_apicalls_for(salaries_link)["salaries"]
        all_scores =  perform_apicalls_for(scores_link)["categories"]
        all_photos = perform_apicalls_for(images_link)["photos"]
        all_details = perform_apicalls_for(details_link)["categories"]
        
        african_urban_response = {
            "ua_id": api_response["ua_id"],
            "full_name": api_response["full_name"],
            "continent": api_response["continent"],
            "images": all_photos,
            "details": all_details,
            "scores": all_scores,
            "salaries": all_salaries,
            
            
        }
    
        logging.info(f"GET Request made to fetch African country urban area around {datetime.now()}")
        
        return APIResponse.send(
            message=f"Success. African country {country} fetched.",
            status_code=status.HTTP_200_OK,
            count=1,
            data=african_urban_response,
        )
        
        
  