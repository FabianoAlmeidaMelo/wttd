from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # context = dict(name="Fabiano Almeida", cpf='12345678901',
            #               email='falmeidamelo@uol.com.br', phone='12-98223-9764')

            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            mail.send_mail('Confirmação de inscrição',
                            body,
                            'contato@eventex.com.br',
                            ['contato@eventex.com.br', form.cleaned_data['email']])
            messages.success(request, 'Inscrição realizada com sucesso!')
            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html',
                         {'form': form })
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)
