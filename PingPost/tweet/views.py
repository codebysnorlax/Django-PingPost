from django.shortcuts import render

from .models import Tweet
from .forms import TweetForms
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

# for listing tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})

# for creating tweets
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
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

# for tweet delete
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_conform_delete.html', {'tweet':tweet})
