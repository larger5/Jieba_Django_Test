from django.contrib import admin
from django.urls import path
# 注意要引入 url
from django.conf.urls import url
# 注意要引入自己的 views
from booktest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^fenci/$', views.fenci),
    url(r'^index/$', views.index),
    url(r'^fenci2/$', views.fenci2),
]
