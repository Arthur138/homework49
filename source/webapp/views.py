from django.shortcuts import render , redirect , get_object_or_404
from webapp.models import Doings , Status , Type
# from django.http import HttpResponseRedirect , HttpResponseNotFound
from webapp.forms import DoingForm
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
    template_name = "doings_create.html"
    def get(self,request, *args, **kwargs):
        form = DoingForm()
        return render(request, "doings_create.html", {'form': form})
    def post(self,request, *args, **kwargs):
        form = DoingForm(data=request.POST)
        if form.is_valid():
            new_doing = Doings.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('doing_view', pk=new_doing.pk)
        else:
            return render(request, "doings_create.html", {'form': form})

class DoingUpdateView(TemplateView):
    template_name = "update.html"
    def get(self,request, *args, **kwargs):
        doing = get_object_or_404(Doings, pk=kwargs['pk'])
        form = DoingForm(initial={
            'summary':doing.summary,
            'description':doing.description,
            'status':doing.status,
            'type':doing.type
        })
        return render(request, "update.html", {'form': form})
    def post(self, request, *args, **kwargs):
        doing = get_object_or_404(Doings, pk=kwargs['pk'])
        form = DoingForm(data=request.POST)
        if form.is_valid():
            doing.summary = form.cleaned_data.get('summary')
            doing.description = form.cleaned_data.get('description')
            doing.status = form.cleaned_data.get('status')
            doing.type = form.cleaned_data.get('type')
            doing.save()
            return redirect('doing_view', pk=doing.pk)
        else:
            return render(request, "doings_create.html", {'form': form})