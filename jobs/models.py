# jobs/models.py
from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

class JobListing(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('applied', 'Applied'),
        ('interviewing', 'Interviewing'),
        ('offered', 'Offered'),
        ('rejected', 'Rejected'),
        ('not_interested', 'Not Interested'),
    ]

    WORK_TYPE_CHOICES = [
        ('onsite', 'On-site'),
        ('hybrid', 'Hybrid'),
        ('remote', 'Remote'),
    ]

    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    url = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True)
    skills_required = models.TextField(blank=True)
    date_posted = models.DateField(default=timezone.now)
    date_applied = models.DateField(null=True, blank=True)
    distance_to_sb = models.IntegerField(null=True, blank=True, help_text="Distance to Santa Barbara in miles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    class Meta:
        ordering = ['-created_at']