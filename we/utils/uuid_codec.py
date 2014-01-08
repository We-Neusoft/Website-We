import uuid

def encode(UUID):
    return UUID.bytes.encode('base64').rstrip('=\n').replace('/', '_').replace('+', '-')

def decode(string):
    return uuid.UUID(bytes=(string + '==').replace('_', '/').replace('-', '+').decode('base64'))
