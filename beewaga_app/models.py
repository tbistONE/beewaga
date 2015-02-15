from django.db import models
from django.contrib.auth.models import User
import hashlib

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    supports = models.ManyToManyField('self', related_name='supported_by', symmetrical=False)


    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

    