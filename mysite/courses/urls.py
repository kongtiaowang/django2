from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.get_courses, name='list'),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail, name='step_de'),
    url(r'(?P<pk>\d+)/$', views.course_detail, name='course_de'),
    url(r'add/$', views.courses_add),

]