from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('books.views',
    url(r'^$', 'index'),
    url(r'^login', 'my_login'),
    url(r'^logout', 'my_logout'),
    url(r'^signup', 'signup'),
    url(r'^books', 'books'),
    url(r'^book/(?P<id_num>\d+)/$', 'book_id'),
    url(r'^book/(?P<id_num>\d+)/(?P<page_num>\d+)/$', 'book_id_on_page'),
    url(r'^quotes', 'quotes'),
    url(r'^quote', 'quote'),
    url(r'^reviews', 'reviews'),
    url(r'^review', 'review'),
    url(r'^upload', 'upload'),
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    # url(r'^booksite/', include('booksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
