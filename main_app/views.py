from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import WateringForm
from .models import Plant, Fertilizer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user = request.user)
    return render(request, 'plants/index.html', {'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    watering_form = WateringForm()
    fertilizers_not_used = Fertilizer.objects.exclude(id__in = plant.fertilizers.all().values_list('id'))
    return render(request, 'plants/detail.html', {
        'plant': plant, 
        'watering_form': watering_form,
        'fertilizers': fertilizers_not_used,
    })

@login_required
def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail', plant_id=plant_id)

@login_required
def assoc_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
    return redirect('detail', plant_id=plant_id)

@login_required
def remove_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.remove(fertilizer_id)
    return redirect('detail', plant_id=plant_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid sign up - please try again'
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)
    
class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ('name', 'type', 'genus', 'description')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ('name', 'type', 'genus', 'description')

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

class FertilizerList(LoginRequiredMixin, ListView):
    model = Fertilizer

class FertilizerDetail(LoginRequiredMixin, DetailView):
    model = Fertilizer

class FertilizerCreate(LoginRequiredMixin, CreateView):
    model = Fertilizer
    fields = '__all__'

class FertilizerUpdate(LoginRequiredMixin, UpdateView):
    model = Fertilizer
    fields = ('name', 'brand')

class FertilizerDelete(LoginRequiredMixin, DeleteView):
    model = Fertilizer
    success_url = '/fertilizers/'