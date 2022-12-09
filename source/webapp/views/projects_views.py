from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Projects
from webapp.forms import ProjectForm


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


class ProjectCreateView(CreateView):
    template_name = 'projects/project_create.html'
    model = Projects
    form_class = ProjectForm

    def get_success_url(self):

        return reverse('project_view', kwargs={'pk': self.object.pk})

class ProjectUpdateView(UpdateView):
    model = Projects
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'projects'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class ProjectDeleteView(DeleteView):
    template_name = 'projects/project_delete.html'
    model = Projects
    context_object_name = 'projects'
    success_url = reverse_lazy('projects_list')


