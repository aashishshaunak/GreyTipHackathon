from datetime import date
from calendar import monthrange
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import chimeRoom
class ChimeRoom(APIView):
    def post(self, request):
        try:
            chime_room_obj = chimeRoom(capacity=request.data['capacity'][0],floor=request.data['floor'][0],
                                       name=request.data['name'][0],active=request.data['active'][0],white_board=request.data['white_board'][0],
                                       wi_fi=request.data['wi_fi'][0],projector=request.data['projector'][0],internet=request.data['internet'][0],
                                       intercom=request.data['intercom'][0],tele_conferencing=request.data['tele_conferencing'][0],video_conferencing=request.data['video_conferencing'][0])
            chime_room_obj.save()
        except Exception as e:
            return Response({"error":"cannot save data with above data set"})
        return Response({"HI":"DER"})
