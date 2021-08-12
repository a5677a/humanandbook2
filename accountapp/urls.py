
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp import views
from accountapp.views import AccCreateView, AccDetailView, AccUpdateView, AccDeleteView

app_name = 'accountapp'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'),
    path('create/', AccCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccDeleteView.as_view(), name='delete'),
]