from django.shortcuts import render,redirect
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request,'index.html')

def tweetlist(request):
    tweets=Tweet.objects.all().order_by('created_at')
    return render(request,'tweetlist.html',{'tweets':tweets})

@login_required
def tweetcreate(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweetlist')
    else:
        form=TweetForm()
    return render(request,'tweetforms.html',{'form':form})    

@login_required
def tweetedit(request,tweetid):
    tweet=get_object_or_404(Tweet,pk=tweetid,user=request.user)
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweetlist')
        
    else:
         form=TweetForm(instance=tweet)
    return render(request,'tweetform.html',{'form':form})    

@login_required
def tweetdelete(request,tweetid):
    tweet=get_object_or_404(Tweet,pk=tweetid,user=request.user)
    if request.method=="POST":
        tweet.delete()  
        return redirect('tweetlist')
    return render(request,'confirmdelete.html',{'tweet':tweet}) 

def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST) 
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweetlist')
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form':form})    
                