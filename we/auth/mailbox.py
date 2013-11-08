from django.contrib.auth.models import User

from imaplib import IMAP4

ALLOWED_DOMAIN = ['nou.com.cn', 'neusoft.edu.cn']

class MailboxAuth(object):
    def authenticate(self, username=None, domain=None, password=None):
        if not domain.lower() in ALLOWED_DOMAIN:
            return None

        try:
            mailbox = IMAP4('mail.' + domain)
            mailbox.login(username + '@' + domain, password)

            try:
                user = User.objects.get(username=username + '@' + domain)
            except User.DoesNotExist:
                user = User(username=username + '@' + domain, email=username + '@' + domain)
                user.save()

            return user
        except:
            return None

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
