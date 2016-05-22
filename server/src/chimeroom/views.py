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
            chime_room_obj = chimeRoom(capacity=request.data['numberOfSeats'],floor=request.data['floorValue'],
                                       name=request.data['conferenceName'],active=True,
                                       white_board=request.data['ameneties']['whiteboard'],
                                       wi_fi=request.data['ameneties']['wifi'],
                                       projector=request.data['ameneties']['projector'],
                                       internet=request.data['ameneties']['internet'],
                                       intercom=request.data['ameneties']['intercom'],
                                       tele_conferencing=request.data['ameneties']['teleconferencing'],
                                       video_conferencing=request.data['ameneties']['videoconferencing'])
            chime_room_obj.save()
        except Exception as e:
            return Response({"error":"cannot save data with above data set"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(request.data, status=status.HTTP_200_OK)



class RoomView(APIView):

    def get(self,request):
        projects = chimeRoom.objects.filter(active=True)
        all_data = list()
        for project in projects:
            print project.__dict__
            data = dict()
            data['ameneties'] = []
            data['name'] = project.name
            data['capacity'] = project.capacity
            data['floor'] = project.floor
            data['is_locked'] = project.is_locked
            if project.intercom:
                data['ameneties'].append('intercom')
            if project.wi_fi:
                data['ameneties'].append('wi_fi')
            if project.video_conferencing:
                data['ameneties'].append('video_conferencing')
            if project.white_board:
                data['ameneties'].append('white_board')
            if project.tele_conferencing:
                data['ameneties'].append('tele_conferencing')
            if project.internet:
                data['ameneties'].append('internet')
            if project.projector:
                data['ameneties'].append('projector')
            all_data.append(data)
        return Response(all_data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            project = chimeRoom.objects.get(name=request.data['conferenceName'])
        except chimeRoom.DoesNotExist:
            return Response(request.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        project.delete()
        return Response(request.data, status=status.HTTP_200_OK)

class EditView(APIView):
    def get(self,request):
        # import pdb;
        # pdb.set_trace()
        request.data[0]['name']
        projects = chimeRoom.objects.filter(name='gabbar')
        all_data = list()
        for project in projects:
            print project.__dict__
            data = dict()
            data['ameneties'] = []
            data['name'] = project.name
            data['capacity'] = project.capacity
            data['floor'] = project.floor
            data['is_locked'] = project.is_locked
            if project.intercom:
                data['ameneties'].append('intercom')
            if project.wi_fi:
                data['ameneties'].append('wi_fi')
            if project.video_conferencing:
                data['ameneties'].append('video_conferencing')
            if project.white_board:
                data['ameneties'].append('white_board')
            if project.tele_conferencing:
                data['ameneties'].append('tele_conferencing')
            if project.internet:
                data['ameneties'].append('internet')
            if project.projector:
                data['ameneties'].append('projector')
            all_data.append(data)
        return Response(all_data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            project = chimeRoom.objects.get(name=request.data['conferenceName'])
        except chimeRoom.DoesNotExist:
            return Response(request.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        project.delete()
        return Response(request.data, status=status.HTTP_200_OK)

class ChimeBooking(APIView):
    def post(self, request):
        meeting_st = parser.parse(request.data['meeting_starting'])
        meeting_end = parser.parse(request.data['meeting_ending'])
        amenities = ['white_board','wi_fi','projector', 'internet', 'intercom', 'tele_conferencing', 'video_conferencing']
        requested_amenities = []
        for facility in amenities:
            if request.data[facility]:
                requested_amenities.append(facility)
        try:
            feasible_room_obj = chimeRoom.objects.filter(capacity__gte=request.data['user_capacity'],facility__in=True)
            room_id_list = []
            for rooms in feasible_room_obj:
                room_id_list.append(rooms.id)
            room_id_list.sort()
            get_chime_obj = chimeBooking.filter.get(room_id__in=room_id_list, meeting_starting__lte=meeting_st, meeting_ending__lte=meeting_end)
            if get_chime_obj:
                chime_room_obj = chimeBooking(room_id=None, meeting_starting=meeting_st,
                                           meeting_ending=meeting_end, active=request.data['active'],
                                           white_board=request.data['white_board'],
                                           wi_fi=request.data['wi_fi'], projector=request.data['projector'],
                                           internet=request.data['internet'],
                                           intercom=request.data['intercom'],
                                           tele_conferencing=request.data['tele_conferencing'],
                                           video_conferencing=request.data['video_conferencing'],user_capacity=request.data['user_capacity'],
                                           is_locked=False)
            else:
                chime_room_obj = chimeBooking(room_id=get_chime_obj.id, meeting_starting=meeting_st,
                                              meeting_ending=meeting_end, active=request.data['active'],
                                              white_board=request.data['white_board'],
                                              wi_fi=request.data['wi_fi'], projector=request.data['projector'],
                                              internet=request.data['internet'],
                                              intercom=request.data['intercom'],
                                              tele_conferencing=request.data['tele_conferencing'],
                                              video_conferencing=request.data['video_conferencing'],
                                              user_capacity=request.data['user_capacity'],
                                              is_locked=True)
            chime_room_obj.save()
        except Exception as e:
            return Response({"error": "cannot save data with above data set"})
        return Response({"hello":"mister"})
