from django.utils.deprecation import MiddlewareMixin


class DisableCSRFOnAPI(MiddlewareMixin):
    """
    Disable CSRF for API calls.
    """
    def process_request(self, request):
        if (request.path.startswith('/api/')
            or request.path.startswith('/auth/')
            or request.path.startswith('/admin/')
            or request.path.startswith('/swagger/')
            or request.path.startswith('/redoc/')
            or request.path.startswith('/openapi/')
            or request.path.startswith('/favicon.ico')
            or request.path.startswith('/register/')
            or request.path.startswith('/verify_otp/')
            or request.path.startswith('/complete_registration/')

        ):
            setattr(request, '_dont_enforce_csrf_checks', True)
