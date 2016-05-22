from django.conf.urls import include, url
from django.contrib import admin
from chimeroom.views import ChimeRoom,RoomView,ChimeBooking,EditView
from rest_framework import routers
router = routers.SimpleRouter()
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'addroom/', ChimeRoom.as_view())
# ]


urlpatterns = [
    url(r'^addroom$', ChimeRoom.as_view()),
    url(r'^viewrooms$', RoomView.as_view()),
    url(r'addbooking/', ChimeBooking.as_view()),
    url(r'^editroom$', EditView.as_view()),
    url(r'^', include(router.urls)),
]
