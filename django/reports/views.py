# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib import messages

from mcapi_python_example.utils import get_mailchimp_api
import mailchimp

def index(request):
    try:
        m = get_mailchimp_api()
        campaigns = m.campaigns.list({'status':'sent'})
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        return redirect('/')
    return render_to_response('reports/index.html', {'campaigns':campaigns['data']}, context_instance=RequestContext(request))

def view(request, cid):
    try:
        m = get_mailchimp_api()
        campaigns = m.campaigns.list({'cid':cid})
        campaign = campaigns['data'][0]
        report = m.reports.summary(cid)
    except mailchimp.CampaignDoesNotExistError:
        messages.error(request,  "The campaign does not exist")
        return redirect('/reports')
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        return redirect('/reports')

    return render_to_response('reports/view.html', {'campaign':campaign, 'report':report}, context_instance=RequestContext(request))
