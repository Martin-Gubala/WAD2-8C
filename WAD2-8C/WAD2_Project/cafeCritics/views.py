from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Cafe, Drink, Review, UserProfile
from .forms import EditCafeForm, ReviewForm, UserRegistrationForm, UserLoginForm, CafeSetupForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth import logout

# Create your views here.

# Consolidated signup and register views into one
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            context_dict = {
                'top_cafes': Cafe.objects.order_by('-average_rating')[:5],
                'top_drinks': Drink.objects.order_by('-rating')[:5]
            }
            return render(request, 'registration/home.html', context=context_dict)
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form, 'show_search': False})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form, 'show_search': False})

def logout_view(request):
    logout(request) 
    return redirect('cafeCritics:home_page') 

def home_view(request):
    cafe_list = Cafe.objects.order_by('-average_rating')[:5]
    drink_list = Drink.objects.order_by('-rating')[:5]

    return render(request, 'registration/home.html', {
        'top_cafes': cafe_list,
        'top_drinks': drink_list,
        'show_search': True
    })

def cafes_view(request):
    cafe_list = Cafe.objects.all()
    
    context_dict = {}
    context_dict['cafes'] = cafe_list

    response = render(request, 'cafes.html', context=context_dict)
    return response

def about_view(request):
    return render(request, 'about.html')

def account_settings_view(request):
    return render(request, 'account_settings.html', {'show_search': False})

def show_cafe(request, cafe_name_slug):
    context_dict = {}
    try:
        cafe = Cafe.objects.get(slug=cafe_name_slug)
        drinks = Drink.objects.filter(cafe=cafe)
        context_dict['drinks'] = drinks
        context_dict['cafe'] = cafe
    except Cafe.DoesNotExist:
        context_dict['cafe'] = None
        context_dict['drinks'] = None

    return render(request, 'cafe.html', context=context_dict)

def show_drinks(request, cafe_name_slug):
    context_dict = {}
    try:
        cafe = Cafe.objects.get(slug=cafe_name_slug)
        drinks = Drink.objects.filter(cafe=cafe)
        context_dict['drinks'] = drinks
        context_dict['cafe'] = cafe
    except Cafe.DoesNotExist:
        context_dict['cafe'] = None
        context_dict['drinks'] = None

    return render(request, 'drinks.html', context=context_dict)

def show_cafeAJAX(request, cafe_name_slug):
    context_dict = {}
    try:
        cafe = Cafe.objects.get(slug=cafe_name_slug)
        drinks = Drink.objects.filter(cafe=cafe)
        context_dict['drinks'] = drinks
        context_dict['cafe'] = cafe
    except Cafe.DoesNotExist:
        context_dict['cafe'] = None
        context_dict['drinks'] = None

    return render(request, 'cafeAJAX.html', context=context_dict)

def review_view(request, cafe_name_slug):
    cafe = get_object_or_404(Cafe, slug=cafe_name_slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.cafe = cafe
            review.save()
            return redirect('cafeCritics:show_cafe', cafe_name_slug=cafe_name_slug)
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form, 'cafe': cafe})

def cafe_setup_view(request):
    if request.method == 'POST':
        form = CafeSetupForm(request.POST)
        if form.is_valid():
            cafe = form.save(commit=False)
            cafe.owner = request.user
            cafe.save()
            return redirect('home')
    else:
        form = CafeSetupForm()
    return render(request, 'registration/cafe_setup.html', {'form': form})

def search_results(request):
    query = request.GET.get('q', '')
    results = Cafe.objects.filter(name__icontains=query) if query else None
    return render(request, 'search_results.html', {'query':query, 'results': results})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    cafes = Cafe.objects.filter(owner=user) if user_profile.user_type == 'business' else None
    reviews = Review.objects.filter(user=user) if user_profile.user_type == 'personal' else None

    context = {
        'user_profile': user_profile,
        'cafes': cafes,
        'reviews': reviews,
    }
    return render(request, 'profile.html', context)


@login_required
def account_settings_view(request):
    user = request.user

    #User update form
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        password_form = PasswordChangeForm(user, request.POST)

        if 'update_user' in request.POST:  
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Your account details have been updated.")
                return redirect('cafeCritics:account_settings')

        elif 'change_password' in request.POST:  
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  
                messages.success(request, "Your password has been updated.")
                return redirect('cafeCritics:account_settings')

    else:
        user_form = UserUpdateForm(instance=user)
        password_form = PasswordChangeForm(user)

    return render(request, 'account_settings.html', {
        'user_form': user_form,
        'password_form': password_form,
        'show_search': False
    })

@login_required
def edit_cafe_view(request, cafe_name_slug):
    cafe = get_object_or_404(Cafe, slug=cafe_name_slug)
    if request.method == 'POST':
        form = CafeSetupForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
            messages.succes(request, "Your cafe details have been updated.")
            return redirect('cafeCritics:show_cafe', cafe_name_slug=cafe_name_slug)
        else:
            form = EditCafeForm(instance=cafe)
        return render(request, 'edit_cafe.html', {'form': form, 'cafe': cafe})