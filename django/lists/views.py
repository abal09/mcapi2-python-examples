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
        lists = m.lists.list()
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        return redirect('/')

    return render_to_response('lists/index.html', {'lists':lists['data']}, context_instance=RequestContext(request))

def view(request, list_id):
    try:
        m = get_mailchimp_api()
        lists = m.lists.list({'list_id':list_id})
        list = lists['data'][0]
        members = m.lists.members(list_id)['data']
    except mailchimp.ListDoesNotExistError:
        messages.error(request,  "The list does not exist")
        return redirect('/lists')
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        return redirect('/lists')

    return render_to_response('lists/view.html', {'list':list, 'members':members}, context_instance=RequestContext(request))

def subscribe(request, list_id):
    try:
        m = get_mailchimp_api()
        m.lists.subscribe(list_id, {'email':request.POST['email']})
        messages.success(request,  "The email has been successfully subscribed")
    except mailchimp.ListAlreadySubscribedError:
        messages.error(request,  "That email is already subscribed to the list")
        return redirect('/lists/'+list_id)
    except mailchimp.Error, e:
        messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        return redirect('/lists/'+list_id)
    return redirect(reverse('lists.views.view', args=(list_id,)))
