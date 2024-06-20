from django.shortcuts import render, get_object_or_404, redirect
from .models import UserInfo
from .forms import UserForm

def home(request):
    return render(request, 'home.html')

def user_list(request):
    users = UserInfo.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(UserInfo, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def update_user(request, pk):
    user = get_object_or_404(UserInfo, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(UserInfo, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'delete_user.html', {'user': user})
