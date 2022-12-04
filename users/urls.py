from django.urls import path
from users.views import (
    me_view
)

urlpatterns = [
    path('me/', me_view, name='me_view'),
]
