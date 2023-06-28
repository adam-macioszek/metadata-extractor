from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from extractor.extract import extract_metadata
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse

def defaultView(request):
    return HttpResponse("hello")

@csrf_exempt
def metaView(request, encoded_database_connection_string):
    database_connection_string=urllib.parse.unquote(encoded_database_connection_string)
    try:
        response = extract_metadata(database_connection_string)
        return HttpResponse(response)
    except SQLAlchemyError as err:
        print("error")

    return HttpResponse(database_connection_string)