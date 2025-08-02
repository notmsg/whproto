from django.urls import path
from .views import recycle_view
urlpatterns = [
    path('', recycle_view, name='recycle'),
]