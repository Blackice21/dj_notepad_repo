from django.db import models
from datetime import datetime

# Create your models here.
LABEL_CHOICES = (
    ('p','primary'),
    ('se','secondary'),
    ('d','danger'),
    ('s','success'),
    ('w','warning'),
    ('i','info'),
    ('d','dark'),
    ('l','light'),
)

class Note(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField()
    pub_date = models.DateField(default=datetime.now())
    label = models.CharField(choices=LABEL_CHOICES, max_length=2, default='p')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def short_notes(self):
        return self.notes[0:21]