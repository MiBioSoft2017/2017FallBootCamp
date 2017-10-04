# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
	message = models.TextField()
	sender = models.ForeignKey(User, related_name="user_sender")
	recipient = models.ForeignKey(User, related_name="user_recipient")