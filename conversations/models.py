
from django.conf import settings
from django.db import models


#this class stores conversational details
class Conversation(models.Model):
                   #this tells this is a db model to django
    
    # if a user is deleted all this chats will be deleted
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conversations"
    )

    #to name a title to the conversation
    title = models.CharField(
        max_length=255,
        blank=True
    )

    #automatically records the current date and time 
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    #updates the created date and time at each chat 
    updated_at = models.DateTimeField(
        auto_now=True
    )

    #new convo must be on top, this class does this part
    class Meta:
        ordering = ["-updated_at"]

    #if their is no name for chat it puts convo id as name
    def __str__(self):
        return self.title or f"Conversation {self.id}"


#message model to store every individual message in a chat
class Message(models.Model):

    # tell django to store msg acc to roles 
    class Role(models.TextChoices):
        USER = "user", "User"
                #1st is for django and 2nd is for user display
        ASSISTANT = "assistant", "Assistant"
        SYSTEM = "system", "System"

    #to delete all the messages of that convo
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    #to store the role name
    role = models.CharField(
        max_length=20,
        choices=Role.choices
    )

    #to store the reply of query or data
    content = models.TextField()

    # timestamp
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    #the newest msh should be down of screen , so no "-"
    class Meta:
        ordering = ["created_at"]

    #to tell django who is user and what is 1st 50 char of reply
    def __str__(self):
        return f"{self.role}: {self.content[:50]}"
