from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from forms import RegisterForm, PictureForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from main.models import Tweet, User, Following, MyUser, Messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect(reverse('login_page'))
        else:
            messages.add_message(request, messages.ERROR, 'registration incomplete')
            return redirect(reverse('register'))

    else:
        form = RegisterForm()
        return render(request, 'registerForm.html', {'form': form})


def login_page(request):
    form = ''
    username = ''
    password = ''
    if request.user.is_authenticated():
        return redirect(reverse('main'))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('main'))
            else:
                return redirect(reverse('login_page'))
        else:
            return redirect(reverse('login_page'))

    return render(request, 'login.html', {form: 'form'})


@login_required(login_url='login_page')
def main(request):
        tweets = Tweet.objects.all().order_by('-date')
        #image = MyUser.objects.get(user=tweets)
        if not tweets:
            tweets = None
        return render(request, 'main.html', {'tweets': tweets, 'username': request.user.username})


@login_required(login_url='login_page')
def likes(request, username, id):
    user = User.objects.get(username=username)
    tweet = Tweet.objects.get(id=id)
    if request.user != user:
        tweet.likes.add(request.user)
        tweet.save()
        return redirect(reverse(main))
    else:
        HttpResponse('error')
    return redirect(reverse(main))


@login_required(login_url='login_page')
def new_tweet(request):
    if request.method == 'POST':
        tweet = request.POST['tweet']
        image = request.FILES['image']
        time = datetime.datetime.now()
        Tweet.objects.create(owner=request.user, context=tweet, image=image, date=time)
        return redirect(reverse('main'))


@login_required(login_url='login_page')
def profile(request, username):
    user = User.objects.get(username=username)
    try:
        image = MyUser.objects.get(user=user)
    except MyUser.DoesNotExist:
        image = None
    tweets = Tweet.objects.filter(owner=user).order_by('-date')
    following = Following.objects.filter(follower=user.id).count()
    followers = Following.objects.filter(following=user.id).count()
    if not tweets:
        tweets = None
    return render(request, 'profile.html', {'tweets': tweets,
                                            'username': user.username,
                                            'following': following,
                                            'followers': followers,
                                            'image': image})


@login_required(login_url='login_page')
def follow(request, username):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if request.user == user:
            return HttpResponseBadRequest('What the hell are you doing?!')
        if request.user != user:
            Following.objects.create(following=user, follower=request.user)
        else:
            return HttpResponse('Something went wrong:(')
    return redirect(reverse('main'))


@login_required(login_url='login_page')
@csrf_exempt
def settings(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(id=request.user.id)
        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        return HttpResponse('User information successfully changed.')


@login_required(login_url='login_page')
@csrf_exempt
def profile_pic(request):
    if request.method == 'POST':
        image = request.FILES['image']
        MyUser.objects.update(image=image, user=request.user)
        return HttpResponse('Profile picture successfully saved.')


@login_required(login_url='login_page')
def all_messages(request):
    #  contacts
    followings = Following.objects.filter(follower=request.user)
    return render(request, 'allMessages.html', locals())


@login_required(login_url='login_page')
def send_message(request, username):
    send_from = User.objects.get(username=username)
    print send_from
    # if request.method == 'POST':
    content = request.POST['content']
    print content
    #     Messages.objects.create(content=content, send_from=send_from)
    return render(request, 'allMessages.html')


@login_required(login_url='login_page')
def log_out(request):
    logout(request)
    return redirect(reverse('login_page'))


