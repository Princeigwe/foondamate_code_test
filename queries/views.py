from django.shortcuts import render
import requests
from rest_framework.decorators import api_view, parser_classes
from django.conf import settings
from rest_framework.response import Response
from .serializers import MathQuerySerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def solve_question(request):
    math_query=request.query_params.get('math_query')
    if request.method == 'GET':
        url = 'http://api.wolframalpha.com/v2/query'
        headers = {'Content-Type': 'application/xml'}
        parameters = {'appid' : settings.WOLFRAM_API_KEY, 'podstate': 'Step-by-step solution', 'input': math_query}
        response = requests.get(url, params=parameters, headers=headers)
        return Response(response.content, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    # math_query_serializer = MathQuerySerializer(data=request.data)
    # if math_query_serializer.is_valid():
    #     url = 'http://api.wolframalpha.com/v2/query'
    #     headers = {'Content-Type': 'application/xml'}
    #     parameters = {'appid' : settings.WOLFRAM_API_KEY, 'podstate': 'Step-by-step%20solution', 'input': math_query_serializer}
    #     response = requests.get(url, params=parameters, headers=headers)
    #     return Response(response.content, status=status.HTTP_201_CREATED)
    # return Response(math_query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)