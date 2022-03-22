from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

from meetingsite.api.auth import JsonView, AuthView
from meetingsite.forms import RegisterForm
from meetingsite.models import Post
from meetingsite.serializers import UserSerializer, PostSerializer, CommentSerializer


class RegisterViewApi(JsonView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                if User.objects.filter(email=email).exists():
                    return self.json_error('User with such email already exists', "duplicate_email")
                try:
                    User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
                    user = User.objects.get(email=email)
                    serializer = UserSerializer(user)
                    return self.json_success(serializer.data)

                except IntegrityError:
                    return self.json_error('User with such username already exists', "duplicate_username")
            else:
                return self.json_error("Form filled incorrectly", "form_error")
        else:
            return self.json_error('Auth failed', "only_post_allowed")


class LoginViewApi(JsonView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            email = self.request.POST.get('email')
            password = self.request.POST.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                serializer = UserSerializer(user)
                return self.json_success(serializer.data)
            else:
                return self.json_error('Credentials is wrong', "login_incorrect")
        else:
            return self.json_error('Auth failed', "only_post_allowed")


class LogoutViewApi(AuthView):
    def handle(self, request, *args, **kwargs):
        if request.method == 'POST':
            logout(request)
            return self.json_success('Logged out successfully')


class GetProfileApi(AuthView):
    def handle(self, request, *args, **kwargs):
        serialized_user = UserSerializer(request.user)
        return self.json_success(serialized_user.data)


class GetTimelineApi(AuthView):
    def handle(self, request, *args, **kwargs):
        posts = PostSerializer(Post.objects.all(), many=True)
        return self.json_success(posts.data)


class GetCommentsApi(AuthView):
    def handle(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['post_id'])
        comments = CommentSerializer(post.comments.all(), many=True)
        return self.json_success(comments.data)


