from django.db import models

class Club(models.Model):
    
    CLUB_STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    
    club_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=CLUB_STATUS)
    club_description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=9, default='113631232')
    officials_name = models.CharField(max_length=100, default='8Tech')

    def __str__(self):
        return self.club_name
