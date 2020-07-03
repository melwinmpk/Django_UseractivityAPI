from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('',views.login, name='index'), # HomeView views.index
    path('', TemplateView.as_view(template_name="index.html")),
]
