from django.test import TestCase, override_settings
from django.shortcuts import reverse
from django.core import mail

import json

class CspReportTests(TestCase):
    @override_settings(ADMINS=[('admin', 'admin@example.com')])
    def test_report(self):
        payload = json.dumps("hey")
        url = reverse('hardening:csp-report')
        self.client.post(url, payload, content_type="application/json")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ['admin@example.com'])
        self.assertEqual(mail.outbox[0].body, payload)
