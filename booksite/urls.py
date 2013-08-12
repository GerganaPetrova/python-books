from django.conf.urls import patterns, include, url
from books.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', Index.as_view()),
    (r'^login', LoginView.as_view()),
    (r'^logout', LogoutView.as_view()),
    (r'^signup', Signup.as_view()),
    (r'^books', Books.as_view()),
    (r'^book/(?P<id>\d+)/$', BookId.as_view()),
    (r'^book/(?P<id>\d+)/(?P<page_num>\d+)/$', BookIdOnPage.as_view()),
    (r'^quotes', QuotesView.as_view()),
    (r'^quote', QuoteView.as_view()),
    (r'^reviews', ReviewsView.as_view()),
    (r'^review', ReviewView.as_view()),
    (r'^upload', Upload.as_view()),
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    # url(r'^booksite/', include('booksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
