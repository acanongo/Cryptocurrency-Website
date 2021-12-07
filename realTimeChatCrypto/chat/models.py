from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User as auth_user


class SuggestionModel(models.Model):

    suggestionText = models.CharField(max_length=400)
    author = models.ForeignKey(auth_user, on_delete= models.CASCADE)
    datePublished = models.DateTimeField(auto_now_add = True)
    image = models.ImageField( max_length= 200, upload_to='uploads/%Y/%m/%d/', null = True )

    imageDescription = models.CharField(max_length= 240, null = True)


    def __str__(self):

        return str(self.suggestionText) + "  --  " + str(self.author.username)


class CommentModel(models.Model):

    commentText = models.CharField(max_length= 400)
    author = models.ForeignKey(auth_user, on_delete= models.CASCADE)
    suggestion = models.ForeignKey(SuggestionModel, on_delete= models.CASCADE)
    datePublished = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.commentText) +  "  ---  " + str(self.author.username)



'''
class realTimeChatMessage(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
        
'''