# coding:utf-8
from django.contrib import admin
from .models import Article, Person
 
 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)
    def save_model(self, request, obj, form, change):
        if change:# 更改的时候
            obj_original = self.model.objects.get(pk=obj.pk)
        else:# 新增的时候
            obj_original = None 
        obj.user = request.user
        obj.save()
		
 
'''
定制加载的列表, 根据不同的人显示不同的内容列表，比如输入员只能看见自己输入的，审核员能看到所有的草稿
'''
class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

class PersonAdmin(admin.ModelAdmin):
    #list_display = ('name', 'age')
    list_display = ('full_name',)
    search_fields = ('name',)
 
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)