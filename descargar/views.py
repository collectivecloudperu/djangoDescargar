from django.shortcuts import render

from django.http.response import HttpResponse
import mimetypes
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def descargar_archivo(request): 

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

    filename = 'mi_archivo.txt'

    filepath = BASE_DIR + '/descargar/archivos/' + filename 

    path = open(filepath, 'r') 

    mime_type, _ = mimetypes.guess_type(filepath)
    
    response = HttpResponse(path, content_type = mime_type)

    response['Content-Disposition'] = f"attachment; filename={filename}"

    return response 