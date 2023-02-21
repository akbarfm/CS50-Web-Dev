from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "simple/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Shimishimiya", "Shimiyay", "Shimiya"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")