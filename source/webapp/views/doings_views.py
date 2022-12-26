from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from webapp.models import Doings , Status , Type , Projects
from webapp.forms import DoingForm , SimpleSearchForm
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):
    template_name = 'doings/index.html'
    context_object_name = 'doings'
    model = Doings
    ordering = ['-create']
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
         context['query'] = urlencode({'search': self.search_value})
         context['search'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)
        
    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

class DoingView(DetailView):
    template_name = 'doings/doings_view.html'
    model = Doings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doings = self.object
        context['doings'] = doings
        return context
class DoingCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'doings/doings_create.html'
    model = Doings
    form_class = DoingForm
    permission_required = 'webapp.add_doings'

    def has_permission(self):
        return super().has_permission() or Projects.users == self.request.user


    def form_valid(self, form):
        task = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        form.instance.task = task
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('webapp:doing_view', kwargs={'pk': self.object.pk})

class DoingUpdateView(PermissionRequiredMixin, UpdateView):
    model = Doings
    template_name = 'doings/update.html'
    form_class = DoingForm
    context_object_name = 'doing'
    permission_required = 'webapp.change_doings'

    def has_permission(self):
        return super().has_permission() or Projects.users == self.request.user

    def get_success_url(self):
        return reverse('webapp:doing_view', kwargs={'pk': self.object.pk})

class DoingDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'doings/delete.html'
    model = Doings
    context_object_name = 'doing'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_doings'

    def has_permission(self):
        return super().has_permission() or Projects.users == self.request.user

