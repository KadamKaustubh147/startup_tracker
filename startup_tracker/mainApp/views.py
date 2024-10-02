from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StartupKYCForm
from django.contrib.auth import login
from .forms import SignupForm

# Create your views here.


@login_required
def formKyc(request):
    if request.method == 'POST':
        form = StartupKYCForm(request.POST)
        if form.is_valid():
            startup = form.save(commit=False)  # Create the Startup instance but don't save to DB yet
            startup.founder = request.user  # Set the founder to the logged-in user
            startup.save()  # Now save the instance to the database
            return redirect('kyc_success')  # Redirect to a success page (create this later)
    else:
        form = StartupKYCForm()

    return render(request, 'kyc_form.html', {'form': form})

def kyc_success(request):
    return render(request, 'kyc_success.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request, user)  # Log the user in immediately after signup
            return redirect('kyc_success')  # Redirect to the KYC form or another page
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
