from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from onbase import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("volunteer/", views.volunteer, name="volunteer"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("ideas/", views.ideas, name="ideas"),
    path("team/", views.team, name="team"),
    path("contact/", views.contact, name="contact"),
    path("donate/", views.donate, name="donate"),
    path("success/", views.success, name="success"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$', views.activate, name='activate'),
    path('admin/',admin.site.urls),
]
