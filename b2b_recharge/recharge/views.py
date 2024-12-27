from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PhoneNumber

import logging

logger = logging.getLogger(__name__)


class RechargeAPI(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        amount = request.data.get('amount')
        try:
            phone = PhoneNumber.objects.get(number=phone_number)
            transaction = phone.recharge(amount)
            logger.info(f"Recharge successful for phone number {phone_number} with amount {amount}")
            return Response({'message': 'Phone recharged successfully', 'transaction_id': transaction.id}, status=status.HTTP_200_OK)
        except PhoneNumber.DoesNotExist:
            logger.error(f"Phone number {phone_number} not found")
            return Response({'error': 'Phone number not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            logger.error(f"Error recharging phone number {phone_number}: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)