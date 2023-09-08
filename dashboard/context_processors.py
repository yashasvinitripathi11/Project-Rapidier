# your_app/context_processors.py

from .models import WhatsNew

def has_notification(request):
    return {
        'has_notification': WhatsNew.has_notification(),
        'blinking_dot_class': 'blinking-dot'
    }
