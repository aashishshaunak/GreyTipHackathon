from datetime import date
from calendar import monthrange
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

print "here"
class ChimeRoom(APIView):
    print "In class"
    def post(self, request):
        print "just paste"
        return Response({"HI":"DER"})
