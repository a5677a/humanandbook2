from django.urls import path
from profileapp.views import PfCreate, PfUpdate

app_name = 'profileapp'

urlpatterns = [
    path('create/', PfCreate.as_view(), name='create'),
    path('update/<int:pk>', PfUpdate.as_view(), name='update'),
]