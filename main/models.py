from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def image_path(instance, filename):
    return "message/{}/{}/{}".format(instance.user, instance.title, filename)

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True) 
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TimeStampedModel):
    user = models.ForeignKey(User, related_name='message', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to=image_path, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    message = models.ForeignKey(Message, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField()
