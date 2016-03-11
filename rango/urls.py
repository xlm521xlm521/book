from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns( '',
        url(r'^$', views.index, name='index' ) ,
        url(r'^showpython/', views.showpython, name='showpython'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'), # New!
        url(r'^add_category/$' , views.add_category, name='add_category' ), # NEW MAPPING!
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^register/$' , views.register, name='register' ) , # New!
        url(r'^login/$' , views.user_login, name='login' ) ,
        url(r'^xlm/' , views.xlm, name='xlm' ) ,
        url(r'^logout/$' , views.user_logout, name='logout' ) ,
        url(r'^category/(?P<category_name_slug>[\w\-]+)/xz/$', views.xz, name='xz'),
        url(r'^x001/', views.x001,  name='x001'),
        url(r'^x002/', views.x002,  name='x002'),
        url(r'^x003/', views.x003,  name='x003'),
        url(r'^xz/', views.xz,  name='xz'),
)
