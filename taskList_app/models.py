from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileImg(models.Model):
    profileImg = models.ImageField(upload_to="avatar", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile Picture"

    def __str__(self):
        return self.user.username
    