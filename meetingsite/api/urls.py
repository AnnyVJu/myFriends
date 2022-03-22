from django.urls import re_path, path, include
from django.views.decorators.csrf import csrf_exempt

from meetingsite.api.views import RegisterViewApi, LoginViewApi, GetProfileApi, LogoutViewApi, GetTimelineApi, GetCommentsApi

urlpatterns = [
    #path('accounts/', include('meetingsite.urls', namespace='meetingsite')),
    re_path(r'^accounts/register/$', csrf_exempt(RegisterViewApi.as_view())),
    re_path(r'^accounts/login/$', csrf_exempt(LoginViewApi.as_view())),
    re_path(r'^accounts/logout/$', csrf_exempt(LogoutViewApi.as_view())),
    re_path(r'^me/$', GetProfileApi.as_view()),
    re_path(r'^timeline/$', GetTimelineApi.as_view()),
    re_path(r'^posts/(?P<post_id>\d+)/comments/$', GetCommentsApi.as_view()),
]