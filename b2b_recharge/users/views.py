from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Seller, CreditRequest

import logging

logger = logging.getLogger(__name__)


class IncreaseCreditAPI(APIView):
    def post(self, request, seller_id):
        seller = Seller.objects.get(id=seller_id)
        amount = request.data.get("amount")
        try:
            credit_request = CreditRequest.objects.create(seller=seller, amount=amount)
            logger.info(f"Credit request created for seller {seller_id} with amount {amount}")
            return Response(
                {"message": "Credit request created successfully", "request_id": credit_request.id},
                status=status.HTTP_200_OK
            )
        except ValueError as e:
            logger.error(f"Error creating credit request for seller {seller_id}: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)