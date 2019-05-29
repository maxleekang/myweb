from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
    url(r'(?P<article_id>[0-9]+)/$', views.blog_article, name="blog_content")
]