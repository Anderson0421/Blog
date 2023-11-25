from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Dashboard

def admin_only(function):
    def _wrapped(request, *args, **kwargs):  # Cambiado de user a request
        if request.user.has_perm('core.can_add_post_view'):
            return function(request, *args, **kwargs)
        else:
            return redirect('/')

    return _wrapped


class DashboardView(View):
    @method_decorator(login_required)
    @method_decorator(admin_only)
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/index.html', {})