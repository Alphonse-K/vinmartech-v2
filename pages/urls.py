from django.urls import path

from pages.views import HomeView, TeamView, ContactView, AboutView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),  
    path('team/', TeamView.as_view(), name='team'),
    path('contact/', ContactView.as_view(), name='contact')
]
