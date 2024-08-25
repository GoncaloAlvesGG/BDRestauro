from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class CheckSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs that can be accessed without session check
        exempt_urls = [
            reverse('login'),  # Replace 'login' with your login URL name
            reverse('register'), # If you have a signup page
            reverse('index'),
            reverse('login_user')
        ]

        # Check if the user is logged in by checking the session
        if not request.session.get('id_utilizador') and request.path not in exempt_urls:
            messages.error(request, 'Autentique-se primeiro para aceder a essa página!')
            return redirect('login')  # Redirect to login page

        response = self.get_response(request)
        return response