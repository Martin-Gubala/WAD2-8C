from django.shortcuts import render, redirect, get_object_or_404
from .models import Cafe
from .models import Drink
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def home_view(request):
    cafe_list = Cafe.objects.order_by('-average_rating')[:5]
    drink_list = Drink.objects.order_by('-rating')[:5]

    context_dict = {}
    context_dict['cafes'] = cafe_list
    context_dict['drinks'] = drink_list

    return render(request, 'registration/home.html', context=context_dict)

def cafes_view(request):
    cafe_list = Cafe.objects
    
    context_dict = {}
    context_dict['cafes'] = cafe_list

    response = render(request, 'cafes.html')
    return response

def about_view(request):
    return render(request, 'about.html')

def account_settings_view(request):
    return render(request, 'account_settings.html')

def cafe_view(request, cafe_id):
    cafe = get_object_or_404(Cafe, id=cafe_id)
    drink_list = Drink.objects

    context_dict = {}
    context_dict['cafe'] = cafe
    context_dict['drinks'] = drink_list

    return render(request, 'cafe.html', context_dict)

def review_view(request):
    return render(request, 'review.html')