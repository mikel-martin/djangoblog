from django.conf.urls import url

from . import views

app_name = 'articles'

urlpatterns = [
    url('^$', views.article_list, name="list"),
    url('^create/$', views.article_create, name="create"),
    url('^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
