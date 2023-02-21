from django.shortcuts import render
from django.urls import reverse, resolvers
from django.http import HttpResponse, HttpResponseRedirect
from . import urls



def home(request):
    # patterns = urls.urlpatterns
    # url_list = []
    # for path in patterns:
    #     if isinstance(path, resolvers.URLPattern):
    #         url_list.append(path.name)
    #     elif isinstance(path, resolvers.URLResolver):
    #         url_list.append(path.url_patterns[0].name)
    #     else:
    #         pass
    # del url_list[1]
    return render(request, 'airline/home.html')