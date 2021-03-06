from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import mail_admins
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def csp_report(request):
    mail_admins('CSP Report', request.body.decode('utf-8'))
    return HttpResponse()
