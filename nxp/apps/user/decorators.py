from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def login_validate(view_func):
    def _check_user(request, *args, **kwargs):
        if not request.user.is_anonymous:
            if request.user.is_superuser or request.user.type == 'tim7':
                return view_func(request, *args, **kwargs)
            messages.info(request, 'Please login as a TIM7 or Admin')
        return redirect(reverse('backoffice:login'))
    return wraps(view_func)(_check_user)