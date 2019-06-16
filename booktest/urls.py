from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^books/$', views.SearchBooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.SearchSingleBookView.as_view()),
]