from django.contrib import admin, messages
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from admin_two_factor.models import TwoFactorVerification
from admin_two_factor.utils import set_expire


@admin.register(TwoFactorVerification)
class TwoStepVerificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'created_time']
    raw_id_fields = ['user']
    list_filter = ['is_active', 'created_time']
    fieldsets = (("", {'fields': ('user', 'code', 'is_active', 'qrcode'), }),)
    readonly_fields = ['qrcode']

    def qrcode(self, obj):
        secret_key, qrcode = obj.get_qrcode
        if qrcode:
            return render_to_string('two_step_verification/admin/qrcode.html', {'qrcode': qrcode})

    qrcode.short_description = _('Two Step QR Code')

    def get_fieldsets(self, request, obj=None):
        fieldsets = self.fieldsets
        if not obj:
            fieldsets = (("", {'fields': ('user',), }),)
        elif obj and obj.secret:
            fieldsets = (("", {'fields': ('user', 'code', 'is_active'), }),)
        return fieldsets

    def response_add(self, request, obj, post_url_continue=None):
        self.message_user(request, _('user added successfully'), level=messages.SUCCESS)
        return redirect('admin:admin_two_factor_twofactorverification_change', obj.id)

    def response_change(self, request, obj):
        request.session['two_step_%s' % request.user.id] = {'expire': set_expire().get('time')}
        return super(TwoStepVerificationAdmin, self).response_change(request, obj)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if not self.get_object(request, object_id):
            extra_context['show_save_and_add_another'] = False
        return super(TwoStepVerificationAdmin, self).changeform_view(request, object_id, form_url, extra_context)
