from os import close
from django.http import HttpResponse
from django.shortcuts import render

import datetime

def main(request):

    date = datetime.datetime.now()
    dic = {"fecha":date}

    return render(request,"index.html",dic)