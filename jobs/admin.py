from django.contrib import admin
from .models import Company, JobListing, Resume, CoverLetter

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website')
    search_fields = ('name', 'location')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'filename', 'created_at', 'updated_at')
    search_fields = ('name', 'filename', 'notes')

@admin.register(CoverLetter)
class CoverLetterAdmin(admin.ModelAdmin):
    list_display = ('name', 'filename', 'created_at', 'updated_at')
    search_fields = ('name', 'filename', 'notes')

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status', 'resume_used', 'cover_letter_used')
    list_filter = ('status', 'work_type', 'company', 'resume_used', 'cover_letter_used')
    list_display = ('title', 'company', 'location', 'work_type', 'status', 'salary_min', 'salary_max', 'date_posted')
    list_filter = ('status', 'work_type', 'company')
    search_fields = ('title', 'company__name', 'description', 'skills_required')
    date_hierarchy = 'date_posted'