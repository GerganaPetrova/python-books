from django.conf.urls import patterns, include, url
from books.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', Index.as_view()),
    (r'^login', MyLogin.as_view()),
    (r'^logout', MyLogout.as_view()),
    (r'^signup', Signup.as_view()),
    (r'^books', Books.as_view()),
    (r'^book/(?P<id>\d+)/$', BookId.as_view()),
    (r'^book/(?P<id>\d+)/(?P<page_num>\d+)/$', BookIdOnPage.as_view()),
    (r'^quotes', MyQuotes.as_view()),
    (r'^quote', MyQuote.as_view()),
    (r'^reviews', MyReviews.as_view()),
    (r'^review', MyReview.as_view()),
    (r'^upload', Upload.as_view()),
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    # url(r'^booksite/', include('booksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
