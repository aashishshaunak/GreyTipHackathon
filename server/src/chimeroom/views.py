from datetime import date
from calendar import monthrange
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import chimeRoom, chimeBooking
from dateutil import parser

class ChimeRoom(APIView):
    def post(self, request):
        try:
            chime_room_obj = chimeRoom(capacity=request.data['capacity'][0],floor=request.data['floor'][0],
                                       name=request.data['name'][0],active=request.data['active'][0],white_board=request.data['white_board'][0],
                                       wi_fi=request.data['wi_fi'][0],projector=request.data['projector'][0],internet=request.data['internet'][0],
                                       intercom=request.data['intercom'][0],tele_conferencing=request.data['tele_conferencing'][0],
                                       video_conferencing=request.data['video_conferencing'][0], is_locked=request.data['is_locked'][0])
            chime_room_obj.save()
        except Exception as e:
            return Response({"error":"cannot save data with above data set"})
        return Response({"HI":"DER"})


class ChimeBooking(APIView):
    def post(self, request):
        meeting_st = parser.parse(request.data['meeting_starting'])
        meeting_end = parser.parse(request.data['meeting_ending'])
        try:
            chime_room_obj = chimeBooking(room_id=request.data['room_id'], meeting_starting=meeting_st,
                                       meeting_ending=meeting_end, active=request.data['active'],
                                       white_board=request.data['white_board'],
                                       wi_fi=request.data['wi_fi'], projector=request.data['projector'],
                                       internet=request.data['internet'],
                                       intercom=request.data['intercom'],
                                       tele_conferencing=request.data['tele_conferencing'],
                                       video_conferencing=request.data['video_conferencing'],user_capacity=request.data['user_capacity'],
                                       is_locked=request.data['is_locked'])
            chime_room_obj.save()
        except Exception as e:
            return Response({"error": "cannot save data with above data set"})
        return Response({"hello":"mister"})