from django.shortcuts import render , redirect , get_object_or_404 
from webapp.models import Doings , Status , Type , Projects
from webapp.forms import DoingForm , SimpleSearchForm
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, CreateView, DetailView
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
        context['doing'] = doings
        return context
class DoingCreateView(CreateView):
    template_name = 'doings/doings_create.html'
    model = Doings
    form_class = DoingForm

    def form_valid(self, form):
        task = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        form.instance.task = task
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('doing_view', kwargs={'pk': self.object.pk})
class DoingUpdateView(FormView):
    template_name = 'doings/update.html'
    form_class = DoingForm

    def dispatch(self, request, *args, **kwargs):
       self.doing = self.get_object()
       return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['doing'] = self.doing
       return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.doing
        return kwargs

    def form_valid(self, form):
       type = form.cleaned_data.pop('type')
       for key, value in form.cleaned_data.items():
           if value is not None:
               setattr(self.doing, key, value)
       self.doing.save()
       self.doing.type.set(type)
       return super().form_valid(form)

    def get_success_url(self):
       return reverse('doing_view', kwargs={'pk': self.doing.pk})

    def get_object(self):
       pk = self.kwargs.get('pk')
       return get_object_or_404(Doings, pk=pk)


class DoingDeleteView(TemplateView):
    def get(self,request, *args, **kwargs):
        doing = get_object_or_404(Doings, pk=kwargs['pk'])
        return render(request, 'doings/delete.html', context={'doing': doing})
    def post(self, request, *args, **kwargs):
        doing = get_object_or_404(Doings, pk=kwargs['pk'])
        doing.delete()
        return redirect('index')

