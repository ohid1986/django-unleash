from django.conf.urls import url

from .views import (startup_detail, startup_list, tag_detail, tag_list)

# url(regular_expression,
# view,
# optional_dictionary_of_extra_values,
# name=a_name)

urlpatterns = [
    url(r'^startup/$',
        startup_list,
        name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    url(r'^tag/$',
        tag_list,
        name='organizer_tag_list'),

    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
]