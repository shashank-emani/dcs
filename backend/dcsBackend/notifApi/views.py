from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import SMSNotification
from datetime import datetime

class SendSMSView(View):
    def post(self, request):
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        if not phone_number or not message:
            return JsonResponse({'error': 'Phone number and message are required'}, status=400)

        sms = SMSNotification.objects.create(phone_number=phone_number, message=message)
        
        try:
            sms.status = "Sent"
            sms.sent_at = datetime.now()
            sms.save()
            return JsonResponse({'success': f'SMS sent to {phone_number}'}, status=200)
        except Exception as e:
            sms.status = "Failed"
            sms.save()
            return JsonResponse({'error': f'Failed to send SMS: {str(e)}'}, status=500)

