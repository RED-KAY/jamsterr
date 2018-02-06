from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, user_logged_in, views
from django.views import generic
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import UserForm

# Create your views here.

def Logout(request):
	logout(request)

	return redirect('music:index')

class Login(views.LoginView):
	template_name = 'user/login.html'
	#redirect_field_name = reverse_lazy('music:index')
	#redirect_authenticated_user = True

class UserFormView(View):
	form_class = UserForm
	template_name = 'user/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})
	
	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned (normalised) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('music:index')

		return render(request, self.template_name, {'form' : form})
