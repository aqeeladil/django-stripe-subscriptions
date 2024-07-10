
from django.shortcuts import render, get_object_or_404, redirect
# from django.shortcuts import render, redirect   #crm
# from .models import Tweet
# from .models import Record     #crm
from .forms import UserRegistrationForm
# from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages   
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def home(request):
	# records = Record.objects.all()
	# user = User
	# Check to see if logging in
    return render(request, 'home.html')


def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
            return render(request, 'registration/login.html')


# crm
def register_user(request):
    if request.method == 'POST':
          form = UserRegistrationForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               user.set_password(form.cleaned_data['password1'])

            #    # Authenticate and login
            #    username = form.cleaned_data['username']
            #    email = form.cleaned_data['email']
            #    password = form.cleaned_data['password1']
            #    user_auth = authenticate(username=username, email=email, password=password)

               user.save()
               login(request, user)
               messages.success(request, "You Have Successfully Registered! Welcome!")

               return redirect('home')
    else:
          form = UserRegistrationForm()
          return render(request, 'registration/register.html', {'form':form})
     
    return render(request, 'registration/register.html', {'form':form})


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


# def tweet_list(request):
#     tweets = Tweet.objects.all().order_by('created_at')
#     return render(request, 'tweet_list.html', {'tweets':tweets})

# @login_required
# def tweet_create(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST, request.FILES)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save()
#             return redirect('tweet_list')
#     else: 
#         form = TweetForm()
#     return render(request, 'tweet_form.html', {'form':form})


# @login_required
# def tweet_edit(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == "POST":
#         form = TweetForm(request.POST, request.FILES, instance=tweet)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm(instance=tweet)
#     return render(request, 'tweet_form.html', {'form':form})


# def tweet_delete(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == "POST":
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})




#crm 


# def customer_record(request, pk):
# 	if request.user.is_authenticated:
# 		# Look Up Records
# 		customer_record = Record.objects.get(id=pk)
# 		return render(request, 'record.html', {'customer_record':customer_record})
# 	else:
# 		messages.success(request, "You Must Be Logged In To View That Page...")
# 		return redirect('home')



# def delete_record(request, pk):
# 	if request.user.is_authenticated:
# 		delete_it = Record.objects.get(id=pk)
# 		delete_it.delete()
# 		messages.success(request, "Record Deleted Successfully...")
# 		return redirect('home')
# 	else:
# 		messages.success(request, "You Must Be Logged In To Do That...")
# 		return redirect('home')


# def add_record(request):
# 	form = AddRecordForm(request.POST or None)
# 	if request.user.is_authenticated:
# 		if request.method == "POST":
# 			if form.is_valid():
# 				add_record = form.save()
# 				messages.success(request, "Record Added...")
# 				return redirect('home')
# 		return render(request, 'add_record.html', {'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('home')


# def update_record(request, pk):
# 	if request.user.is_authenticated:
# 		current_record = Record.objects.get(id=pk)
# 		form = AddRecordForm(request.POST or None, instance=current_record)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "Record Has Been Updated!")
# 			return redirect('home')
# 		return render(request, 'update_record.html', {'form':form})
# 	else:
# 		messages.success(request, "You Must Be Logged In...")
# 		return redirect('home')

