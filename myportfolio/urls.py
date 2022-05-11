from django.urls import path
from .views import MainView
from django.conf.urls.static import static

urlpatterns = [
    path('', MainView.as_view(), name="index")
]