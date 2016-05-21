from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from chimeroom.views import ChimeRoom, ChimeBooking
=======
from chimeroom.views import ChimeRoom
from rest_framework import routers
router = routers.SimpleRouter()
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'addroom/', ChimeRoom.as_view())
# ]
>>>>>>> 41633ccb26f7794f2e07e2bc0380034a0dc599dd


<<<<<<< HEAD
    url(r'^admin/', include(admin.site.urls)),
    url(r'addroom/', ChimeRoom.as_view()),
    url(r'addbooking/', ChimeBooking.as_view()),
=======
urlpatterns = [
    url(r'^addroom$', ChimeRoom.as_view()),
    url(r'^', include(router.urls)),
>>>>>>> 41633ccb26f7794f2e07e2bc0380034a0dc599dd
]
