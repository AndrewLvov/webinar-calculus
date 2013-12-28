# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', {})

def count(request):
    x = ''
    y = ''
    result = 0
    if request.POST:
        try:
            x = unicode(request.POST['x'])
            # y = int(raw_input())
            y = unicode(request.POST['y'])
        except (ValueError, KeyError):
            result = 'error'
        else:
            result = u"{} and {} пошли гулять".format(x, y)

    context = {
        'x': x,
        'y': y,
        'result': result,
    }
    return render_to_response('count.html', context,
        context_instance=RequestContext(request))