"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from courses.views import CourseViewSet
from courses.views import StepViewSet
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView
from mysite.schema import schema

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'steps', StepViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^$', views.home),
    url(r'^react_demo/', views.react_demo),
    url(r'^suggestion/', views.suggestion),
    url(r'^api/', include(router.urls)),
    url(r'^graphql',GraphQLView.as_view(graphiql=True, schema=schema)),

]
urlpatterns += staticfiles_urlpatterns()