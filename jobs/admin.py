from django.contrib import admin
from .models import Company, JobListing

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name', 'location')

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'work_type', 'status', 'salary_min', 'salary_max', 'date_posted')
    list_filter = ('status', 'work_type', 'company')
    search_fields = ('title', 'company__name', 'description', 'skills_required')
    date_hierarchy = 'date_posted'