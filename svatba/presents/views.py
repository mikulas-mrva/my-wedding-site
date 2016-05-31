from django.views.generic import ListView, CreateView, DetailView
from .models import Present, Person
from ..front.models import Message
from .forms import PersonForm
from ..front.forms import MessageForm


class PresentList(ListView):
    model = Present
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(PresentList, self).get_context_data(**kwargs)
        contactoform = MessageForm()
        context.update({
            'contactform': contactoform,
        })
        return context


class PresentDetail(DetailView):
    model = Present
    template_name = "presents/present_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PresentDetail, self).get_context_data(**kwargs)
        form = PersonForm(self.request.POST or None, initial={'present': context.get('present', None)})
        context.update({
            'form': form
        })
        
        return context


class PersonUpdate(CreateView):
    model = Person
    fields = ['present', 'email']
    template_name = "presents/present_detail.html"

    # def post(self, request, *args, **kwargs):
    #     print(request.REQUEST)

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super(PersonUpdate, self).get_context_data(**kwargs)
        form = PersonForm(self.request.POST or None)
        if form.is_valid():
            form.save()
        else:
            form.present = self.object
            context.update({'form': form})
        
        return context

    def get_absolute_url(self):
        return '/#dary'



class MessageUpdate(CreateView):
    model = Message
    template_name = "index.html"
    fields = ['sender', 'message']

    def get_context_data(self, **kwargs):
        context = super(MessageUpdate, self).get_context_data(**kwargs)
        contactoform = MessageForm()
        context.update({
            'contactform': contactoform,
        })
        return context
