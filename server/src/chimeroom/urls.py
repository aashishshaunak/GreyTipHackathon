from django.conf.urls import include, url
from django.contrib import admin
from chimeroom.views import ChimeRoom, ChimeBooking

urlpatterns = [
    # Examples:
    # url(r'^$', 'chimeroom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'addroom/', ChimeRoom.as_view()),
    url(r'addbooking/', ChimeBooking.as_view()),
]
