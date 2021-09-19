from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models
from .models import PostModel ,Category , Comment,Note
from jalali_date import datetime2jalali, date2jalali
from django import forms
from ckeditor.widgets import CKEditorWidget
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	

class InlineModelInline(admin.StackedInline):
    model = Comment
    fields = ('text','status',)
    extra = 0

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:

        model = PostModel
        fields= ['title','body','category','auther','thumnail','status','publish']
        


class PostAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display=('title','category','slug','created')
    #inlines = [InlineModelInline]
    form = PostAdminForm
    


 

    def get_created_jalali(self, obj):
		    return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    

admin.site.register(PostModel,PostAdmin)
admin.site.register(Category)
admin.site.register(Note)


# Register your models here.
