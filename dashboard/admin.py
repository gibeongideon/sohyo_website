from django.contrib import admin
from .models import (
    MainPage, Cause, Feedback, User, Common ,Event ,Leader, Testimomial, Statistic)
from django.contrib.auth.admin import UserAdmin


# class CommonAdmin(admin.ModelAdmin):
    # list_display = ('id','mobile_no','email','address', 'created_at', 'updated_at')
    # list_display_links = ('id', )
    # search_fields = ('id', )
    # list_editable = ('mobile_no','email','address',)

admin.site.register(Common)#, CommonAdmin)

class MainPageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'titleup', 'titledown','donate','small_description',
        'about_our_foundation_header','about_our_foundation_sub_header',
        'about_our_foundation_desc1','about_our_foundation_desc2',
        'mobile_no',
        'email','address',
        'what_we_are_doing','mission1', 'mission1_desc', 'mission2',
        'mission2_desc','mission4', 'mission4_desc','dev_mobile','about1_image','about2_image','active',
        )
    list_display_links = ('id',)
    search_fields = ('id',)
    list_editable = (    
        'titleup', 'titledown','donate','small_description',
        'about_our_foundation_header','about_our_foundation_sub_header',
        'about_our_foundation_desc1','about_our_foundation_desc2',
        'mobile_no',
        'email','address',
        'what_we_are_doing','mission1', 'mission1_desc', 'mission2',
        'mission2_desc','mission4', 'mission4_desc','dev_mobile','about1_image','about2_image', 'active',
        )
        
admin.site.register(MainPage, MainPageAdmin)


class CauseAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'description', 'donation_progress','donation_prog','raised','goal', 'created_at', 'updated_at')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('description','donation_progress','raised','goal',)

admin.site.register(Cause, CauseAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'description','startime','endtime','date','venuetitle','town', 'created_at', 'updated_at')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('description','image','startime','endtime','date','venuetitle','town',)

admin.site.register(Event, EventAdmin)



class DuserAdmin(UserAdmin):

    list_display = (
        'id', 'username', 'phone_number','email', 'first_name', 'last_name',
        'member_type', 'others', 'last_login', 'active')

    list_display_links = ('id','username')
    search_fields = ('id',)
    ordering = ('id',)
    readonly_fields = ('password',)
    list_editable = ('phone_number','email', 'first_name', 'last_name', 'member_type',)  

admin.site.register(User, DuserAdmin)



class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'full_name', 'email', 'subject', 'created_at', 'updated_at')
    list_display_links = ('id', )
    search_fields = ('id', )
    # list_editable = ('message', 'full_name', 'email', 'subject',)
    list_filter=( 'email','created_at')

admin.site.register(Feedback, FeedbackAdmin)


class LeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ( 'image', 'name', 'title',)
    list_filter = ('created_at',)

admin.site.register(Leader, LeaderAdmin)



class TestimomialAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'title','description', 'created_at', 'updated_at')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('image', 'name', 'title','description',)
    list_filter = ('created_at',)

admin.site.register(Testimomial, TestimomialAdmin)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'type','created_at', 'updated_at')
    list_display_links = ('id', )
    search_fields = ('id', )
    list_editable = ('value', 'type',)
    list_filter = ('created_at',)

admin.site.register(Statistic, StatisticAdmin)