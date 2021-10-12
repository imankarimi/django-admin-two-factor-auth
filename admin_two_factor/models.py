import base64
import os
from io import BytesIO

import pyotp
import qrcode
from admin_two_factor import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


class TwoFactorVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='two_step')
    secret = models.CharField(_('secret key'), max_length=20, null=True, blank=True, unique=True, editable=False)
    code = models.CharField(_('code'), max_length=8, null=True, blank=True,
                            help_text=_('You must enter the code here to active/deactivate two step verification.'))
    is_active = models.BooleanField(_('is active?'), default=False)

    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        verbose_name = _('two factor verification')
        verbose_name_plural = _('two factor verifications')

    def clean(self):
        if self.is_active and not self.secret and not self.code:
            raise ValidationError("The code field is required.")
        if not self.is_active and self.secret and not self.code:
            raise ValidationError("The code field is required.")

        if self.code:
            if self.is_active and not self.secret:
                secret = cache.get('user_secret_key_%s' % self.user.id)

                is_verify = self.is_verify(code=self.code, secret=secret)
                if not is_verify:
                    raise ValidationError("The code is wrong. please try again.")

                self.secret = secret

            elif not self.is_active and self.secret:
                is_verify = self.is_verify(code=self.code)
                if not is_verify:
                    raise ValidationError("The code is wrong. please try again.")
                self.secret = None

        self.code = None

    @property
    def get_qrcode(self):
        if self.secret or not self.user:
            return self.secret, None

        secret_key = base64.b32encode(os.urandom(10)).decode()
        username = self.user.get_full_name() if self.user.get_full_name() else self.user.username
        query = pyotp.totp.TOTP(secret_key).provisioning_uri(username,
                                                             issuer_name=settings.ADMIN_TWO_FACTOR_NAME)
        qr_img = qrcode.make(query)
        buffered = BytesIO()
        qr_img.save(buffered, format="JPEG")
        link = base64.b64encode(buffered.getvalue()).decode('UTF-8')

        cache.set('user_secret_key_%s' % self.user_id, secret_key, 300)

        return secret_key, link

    def is_verify(self, code, secret=None):
        secret = secret if secret else self.secret
        if secret:
            totp = pyotp.TOTP(secret)
            if code == totp.now():
                return True
        return False
