from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CleaningForm
from django.http import HttpResponse

class CarUpdate(UpdateView):
    model = Car
    fields = ['color']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'


class CarCreate(CreateView):
    model = Car
    fields= '__all__'
    success_url = '/cars/'


def home(request):
    return HttpResponse('<h1>hello</h1>')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    cleaning_form = CleaningForm()
    return render(request, 'cars/detail.html', {'car': car, 'cleaning_form': cleaning_form})

def add_cleaning(request, car_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.car_id = car_id
        new_cleaning.save()
        return redirect('detail', car_id=car_id)


