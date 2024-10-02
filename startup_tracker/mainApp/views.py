from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StartupKYCForm

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
