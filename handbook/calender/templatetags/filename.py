#filename.py
import os
from django import template
from datetime import date
from datetime import datetime
register = template.Library()
 
@register.filter
def getfilename(value):
    return os.path.basename(value.file.name[:-4])
    

@property
def is_past_due(self):
    return date.today() - self.date
# {% load filename %} 
# {{submission.file | getfilename }}