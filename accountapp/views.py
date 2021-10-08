from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin
from accountapp.decorators import acc_ownership_required
from accountapp.forms import AccUpdateForm, UserForm
from articleapp.models import Article

has_ownership = [acc_ownership_required, login_required]

class SignupView(CreateView):
    model = User
    #form_class = UserCreationForm
    form_class = UserForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/signup.html'

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'accountapp/signup.html', {'form': form})

def send_email(request):
    subject = "message"
    to = ["whdsbswn@gmail.com"]
    from_email = "id@gmail.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()

class AccDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    pagination_by = 8

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccUpdateForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
