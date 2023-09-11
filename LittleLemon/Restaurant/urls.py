from django.urls import include, re_path


urlpatterns = [
    re_path(r'^api/v1/', include('booking.urls')),
    re_path(r'^api/v1/', include('menu.urls')),
]
