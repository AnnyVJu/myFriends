"""meetingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.urls import re_path

from meetingsite import settings, views
from meetingsite.views import HomeView, LogoutView, RegisterView, ProfileView, EditProfileView, PostCommentView, \
    ViewUserView, PostView

app_name = 'meetingsite'
urlpatterns = [
                  # path('accounts/', include('meetingsite.urls', namespace='meetingsite')),
                  path('', HomeView.as_view(), name='home'),
                  path('accounts/login/', LoginView.as_view(), name='login'),
                  path('accounts/logout/', LogoutView.as_view(), name='logout'),
                  path('accounts/register/', RegisterView.as_view(), name='register'),
                  path('accounts/profile/', ProfileView.as_view(), name='profile'),
                  path('accounts/profile/edit/', EditProfileView.as_view(), name='edit_profile'),

                  # path('accounts/register', RegisterView.as_view(template_name='registration/register.html')),
                  # path('accounts/profile', ProfileView.as_view(template_name='registration/profile.html')),
                  # path('accounts/profile/edit', EditProfileView.as_view(template_name='registration/edit_profile.html')),

                  #  path('accounts/login/', login, name="login"),
                  #   path('accounts/logout/', LogoutView.as_view(), name="logout"),
                  #  path('accounts/register/', RegisterView.as_view(), name="register"),
                  #  path('accounts/profile/', ProfileView.as_view(), name="profile"),

                  # path('accounts/profile/edit/', EditProfileView.as_view(), name="edit_profile"),

                  # path('post-comment/', PostCommentView.as_view()),
                  # re_path('^post-view/(?P<post_id>\d+)/$', PostView.as_view(), name="post_view"),
                  # re_path('^user/@(?P<username>[-\w\s\d]+)$', ViewUserView.as_view(), name="view_user"),

                  # path('api/', include("meetingsite.api.urls")),

                  # re_path(r'^$', HomeView.as_view(), name="home"),

                  # re_path(r'^accounts/login/$', login, name="login"),
                  # re_path(r'^accounts/logout/$', LogoutView.as_view(), name="logout"),
                  # re_path(r'^accounts/register/$', RegisterView.as_view(), name="register"),
                  # re_path(r'^accounts/profile/$', ProfileView.as_view(), name="profile"),

                  # re_path(r'^accounts/profile/edit/$', EditProfileView.as_view(), name="edit_profile"),

                  re_path(r'^post-comment/$', PostCommentView.as_view()),
                  re_path(r'^post-view/(?P<post_id>\d+)/$', PostView.as_view(), name="post_view"),
                  re_path(r'^user/@(?P<username>[-\w\s\d]+)$', ViewUserView.as_view(), name="view_user"),
                  re_path(r'^admin/', admin.site.urls),
                  re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  re_path(r'^api-auth/', include('meetingsite.api.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
