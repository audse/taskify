from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	url(r'^add/$', views.add_task, name='add_task'),
	url(r'^complete/(?P<pk>[0-9]+)/$', views.complete_task, name='complete_task'),
	url(r'^about/$', views.about_page, name='about_page'),
]
