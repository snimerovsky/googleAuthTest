from django.shortcuts import render
from users.models import Profile
# Create your views here.


def index(request):
    profile_data = {}
    if (not request.user.is_anonymous):
        profile_data = Profile.objects.filter(user=request.user).values()
    return render(request, 'profile/index.html', {'profile_data': profile_data})


def not_found(request, exception):
    return render(request, '404.html')
