from django.shortcuts import render
from .forms import *
import requests
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django_q.tasks import async_task, result, Schedule
from datetime import datetime
from decouple import config


def index(request):
    return render(request, 'monitoring/index.html', {})


def make_request(request):
    if request.POST:
        form = MakeRequestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            link = cd['link']
            user = User.objects.filter(id=int(cd['user'])).first()
            account = Account.objects.filter(user=user).first()
            try:
                # async_task(make_resp, link, hook=pt)
                # print(result(task))
                ##resp = requests.get(link)
                # if resp.status_code != 200:
                #     print(resp.json())
                # print(resp.json())
                # print(resp.history)
                # print(resp.url)
                ## link = Link.objects.create(link=link, account=account, response=resp.status_code, finish_link=resp.url)
                ## try:
                ##     link.resp_text = resp.json()
                ## except Exception:
                ##     pass
                # if resp.json():
                #     link.resp_text = resp.json()
                ## link.save()
                link_obj = Link.objects.create()
                link_obj.save()
                async_task(make_resp, link, link_obj.id, account.id)
            except Exception as e:
                print(e)
            # print(resp.status_code)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def make_resp(link, link_id, account_id):
    link_obj = Link.objects.get(id=int(link_id))
    account = Account.objects.get(id=int(account_id))
    resp = requests.get(link)
    link_obj.account = account
    link_obj.name = link
    link_obj.link = link
    link_obj.response = resp.status_code
    link_obj.finish_link = resp.url
    now = datetime.now()
    link_obj.last_check_time = now
    next_run = datetime(now.year, now.month, now.day, now.hour, now.minute+1, now.second)
    if resp.status_code != 200:
        link_obj.status = 'error'
        if 'error' in resp.json():
            link_obj.error = resp.json()['error']
    else:
        link_obj.status = 'ok'
    link_obj.save()
    if not link_obj.in_schedule:
        Schedule.objects.create(func='make_resp',
                                args='{}, {}, {}'.format(link, link_id, account_id),
                                schedule_type=Schedule.MINUTES,
                                minutes=config('MINUTES_FOR_TASK'),
                                repeats=-1,
                                next_run=next_run)
    link_obj.in_schedule = True
    try:
        link_obj.resp_text = resp.json()
    except Exception:
        pass




# def pt(task):
#     print('hook: ', task.result)
#
#
# def make_resp(link):
#     resp = requests.get(link)
#     print(resp)
#     return resp

# task = async_task(make_request)
