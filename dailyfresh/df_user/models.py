# coding = utf-8
from django.db import models


# Create your models here.
class UserInfo(models.Model):
	uname = models.CharField(max_length = 20)
	upwd = models.CharField(max_length = 40)
	def __str__(self):
		# pk为primary key,相当于id
		return "%d" % self.pk_