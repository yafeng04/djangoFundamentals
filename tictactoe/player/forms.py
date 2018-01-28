from .models import Invitation
from django.forms import ModelForm

class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude=('from_user', 'timestamp')