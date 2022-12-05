from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
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
