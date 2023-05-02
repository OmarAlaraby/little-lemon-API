from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


# create the user's Token automatically
User = get_user_model()

@receiver(post_save , sender=User)
def CreateToken(sender , instance=None , created=False , **kwargs):
    if created:
        Token.objects.create(user=instance)