from django.test import TestCase
from django.urls import reverse
from .models import SMSNotification

class SendSMSViewTest(TestCase):

    def test_send_sms_success(self):
        data = {
            'phone_number': '8788988583',
            'message': 'Test message'
        }
        response = self.client.post(reverse('send_sms'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertEqual(SMSNotification.objects.count(), 1)

    def test_send_sms_missing_data(self):
        data = {
            'phone_number': '',
            'message': 'Test message'
        }
        response = self.client.post(reverse('send_sms'), data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
