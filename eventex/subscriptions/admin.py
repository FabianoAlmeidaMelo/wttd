from django.contrib import admin
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf','created_at',
                    'subscrites_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf','created_at')
    list_filter = ('created_at', 'paid')

    actions = ['mark_as_paid']

    def subscrites_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscrites_today.short_description = 'inscrito hoje?'
    subscrites_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Subscription, SubscriptionModelAdmin)
