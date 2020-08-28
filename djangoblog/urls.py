from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^articles/', include('articles.urls')),
    url('^about/$', views.about),
    url('^$', article_views.article_list, name='home'),
    url('^accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)