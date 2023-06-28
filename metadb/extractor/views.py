from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from extractor.extract import extract_metadata
from sqlalchemy.exc import SQLAlchemyError
import urllib.parse

def defaultView(request):
    errResp="Please make sure to attach a properly formated postgres conntection string, that has then been url encoded."
    sampleResp="Something like: postgresql%3A%2F%2FUSERNAME%3APASSWORD%40localhost%3A5432%2FDBNAME%3Fsslmode%3Ddisable "
    alchemy_docs="https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases\n"
    return HttpResponse(errResp+" Please fine more info at:"+alchemy_docs)

@csrf_exempt
def metaView(request, encoded_database_connection_string):
    database_connection_string=urllib.parse.unquote(encoded_database_connection_string)
    try:
        response = extract_metadata(database_connection_string)
        return JsonResponse(response, safe=False)
    except SQLAlchemyError as err:
        #error = ("error extracting metadata: ", err.__cause__)
        errResp="Please make sure to attach a properly formated postgres conntection string, that has then been url encoded."
        sampleResp="Something like: postgresql%3A%2F%2FUSERNAME%3APASSWORD%40localhost%3A5432%2FDBNAME%3Fsslmode%3Ddisable "
        alchemy_docs="https://docs.sqlalchemy.org/en/13/core/engines.html#supported-databases\n"
        return HttpResponse(errResp+" Please fine more info at:"+alchemy_docs)