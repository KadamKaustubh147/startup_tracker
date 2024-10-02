from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User  # For startup user accounts


# Model for startup details (KYC)
class Startup(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=20)  # Phone or email
    company_details = models.TextField()
    founder = models.ForeignKey(User, on_delete=models.CASCADE)  # To link to a startup account
    created_at = models.DateTimeField(auto_now_add=True)
    # Uss time pe time record karlega without asking

    def __str__(self):
        return self.name

# Model to track progress of startups (monthly reports, milestones)
class Progress(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='progress_reports')
    report_date = models.DateField()
    progress_description = models.TextField()
    milestone_achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"Progress report for {self.startup.name} on {self.report_date}"

# Model for schemes (EIR, Grants, Scale-up)
class Scheme(models.Model):
    SCHEME_CHOICES = [
        ('EIR', 'Entrepreneur in Residence'),
        ('GRANT', 'Startup Grant'),
        ('SCALEUP', 'Scale-up Investment'),
    ]
    
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='schemes_applied')
    scheme_type = models.CharField(max_length=20, choices=SCHEME_CHOICES)
    application_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Applied', 'Applied'), ('Shortlisted', 'Shortlisted'), ('Selected', 'Selected'), ('Rejected', 'Rejected')])
    fund_disbursal_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Optional until disbursal

    def __str__(self):
        return f"{self.scheme_type} for {self.startup.name} (Status: {self.status})"


