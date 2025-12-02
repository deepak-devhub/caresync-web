"""
Custom middleware for security and caching control
"""
from django.utils.deprecation import MiddlewareMixin


class NoCacheMiddleware(MiddlewareMixin):
    """
    Middleware to prevent caching of authenticated pages.
    This ensures users can't access protected pages via browser back button after logout.
    """

    def process_response(self, request, response):
        # Check if user has an active session (is logged in)
        if 'lid' in request.session and request.session['lid']:
            # Add cache control headers for authenticated users
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'

        return response
