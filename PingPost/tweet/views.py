from django.shortcuts import render
from .models import Tweet
from .forms import TweetForms, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')

# for listing tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})

# for creating tweets
@login_required
def tweet_create(request):
    if request.method == 'POST' :
        form = TweetForms(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms()
    return render(request, 'tweet_form.html', {'form': form})

# for editing tweets
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    old_photo = tweet.photo
    
    if request.method == 'POST':
        form = TweetForms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user
            
            # Delete old photo if it's being replaced
            if old_photo and new_tweet.photo != old_photo:
                if os.path.isfile(old_photo.path):
                    os.remove(old_photo.path)
            
            new_tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

# for tweet delete
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_conform_delete.html', {'tweet':tweet})

# for user registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
