from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from werkzeug.security import generate_password_hash
from . import models


# Create your views here.

def user(request):
    users = models.User.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data)

