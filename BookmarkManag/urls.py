from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # API for storing Data of Customer'Bookmark
    path('create', views.BookmarkApi.as_view()),
    # API for Browsw Data from CustomerBookmark with all values, can short Data with 'ordering' param and can perform search via title
    path('browse', views.BookmarkListView.as_view()),
    # Api for Link Customer's Bookmark with Customer Profile API
    path('addCusBook', views.BookmarkBrowseApi.as_view()), 
    path('creteApi', views.CustomerProApi.as_view()),
    path('createData', views.create), 
    path('createCus', views.createCus), 
    path('linkData', views.createCusBook),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^browsedetails/(?P<customer_id>[\w\-]+)/(?P<bookmark_id>[\w\-]+)/$', views.details_view,name='Details_view'), 
    path('listData', views.list_viewData), 
]


