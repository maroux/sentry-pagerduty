# coding: utf-8
"""
sentry_statsd.forms
"""
from django import forms


class PagerDutyConfigForm(forms.Form):
    api_key = forms.CharField(
        max_length=255,
        help_text='PagerDuty API KEY'
    )

    service_key = forms.CharField(
        max_length=32,
        help_text="PagerDuty's Sentry service Integration Key"
    )

    domain_name = forms.CharField(
        max_length=255,
        help_text="Domain Name of your PagerDuty instance (e.g. 'sterling-cooper')"
    )
