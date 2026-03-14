from django.shortcuts import render
from .models import Like, Tweet, Comment
from .forms import TweetForm, UserRegistrationForm, CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.http import JsonResponse
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")

    paginator = Paginator(tweets, 5)   # show 5 tweets per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "tweet_list.html", {
        "page_obj": page_obj
    })
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list') 
    else:
        form = TweetForm()
    
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id,user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user 
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        tweet=tweet
    )

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse(
        {
            "liked": liked,
            "total_likes": tweet.like_set.count(),
            }
    )

@login_required
def add_comment(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.tweet = tweet
            comment.save()

    return redirect("tweet_list")

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    comment.delete()
    return redirect("tweet_list")

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(user=user).order_by("-created_at")
    return render(request, "profile.html", {"profile_user": user, "tweets": tweets})