from django.shortcuts import render
import requests
from rest_framework.decorators import api_view, parser_classes
from django.conf import settings
from rest_framework.response import Response
from .serializers import MathQuerySerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

@api_view(['GET'])
@parser_classes([JSONParser])
def solve_question(request):
    math_query=request.query_params.get('math_query')
    url = 'http://api.wolframalpha.com/v2/query'
    headers = {'Content-Type': 'application/xml'}
    parameters = {'appid' : settings.WOLFRAM_API_KEY, 'podstate': 'Step-by-step solution', 'input': math_query}
    response = requests.get(url, params=parameters, headers=headers)
    return Response(response.content, status=status.HTTP_201_CREATED)