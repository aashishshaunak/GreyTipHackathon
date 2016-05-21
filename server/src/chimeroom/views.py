from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from models import chimeRoom


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
        data = []
        for project in projects:
            data = project.__dict__
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            project = chimeRoom.objects.get(name=request.data['conferenceName'])
        except chimeRoom.DoesNotExist:
            return Response(request.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        project.delete()
        return Response(request.data, status=status.HTTP_200_OK)

