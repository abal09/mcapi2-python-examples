# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib import messages

from mcapi_python_example.utils import get_mailchimp_api
import mailchimp



def index(request):
    m = get_mailchimp_api()
    try:
        m.helper.ping()
    except mailchimp.Error:
        messages.error(request,  "Invalid API key")
    return render_to_response('home.html', {}, context_instance=RequestContext(request))
