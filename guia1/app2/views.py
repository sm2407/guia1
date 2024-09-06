from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html = """
    <h1> Mi loco, ta complica esta vaina </h1>
    &copy; derechos reservados"""
    return HttpResponse(html)

def hola(request):
    html = """
    <h1> Mi estimado, confirmo con su afirmacion anterior :) </h1>
    <p> Atte su colaborador &copy; </p>"""
    return HttpResponse(html)