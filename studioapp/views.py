from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Contact, Work
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
def home(request):
    return render(request, 'home.html')

def work(request):
    works=Work.objects.all()
    return render(request, 'work.html',{'works':works})

def service(request):
    return render(request, 'service.html')
# def signup_view(request):

#     return render(request, 'signup.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password != password1:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully.")
        return redirect('login')

    return render(request, 'signup.html')
def contact(request):
    if request.method == 'POST':
        # Extract values directly from request.POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        location = request.POST.get('location')

        # You can now do whatever you want with these values
        # Example: Save to database manually or use for email
        # Assuming you have a Contact model:
        from .models import Contact
        Contact.objects.create(
            name=name,
            email=email,
            message=message,
            location=location
        )

        messages.success(request, "Your booking was submitted successfully!")
        return redirect('bookinglog')  # Replace with the actual name of your success URL
    
    return render(request, 'contact.html')


def booking_list(request):
    bookings = Contact.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})







def Custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)