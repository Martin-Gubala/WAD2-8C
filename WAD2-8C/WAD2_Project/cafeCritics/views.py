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
"""
Handles user registration by presenting a sign-up form and processing the submission of form data to create a new user account. 
Once registration is successful, the user is logged in immediately and redirected to the homepage.
"""
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Saves the new user to the database
            form.save()
            # Login the user after signing up
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Redirect the user to the home page with context
            context_dict = {
                'top_cafes': Cafe.objects.order_by('-average_rating')[:5],
                'top_drinks': Drink.objects.order_by('-rating')[:5]
            }
            return render(request, 'registration/home.html', context=context_dict)
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form, 'show_search': False})

"""
Handles user authentication by showing a login form and processing the submitted data to verify the user's identity. 
After a successful login, users are redirected to the homepage.
"""
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

# Logs out the current user and redirects to the home page.
def logout_view(request):
    logout(request) 
    return redirect('cafeCritics:home_page') 

# Displays the homepage of the site, showcasing a list of top-rated cafes and drinks.
def home_view(request):
    cafe_list = Cafe.objects.order_by('-average_rating')[:5]
    drink_list = Drink.objects.order_by('-rating')[:5]

    return render(request, 'registration/home.html', {
        'top_cafes': cafe_list,
        'top_drinks': drink_list,
        'show_search': True
    })
# Displays all cafes with an option to filter by average rating through a GET request.
def cafes_view(request):
    rating = request.GET.get('rating')  # Get the rating value from the GET request
    if rating:  # Check if a rating was provided
        cafe_list = Cafe.objects.filter(average_rating=rating)  #Filter cafes by the provided rating
    else:
        cafe_list = Cafe.objects.all()  # No rating provided, show all cafes

    context_dict = {'cafes': cafe_list}
    return render(request, 'cafes.html', context=context_dict)

# Static view for rendering the about page of the website.
def about_view(request):
    return render(request, 'about.html')
# Displays the account settings page for the logged-in user.
def account_settings_view(request):
    return render(request, 'account_settings.html', {'show_search': False})
# Displays detailed information about a specific cafe, including its drinks and reviews.
def show_cafe(request, cafe_name_slug):
    context_dict = {}
    try:
        cafe = Cafe.objects.get(slug=cafe_name_slug)
        drinks = Drink.objects.filter(cafe=cafe)
        reviews = Review.objects.filter(cafe=cafe)
        context_dict['drinks'] = drinks
        context_dict['cafe'] = cafe
        context_dict['reviews'] = reviews
    except Cafe.DoesNotExist:
        context_dict['cafe'] = None
        context_dict['drinks'] = None
        context_dict['reviews'] = None

    return render(request, 'cafe.html', context=context_dict)

# Displays all drinks associated with a specific cafe.
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

# AJAX view for dynamically updating cafe details without reloading the page
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

# Provides an interface for users to write and submit reviews for cafes. Redirects to the cafe detail page upon submission.
@login_required
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

# Handles the creation and setup of new cafes by authenticated users. 
# Redirects to the home page upon successful cafe creation.
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

# Manages the search function, enabling users to find cafes by their names.
def search_results(request):
    query = request.GET.get('q', '')
    results = Cafe.objects.filter(name__icontains=query) if query else None
    return render(request, 'search_results.html', {'query':query, 'results': results})

# Displays a user's profile page, showcasing their cafes if they are business users, and their reviews if they are personal users.
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


# Manages account settings updates and password changes for the logged-in user, ensuring that changes are securely applied.
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

# Provides functionality for users to edit and update cafe details, ensuring that only authorized users can make changes.
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