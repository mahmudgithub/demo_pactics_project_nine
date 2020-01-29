
from django.urls import path

from .views import One

urlpatterns = [
	path('',One.as_view(),name='hello'),
]
