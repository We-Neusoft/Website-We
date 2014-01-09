from django.contrib import admin

from api.oauth.models import AuthorizationCode, Client, RedirectionUri, AccessToken

class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'encoded_client_secret', 'admin')

    def encoded_client_secret(self, obj):
        return obj.client_secret.encode()
admin.site.register(Client, ClientAdmin)

class RedirectionUriAdmin(admin.ModelAdmin):
    list_display = ('client', 'redirect_uri')
admin.site.register(RedirectionUri, RedirectionUriAdmin)

class AuthorizationCodeAdmin(admin.ModelAdmin):
    list_display = ('client', 'user', 'encoded_code', 'redirect_uri', 'expire_time')

    def encoded_code(self, obj):
        return obj.code.encode()
admin.site.register(AuthorizationCode, AuthorizationCodeAdmin)

class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('client', 'user', 'encoded_code', 'encoded_token', 'expire_time')

    def encoded_code(self, obj):
        return obj.code.encode()

    def encoded_token(self, obj):
        return obj.token.encode()
admin.site.register(AccessToken, AccessTokenAdmin)
