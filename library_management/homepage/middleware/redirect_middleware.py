from django.shortcuts import redirect
from django.urls import resolve

class RedirectUnauthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = ['index', 'login', 'signup']  # view names allowed without login

    def __call__(self, request):
        if not request.user.is_authenticated:
            current_url = resolve(request.path_info).url_name
            if current_url not in self.exempt_urls:
                return redirect('index')  # send to homepage
        return self.get_response(request)
