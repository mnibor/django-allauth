from django.shortcuts import render

# Vista home
def home(request):
    return render(request, 'core/home.html')

def profile(request):
    return render(request, 'account/profile.html')