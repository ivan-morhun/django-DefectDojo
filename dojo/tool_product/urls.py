from django.conf.urls import url
from django.contrib import admin
from django.apps import apps
import views

urlpatterns = [
    url(r'^product/(?P<pid>\d+)/tool_product/add$', views.new_tool_product, name='new_tool_product'),
    url(r'^product/(?P<pid>\d+)/tool_product/all$', views.all_tool_product, name='all_tool_product'),
    url(r'^product/(?P<pid>\d+)/tool_product/(?P<ttid>\d+)/edit$', views.edit_tool_product, name='edit_tool_product'),
    url(r'^product/(?P<pid>\d+)/tool_product/(?P<ttid>\d+)/run$', views.run_tool_product, name='run_tool_product'),
    url(r'^product/(?P<pid>\d+)/tool_product/(?P<ttid>\d+)/delete$', views.delete_tool_product,
        name='delete_tool_product'), ]
