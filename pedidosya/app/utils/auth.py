from functools import wraps
from flask import request, abort

API_KEY = "grupopatito"

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("X-API-KEY")
        if key and key == API_KEY:
            return f(*args, **kwargs)
        abort(401, description="Unauthorized: Invalid or missing API key.")
    return decorated
