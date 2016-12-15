from django.conf.urls import url

from directory import views

urlpatterns = [
    url(r'^$', views.doctor_list, name='list'),
    url(r'^detail/(?P<doctor_id>[0-9]+)/$', views.doctor_details, name='detail'),
    url(r'^add/', views.doctor_add, name='add')
]
