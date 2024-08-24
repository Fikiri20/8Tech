"""
URL configuration for myprojects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Changed the urlpatterns to more mordern and acceptable form

# Also configured the url patterns for the following to remove ambiguity

"""
housing
home
networking
news
club
association 
faith
academic and guidelines
"""


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('download/<int:file_id>', views.download_past_paper, name='download_pastpaper'),
    path('download/<int:file_id>', views.download_note, name='download_note'),
    path('', include('home.urls')),
    path('', include('housing.urls')),
    path('', include('networking.urls')),
    path('', include('news.urls')),
    path('', include('club.urls')),
    path('', include('association.urls')),
    path('', include('faith.urls')),
    path('', include('academic.urls')),
    path('', include('guidelines.urls')),

]
