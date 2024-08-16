from django.urls import path
from .views import registrerUser

urlpatterns = [
    path('personas/', admin.site.urls),
]