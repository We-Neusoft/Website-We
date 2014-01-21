from base64 import urlsafe_b64encode, urlsafe_b64decode
from uuid import UUID

def encode(uuid):
    return base64.urlsafe_b64encode(uuid.bytes.encode('base64')).rstrip('=')

def decode(string):
    return UUID(bytes=urlsafe_b64decode(string + '=='))
