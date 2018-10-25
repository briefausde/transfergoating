from django.shortcuts import redirect
from django.views.generic import *
from .models import *
from .utils import farm_init, herder_create


class FarmView(DetailView):
    model = Farm
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['herder'] = self.object.herder if self.object else farm_init()
        context['herders'] = Herder.objects.all()
        context['goats'] = Goat.objects.all()
        return context

    def get_object(self, queryset=None):
        return self.model.objects.first()


class HerderCreateView(View):

    def get(self, request, *args, **kwargs):
        herder_create()
        return redirect('/')

