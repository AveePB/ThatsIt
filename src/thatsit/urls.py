"""
URL configuration for thatsit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('auth/', include('apps.authz.urls'), name='auth'),
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    path('settings/', include('apps.settings.urls'), name='settings'),
    path('profiles/', include('apps.profiles.urls'), name='profiles'),
    path('networks/', include('apps.networks.urls'), name='networks'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)