import logging

from django.shortcuts import render_to_response
from django.template import RequestContext

logger = logging.getLogger(__name__)


def error404(request):
    logger.warning('404', [request])
    response = render_to_response('index.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
