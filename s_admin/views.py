# Create your views here.
from s_admin.models import CustomUser, UserProfile

# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect
# from .forms import LoginForm

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Replace 'home' with your desired redirect URL after successful login
#             else:
#                 form.add_error(None, 'Invalid email or password.')
#     else:
#         form = LoginForm()

#     return render(request, 'login.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return redirect('login')  # Replace 'login' with your desired redirect URL after logout

