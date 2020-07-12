from django.urls import path
from . import views

#app_name = "main"

urlpatterns = [
	path("app/", views.IndexView, name="index"),
	path("", views.MainView, name="main"),
	path("database/", views.AllView, name="all"),
	path("single-post/<int:post_id>/", views.SinglePostView, name="single_post"),
	
	#path("result/", views.ResultView, name="result"),
	
	
]
