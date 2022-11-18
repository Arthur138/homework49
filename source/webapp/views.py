from django.shortcuts import render , redirect , get_object_or_404
from webapp.models import Doings , Status , Type
# from django.http import HttpResponseRedirect , HttpResponseNotFound
# from webapp.forms import DoingForm
from django.views.generic import View , TemplateView
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

class DoingCreate(TemplateView):
    template_name = 'doings_create.html'
    def get(self, request ,*args, **kwargs):

        return render(request, 'doings_create.html')