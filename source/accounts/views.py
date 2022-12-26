from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from accounts.forms import MyUserCreationForm
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.views.generic.list import MultipleObjectMixin, ListView
from django.core.paginator import Paginator

class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url

class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        projects = self.get_object().projects.all()
        return super().get_context_data(object_list=projects, **kwargs)

class UsersList(PermissionRequiredMixin , ListView):
    model = get_user_model()
    template_name = 'users_list.html'
    context_object_name = 'user_obj'
    permission_required = 'accounts.can_see_users'

    def has_permission(self):
        return super().has_permission()