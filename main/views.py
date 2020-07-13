from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from main.models import *

# Create your views here.
def MainView(request):
	return render(request, "main/main.html")
	
	
def AllView(request):
	posts = Article.objects.order_by("-pub_date")[:12]
	context = {"posts": posts}
	return render(request, "main/all.html", context)
	
	
def SinglePostView(request, post_id):
	article = Article.objects.get(id=post_id)
	opening_statement = OpeningStatement.objects.random()
	did_you_miss = DidYouMiss.objects.random()
	in_this_post = InThisPost.objects.random()
	link_one = LinkOne.objects.random()
	link_two =  LinkTwo.objects.random()
	link_three = LinkThree.objects.random()
	link_four = LinkFour.objects.random()
	game = Game.objects.random()
	encourage_comeback = EncourageComeback.objects.random()
	subscription_talk = SubscriptionTalk.objects.random()
		
	context = {
		"article": article, "opening_statement": opening_statement, "did_you_miss": did_you_miss,
		"in_this_post": in_this_post, "link_one": link_one, "link_two": link_two, "link_three": link_three, 
		"link_four": link_four, "game": game, "encourage_comeback": encourage_comeback,
		"subscription_talk": subscription_talk,
		
		}
		

	return render(request, "main/result.html", context)

def IndexView(request):
	if request.method == "POST":
		title = request.POST.get("title")
		keyphrase = request.POST.get("keyphrase")
		headlines = request.POST.get("headlines")
		content =  request.POST.get("content")
		question =  request.POST.get("question")
		tweet_quote = request.POST.get("tweet_quote")
		more_gist = request.POST.get("more_gist")
		
		#save to db
		article = Article.objects.create(title=title, keyphrase=keyphrase, headlines=headlines, content=content, question=question, tweet_quote=tweet_quote, more_gist=more_gist)
		
		#article = get_object_or_404(Article, id=article_id)
		opening_statement = OpeningStatement.objects.random()
		did_you_miss = DidYouMiss.objects.random()
		in_this_post = InThisPost.objects.random()
		link_one = LinkOne.objects.random()
		link_two =  LinkTwo.objects.random()
		link_three = LinkThree.objects.random()
		link_four = LinkFour.objects.random()
		game = Game.objects.random()
		encourage_comeback = EncourageComeback.objects.random()
		subscription_talk = SubscriptionTalk.objects.random()
		
		context = {
		"article": article, "opening_statement": opening_statement, "did_you_miss": did_you_miss,
		"in_this_post": in_this_post, "link_one": link_one, "link_two": link_two, "link_three": link_three, 
		"link_four": link_four, "game": game, "encourage_comeback": encourage_comeback,
		"subscription_talk": subscription_talk,
		
		}
		

		return render(request, "main/result.html", context)

		

	else:
		context = {}
		return render(request, "main/index.html", context)

		
		
		
		
		
		
		
		
		
