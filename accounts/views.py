from django.shortcuts import render ,redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages

# Create your views here.
def upload_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"profile picture uploaded succesfully")
            return redirect('view_profile')
        else:
            messages.error(request,"error upload due to")
    else:
        form = ProfileForm()
        return render(request,'accounts/upload_profile.html',{'form':form})
    
def view_profile(request):
    profiles = Profile.objects.all()
    return render(request,'accounts/views_profile.html',{'profiles':profiles})


    




