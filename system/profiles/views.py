from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profile_view(request,username=None, *args, **kwargs):
    user_reqst = request.user
    user_object = get_object_or_404(User, username=username)
    is_me = user_object == user_reqst
    return HttpResponse(f"hello dude, you are loged as {username} - {user_object.id} - {                                                        }")