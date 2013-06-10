# encoding: utf-8

from django.contrib import admin

from models import Event, Comment

def mark_private(modeladmin, request, queryset):
	queryset.update(public=False)
	modeladmin.message_user(request,
							u'Eventos atualizados com sucesso!')
mark_private.short_description = u'Marcar evento como Privado'

def mark_public(modeladmin, request, queryset):
	queryset.update(public=True)
	modeladmin.message_user(request,
							u'Eventos atualizados com sucesso!')

mark_public.short_description = u'Marcar evento como Público'

class EventAdmin(admin.ModelAdmin):

	list_display = ['name', 'type','public', 'comments_count']
	search_fields = ['name', 'description']
	actions = [mark_private, mark_public]

admin.site.register(Event, EventAdmin)

class CommentAdmin(admin.ModelAdmin):

	list_display = ['name', 'email', 'event']
	search_fields = ['event__name']


admin.site.register(Comment,CommentAdmin)

