# voice_assistant/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assistant.urls')),
    path('ml_app/', include('assistant.urls'))
]
