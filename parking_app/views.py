from django.shortcuts import render
from .models import InputRegister
from .forms import InputRegisterForm
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.
def home(request):
    return render(request, "index.html")


class CreateRegister(CreateView):
    model = InputRegister
    template_name = "parking_web/create_register.html"
    form_class = InputRegisterForm
    success_url = "/"
