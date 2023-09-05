from django.shortcuts import render
from .models import InputRegister
from .forms import InputRegisterForm, FinishRegisterForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
def home(request):
    return render(request, "parking_web/index.html")


class CreateRegister(CreateView):
    model = InputRegister
    template_name = "parking_web/create_register.html"
    form_class = InputRegisterForm
    success_url = "/"


class ListRegisterActive(ListView):
    model = InputRegister
    context_object_name = "vehicle_list"
    template_name = "parking_web/List_active_vehicle.html"


class FinishRegister(UpdateView):
    model = InputRegister
    template_name = "parking_web/Finish_register.html"
    form_class = FinishRegisterForm
    success_url = "/"
