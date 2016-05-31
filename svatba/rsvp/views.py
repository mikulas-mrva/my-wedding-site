import logging
from django.views.generic import UpdateView, CreateView, TemplateView

from .models import Visitor
from .forms import VisitorForm

logger = logging.getLogger(__name__)


class VisitorUpdate(CreateView):
    form_class = VisitorForm
    template_name = "rsvp/visitor_detail.html"
    success_url = '/?potkame-se'


# class VisitorUpdate(CreateView):
#     # todo session!
#     model = Visitor
#     fields = ['email', 'name', 'baker', 'vegan', 'vegetarian', 'gluten_free']
#     template_name = "rsvp/visitor_detail.html"
#     # label_suffix = ''
#
#     def post(self, request, *args, **kwargs):
#         logger.info('POST?')
#         logger.info('incoming visitor')
#         logger.info('session pokus', [self.request.session.get('pokus')])
#         self.request.session['pokus'] = 'veci'
#         self.request.session.save()
#         return super(VisitorUpdate, self).post(request, *args, **kwargs)
#
#     # def get_context_data(self, **kwargs):
#     #     logger.debug('session: %s' % self.request.session.get('pokus'))
#     #     logger.error(self.request.session.get('visitor'))
#     #     self.request.session['pokus'] = 'veci'
#     #     context = super(VisitorUpdate, self).get_context_data(**kwargs)
#     #     form = VisitorForm(self.request.POST or None, label_suffix='')
#     #     logger.warning('incoming visitor', [kwargs])
#     #
#     #     if form.is_valid():
#     #         a = form.save()
#     #         self.request.session['visitor'] = form.email
#     #         logger.error('a', a=a)
#     #     else:
#     #         form.present = self.object
#     #     context['form'] = form
#     #
#     #     self.request.session.save()
#     #     return context
#
#
# class TesimeSe(TemplateView):
#     template_name = 'rsvp/tesime_se.html'
