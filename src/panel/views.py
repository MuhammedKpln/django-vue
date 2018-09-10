from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    def get(self, request):
        return render(request, 'panel.index.html')


class Dashboard(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return render(request, 'panel.dashboard.html')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'panel.login.html'
    success_url = '/panel'

    def form_valid(self, form):
        try:
            auth = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            login_system = login(self.request, auth)
            messages.success(self.request, 'You have successfully logged in!')

            return redirect(self.success_url)
        except Exception as e:
            messages.error(
                self.request, 'Could not login, please try again another time.')
            return redirect(self.success_url)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'panel.register.html'
    success_url = '/panel'

    def form_valid(self, form):
        created = form.create_user(self.request)
        if created:
            auth = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password1'))
            login_to_system = login(self.request, auth)
            messages.success(self.request, 'You have successfully registered.')
        else:
            messages.error(
                self.request, 'Could not register, please try again another time.')
        return super().form_valid(form)


@login_required
def LogoutView(request):
    log_out = logout(request)
    return redirect('/')
