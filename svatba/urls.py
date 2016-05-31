from django.conf.urls import include, url
from django.contrib import admin

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.core.urlresolvers import reverse

from svatba.presents.views import PresentList, PresentDetail, PersonUpdate, MessageUpdate
from svatba.rsvp.views import VisitorUpdate
from svatba.views import error404

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PresentList.as_view(), name='present_list'),
    url(r'^dary/(?P<slug>[-_\w]+)/$', PresentDetail.as_view(), name='present_detail'),
    url(r'^daruju/$', PersonUpdate.as_view(success_url='/?pridano#dary'), name='person_update'),
    url(r'^zprava/$', MessageUpdate.as_view(success_url='/?poslano#kontakt'), name='message_update'),
    url(r'^prijdu(/)?$', VisitorUpdate.as_view(), name='visitor_update'),
]


handler404 = error404
handler400 = error404
