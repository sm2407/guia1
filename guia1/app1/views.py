from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexApp1(request):
    html="""
    <h1>Index de app1</h1>
    <p>Parrafo</p>
    
    
    """
    return HttpResponse(html)

def vista1(request):
    html="""
    
    <h1>Titulo</h1>
    <h3>subtitulo</h3>
    
    
    """

    return HttpResponse(html)