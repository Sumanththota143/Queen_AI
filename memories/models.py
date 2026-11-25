#Queen should remember past chats. like we ask who am i - it should say out details , so this file 


from django.conf import settings
from django.db import models


# this tells djago this is a memory model
class Memory(models.Model):

    # a user can have many memories like name , place , edu , job, hobbie
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="memories"
    )

    # main data to store as memory
    content = models.TextField()

    # having 1000's of memories creates confusion , so divide them into categories
    category = models.CharField(
        max_length=100,
        blank=True
    )

    #create timestamp
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    #record timestamp
    updated_at = models.DateTimeField(
        auto_now=True
    )

    # store as string only 1st 50 in django
    def __str__(self):
        return self.content[:50]
