from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Booking


def home(request):
    return render(request, 'bookings/home.html')


# ---------------- Authentication ----------------

def signup(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not username or not password:
            error = 'Username and password are required.'
        elif password != confirm_password:
            error = 'Passwords do not match.'
        elif User.objects.filter(username=username).exists():
            error = 'That username is already taken.'
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

    return render(request, 'bookings/signup.html', {'error': error})


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('booking_list')
        else:
            error = 'Invalid username or password.'
    return render(request, 'bookings/login.html', {'error': error})


def logout_view(request):
    auth_logout(request)
    return redirect('login')


# ---------------- CRUD ----------------

@login_required(login_url='login')
def booking_list(request):
    bookings = Booking.objects.all().order_by('id')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required(login_url='login')
def booking_add(request):
    if request.method == 'POST':
        Booking.objects.create(
            customer_name=request.POST.get('customer_name'),
            event_type=request.POST.get('event_type'),
            booking_date=request.POST.get('booking_date'),
            phone=request.POST.get('phone'),
        )
        return redirect('booking_list')
    return render(request, 'bookings/booking_form.html', {'action': 'Add'})


@login_required(login_url='login')
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.customer_name = request.POST.get('customer_name')
        booking.event_type = request.POST.get('event_type')
        booking.booking_date = request.POST.get('booking_date')
        booking.phone = request.POST.get('phone')
        booking.save()
        return redirect('booking_list')
    return render(request, 'bookings/booking_form.html', {'action': 'Edit', 'booking': booking})


@login_required(login_url='login')
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    return redirect('booking_list')
