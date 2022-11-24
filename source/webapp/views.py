from django.shortcuts import render , redirect , get_object_or_404 
from webapp.models import Doings , Status , Type
from webapp.forms import DoingForm
from django.urls import reverse
from django.views.generic import View , TemplateView ,FormView
# Create your views here.


class IndexView(TemplateView):
    def get(self, request ,*args, **kwargs):
        doings = Doings.objects.all()
        context = {
            'doings': doings
        }
        return render(request, 'index.html', context)

class DoingView(TemplateView):
   template_name = 'doings_view.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['doing'] = get_object_or_404(Doings, pk=kwargs['pk'])
       return context

class DoingCreate(FormView):
    template_name = "doings_create.html"
    form_class = DoingForm

    def form_valid(self, form):
       self.doing = form.save()
       return super().form_valid(form)

    def get_success_url(self):
       return reverse('doing_view', kwargs={'pk': self.doing.pk})

class DoingUpdateView(FormView):
    template_name = 'update.html'
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
        return render(request, 'delete.html', context={'doing': doing})
    def post(self, request, *args, **kwargs):
        doing = get_object_or_404(Doings, pk=kwargs['pk'])
        doing.delete()
        return redirect('index')
