from django.urls import path
from .views import Orders  # Import the view class

app_name = 'pizza'  # Replace 'your_app' with your app's name

urlpatterns = [
    path('pizza/create_order/',
         Orders.create_order,
         name='create_order'),
    path('pizza/choice/', Orders.choice, name='choice'),
    path('pizza/getting_status/',
         Orders.getting_status,
         name='getting_status'),
]
