from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    """
    主页
    :param request:
    :return:
    """
    return render(request,'home/home.html')
