from django.conf.urls import patterns, url

from todoList import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^todo/(?P<pk>\d+)/$', views.DetailTodoView.as_view(), name='detail_todo'),
    url(r'^todo/add/(?P<categ>\d+)$', views.AddTodoView.as_view(), name='add_todo'),
    url(r'^todo/(?P<pk>\d+)/delete/$', views.DeleteTodoView.as_view(), name='delete_todo'),
    url(r'^todo/(?P<pk>\d+)/update/$', views.UpdateTodoView.as_view(), name='update_todo'),
    
    url(r'^categ/(?P<pk>\d+)/$', views.DetailCategView.as_view(), name='detail_categ'),
    url(r'^categ/add/$', views.AddCategView.as_view(), name='add_categ'),
    url(r'^categ/(?P<pk>\d+)/delete/$', views.DeleteCategView.as_view(), name='delete_categ'),
    url(r'^categ/(?P<pk>\d+)/update/$', views.UpdateCategView.as_view(), name='update_categ'),
)
