from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from meetingsite.forms import RegisterForm, ProfileForm, PostForm
from meetingsite.models import Profile, Post, Comment


class HomeView(TemplateView):
    template_name = "home.html"
    timeline_template_name = "timeline.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect(reverse('home'))
        context = {
            'posts': Post.objects.all()
        }
        return render(request, self.timeline_template_name, context)


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                self.create_new_user(form)
                messages.success(request, "Successfully register")
                return redirect(reverse('login'))

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def create_new_user(self, form):
        email = None
        if 'email' in form.cleaned_data:
            email = form.cleaned_data['email']
        User.objects.create_user(form.cleaned_data['username'], email, form.cleaned_data['password'],
                                 first_name=form.cleaned_data['first_name'],
                                 last_name=form.cleaned_data['last_name'])


class LogoutView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class ProfileView(TemplateView):
    template_name = "registration/profile.html"

    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect(reverse('edit_profile'))
        context = {
            'selected_user': request.user
        }
        return render(request, self.template_name, context)


def get_profile(user):
    try:
        return user.profile
    except:
        return None


class EditProfileView(TemplateView):
    template_name = "registration/edit_profile.html"

    def dispatch(self, request, *args, **kwargs):
        form = ProfileForm(instance=get_profile(request.user))
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, "Profile updated!")
                return redirect(reverse('profile'))
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.profile
        except:
            return None


class PostCommentView(View):
    def dispatch(self, request, *args, **kwargs):
        post_id = request.GET.get("post_id")
        comment = request.GET.get("comment")
        if comment and post_id:
            post = Post.objects.get(pk=post_id)
            comment = Comment(text=comment, post=post, author=request.user)
            comment.save()
            return render(request, "blocks/comment.html", {'comment': comment})
        return HttpResponse(status=500, content="")


class ViewUserView(TemplateView):
    template_name = "registration/profile.html"

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        try:
            user = User.objects.get(username=username)
            return render(request, self.template_name, {'selected_user': user})
        except:
            return redirect("/")


class PostView(TemplateView):
    template_name = 'blocks/post.html'

    def dispatch(self, request, *args, **kwargs):
        try:
            post = Post.objects.get(id=kwargs['post_id'])
            return render(request, self.template_name, {'post': post})
        except:
            return redirect(reverse('home'))
