from random import randint
from django.db import models
from django.db.models import Count
 
from django.utils import timezone



# Create your models here.
class Article(models.Model):
	title = models.TextField(default="none")
	keyphrase = models.TextField(default="none")
	headlines = models.TextField(default="none")
	content = models.TextField(default="none")
	question = models.TextField(default="none")
	tweet_quote = models.TextField(default="none")
	more_gist = models.TextField(default="none")
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.title
	
	

#####################
class OsManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
        
class OpeningStatement(models.Model):
	opening_statement = models.TextField(default="none")
	objects = OsManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.opening_statement
	
	


#####################
class DymManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
        
class DidYouMiss(models.Model):
	did_you_miss = models.TextField(default="none")
	link = models.TextField(default="none")
	objects = DymManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.did_you_miss
		
		
#####################
class ItpManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
		
class InThisPost(models.Model):
	in_this_post = models.TextField(default="none")
	objects = ItpManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.in_this_post
	
	
#####################
class LoneManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
	
class LinkOne(models.Model):
	title = models.TextField(default="none")
	link_one = models.TextField(default="none")
	objects = LoneManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.link_one
	
	
#####################
class LtwoManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
	
class LinkTwo(models.Model):
	title = models.TextField(default="none")
	link_two = models.TextField(default="none")
	objects = LtwoManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.link_two
		
		
#####################
class LthreeManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

class LinkThree(models.Model):
	title = models.TextField(default="none")
	link_three = models.TextField(default="none")
	objects = LthreeManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.link_three
	
	
#####################
class LfourManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
        
class LinkFour(models.Model):
	title = models.TextField(default="none")
	link_four = models.TextField(default="none")
	objects = LfourManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.link_four
	
	
	
#####################
class GameManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
        
class Game(models.Model):
	game = models.TextField(default="none")
	objects = GameManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.game
	
	
	
#####################
class EcManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
        
class EncourageComeback(models.Model):
	encourage_comeback = models.TextField(default="none")
	objects = EcManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.encourage_comeback
		

#####################
class StManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
        
class SubscriptionTalk(models.Model):
	subscription_talk = models.TextField(default="none")
	objects = StManager()
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.subscription_talk
		
		
	
	
	
	
	
	
	
	
	
	
	
