from django.contrib import messages
from django.shortcuts import redirect
from django.urls import resolve

class RedirectUnauthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = ['index', 'login', 'signup']  # Views allowed without login

    def __call__(self, request):
        if not request.user.is_authenticated:
            current_url = resolve(request.path_info).url_name
            if current_url not in self.exempt_urls:
                # Add a message to inform the user that they must be logged in
                messages.info(request, 'You must be logged in to access this page.')
                return redirect('index')  # Send to homepage if not logged in
        return self.get_response(request)
