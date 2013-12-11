from django.contrib.auth.models import User

from imaplib import IMAP4

ALLOWED_DOMAIN = ['nou.com.cn', 'neusoft.edu.cn']

class MailboxAuth(object):
    def authenticate(self, email=None, password=None):
        if not email.count('@') == 1:
            return None

        email = email.lower()
        if not email.split('@')[1] in ALLOWED_DOMAIN:
            return None

        try:
            mailbox = IMAP4('mail.' + domain)
            mailbox.login(email, password)

            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                user = User(username=email, email=email)
                user.save()

            return user
        except:
            return None

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
