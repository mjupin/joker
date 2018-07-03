from django.urls import path

from . import views

app_name = 'run_results'
urlpatterns = [
    path('', views.ResultsView.as_view(), name='index'),

]