from unittest.mock import patch

from django.test import TestCase
from django.test import override_settings
from django.conf import settings

from hardening.checks import check_axes_config, check_csp_config

class MockGetDistributionResponse:
    def __init__(self, version):
        self.version = version

class BaseTestCase(TestCase):
    def assert_has_error(self, errors, error_id):
        error_ids = [e.id for e in errors]
        self.assertTrue(error_id in error_ids, 'Excepted to find "{0}", but got "{1}" instead'.format(error_id, ','.join(error_ids)))

class AxesTests(BaseTestCase):
    @patch('pkg_resources.get_distribution')
    def test_checks_version(self, mock_get_distribution):
        mock_get_distribution.return_value = MockGetDistributionResponse('5.4.2')
        self.assert_has_error(check_axes_config(None), 'hardening.E004')

    @override_settings(INSTALLED_APPS=[])
    def test_throws_errors_when_not_installed(self):
        self.assert_has_error(check_axes_config(None), 'hardening.E001')

    @override_settings(INSTALLED_APPS=['axes'])
    def test_no_error_when_access_installed(self):
        errors = check_axes_config(None)
        self.assertEqual(0, len(errors), errors)

    @override_settings(INSTALLED_APPS=['axes'], AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend'])
    def test_authentication_backend_contains_axes(self):
        self.assert_has_error(check_axes_config(None), 'hardening.E002')

    @override_settings(INSTALLED_APPS=['axes'], MIDDLEWARE=[])
    def test_checks_middleware(self):
        self.assert_has_error(check_axes_config(None), 'hardening.E003')

class CspTests(BaseTestCase):
    @patch('pkg_resources.get_distribution')
    def test_checks_version(self, mock_get_distribution):
        mock_get_distribution.return_value = MockGetDistributionResponse('3.5')
        self.assert_has_error(check_csp_config(None), 'hardening.E005')

    @override_settings(INSTALLED_APPS=['csp'], MIDDLEWARE=[])
    def test_checks_middleware(self):
        self.assert_has_error(check_csp_config(None), 'hardening.E006')

    @override_settings(INSTALLED_APPS=['csp'], CSP_REPORT_URI='xyz')
    def test_checks_csp_report_url(self):
        self.assert_has_error(check_csp_config(None), 'hardening.E018')

    @override_settings(INSTALLED_APPS=['csp'], CSP_REPORT_TO='xyz')
    def test_checks_csp_report_to(self):
        self.assert_has_error(check_csp_config(None), 'hardening.E019')
