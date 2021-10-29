from django.urls import path
from hotel import views

app_name = 'hotel'

urlpatterns = [
  path("", views.index, name='home'),
  path("booking", views.booking, name='booking'),
  path("cancelation", views.cancel, name='cancel'),
  path("dining", views.dining, name='dining')
]
