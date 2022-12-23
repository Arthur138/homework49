from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects
from webapp.forms import ProjectForm , UserInProjectForm


class ProjectView(ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    model = Projects

class ProjectDetailView(DetailView):
    template_name = 'projects/project_detailview.html'
    model = Projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = self.object
        doings = projects.doings.order_by('-create')
        context['doings'] = doings
        return context



class ProjectCreateView(PermissionRequiredMixin , CreateView):
    template_name = 'projects/project_create.html'
    model = Projects
    form_class = ProjectForm
    permission_required = 'webapp.add_projects'

    def has_permission(self):
        return super().has_permission()


    def get_success_url(self):

        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

class ProjectUpdateView(PermissionRequiredMixin , UpdateView):
    model = Projects
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'projects'
    permission_required = 'webapp.change_projects'

    def has_permission(self):
        return super().has_permission()

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

class ProjectDeleteView(PermissionRequiredMixin,DeleteView):
    template_name = 'projects/project_delete.html'
    model = Projects
    context_object_name = 'projects'
    success_url = reverse_lazy('webapp:projects_list')
    permission_required = 'webapp.delete_projects'

    def has_permission(self):
        return super().has_permission()

class AddUserInProject(PermissionRequiredMixin,UpdateView):
    template_name = 'projects/add_users_in_project.html'
    model = Projects
    form_class = UserInProjectForm
    context_object_name = 'project'
    permission_required = 'webapp.can_add_users'

    def has_permission(self):
        return super().has_permission() or Projects.users == self.request.user

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        users = form.cleaned_data.get("users")
        for user in users:
            project.users.add(user)
        return redirect('webapp:project_view',pk=self.kwargs.get('pk'))
    def get_success_url(self):
        return reverse('webapp:index')

class DeleteUserInProject(PermissionRequiredMixin,CreateView):
    template_name = 'projects/delete_users_project.html'
    model = Projects
    form_class = UserInProjectForm
    context_object_name = 'project'
    permission_required = 'webapp.can_delete_users'

    def has_permission(self):
        return super().has_permission() or Projects.users == self.request.user


    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        users = form.cleaned_data.get("users")
        for user in users:
            project.users.remove(user)
        return redirect('webapp:project_view',pk=self.kwargs.get('pk'))
    def get_success_url(self):
        return reverse('webapp:index')