from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from database.models import CustomUser, Commodity, Comment
from web.form import *
from persiantools.jdatetime import JalaliDate
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
from web.functions.func import *
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
	stuff = Commodity.objects.order_by('-date')
	# modified_stuff = list(stuff.values())
	# for i in range(len(stuff)):
	# 	user_id = stuff[i].user.id
	# 	modified_stuff[i]['date'] = date_convertor(modified_stuff[i]['date'])
	# 	modified_stuff[i]['price'] = price_convertor(stuff[i].price)
	# 	modified_stuff[i]['user'] = stuff[i].user
	# 	modified_stuff[i]['avatar'] = CustomUser.objects.filter(user=user_id).values_list('image', flat=True).get()
	comment_form = CommentSection()
	context = {'all_items': stuff, "comment_form" : comment_form, 'home_page': 'active',"css_name": "home"}
	return render(request, 'home.html', context)

def profile(request):
	if not request.user.is_authenticated:
	 	return redirect('web:sign_in')
	else:
		stuff = Commodity.objects.filter(user=request.user.id).order_by('-date').values_list('image')
		user = request.user
		# modified_user = list(CustomUser.objects.filter(user=request.user.id).values())
		# modified_user[0]['username'] = request.user.username
		context = {
			'stuff': stuff,
			'user': user,
			"css_name": "profile",
			"profile_page":"active",
			}
		return render(request, 'profile.html', context)

#################################################################	
###############            LOGIN START            ###############
def sign_in(request):
	from django.contrib import auth
	if request.user.is_authenticated:
		return redirect('web:home')
	sign_in_form = SignIn()

	context = {
		"sign_in_form":sign_in_form,
		"css_name":"sign_in",
	}
	return render(request, 'sign_in.html', context)
	
@csrf_exempt
def login(request):
	from django.contrib import auth
	if request.user.is_authenticated:
		return redirect('web:home')

	if request.method == 'POST':
		form = SignIn(request.POST)
		username = form['username'].value()
		password = form['password'].value()
		user = auth.authenticate(
                	request,
                	username=username,
                	password=password
                )
		if user is not None:
			auth.login(request, user)
			messages.success(request, 'شما به درستی وارد شدید')
			return redirect('web:home')
		else:
			messages.warning(request, 'رمز عبور یا نام کاربری شما اشتباه است')
			return redirect('web:sign_in')


	else:
		return redirect('web:sign_in')

###############             LOG IN END            ###############
#################################################################	



#################################################################	
###############           REGISTER START          ###############

def sign_up(request):
	from django.contrib import auth
	if request.user.is_authenticated:
		return redirect('web:home')

	
	sign_up_form = SignUp()

	context = {
		"sign_up_form":sign_up_form,
		"css_name":"sign_up"
	}
	return render(request, 'sign_up.html', context)

def register(request):
	from django.contrib.auth.models import User
	from django.contrib import auth

	if request.user.is_authenticated:
		return redirect('web:home')


	sign_up_form = SignUp()
	form = SignUp(request.POST)
	username = form['username'].value()
	email = form['email'].value()
	password = form['password'].value()
	
	if User.objects.filter(username=username).exists():

		messages.error(request, 'این نام کاربری قبلا استفاده شده است')
		context = {
		"sign_up_form":sign_up_form,
		"css_name" : "sign_up",
		}
		return render(request, 'sign_up.html', context)
	else:
		user = User.objects.create_user(
			username,
			email,
			password   
		)
		# create custom user
		user.save()
		custom_user = CustomUser(
			user=user,
		)
		custom_user.save()
		
		auth.login(request, user)
		messages.success(request, 'عضوت شما به درستی انجام شد')
		return redirect('web:home')

	
###############            REGISTER END           ###############
#################################################################	


def log_out(request):
	from django.contrib.auth import logout
	logout(request)
	return redirect ('web:home')


def forget_pass(request):
	pass	

def search(request):
	users = User.objects.all()
	# modified_users = list(users.values())
	# for i in range(len(users)):
	# 	user_id = users[i].id
	# 	modified_users[i]['avatar'] = CustomUser.objects.filter(user=user_id).values_list('image', flat=True).get()
	context = {
		"users": users,
		"css_name" : "search",
		"search" : "active"
		}
	return render(request, 'search.html', context)

def add(request):
	if request.method == 'POST':
		form = Add(request.POST, request.FILES)
		if form.is_valid():
			title = form['title'].value()
			price = form['price'].value()
			image = form.cleaned_data['image']
			user = User.objects.get(id=request.user.id)
			# date = datetime.now()
			description = form['description'].value()
			commodity = Commodity(
				title=title,
				price=price,
				image=image,
				user=user,
				# date=date, 
				description=description 
			)		
			commodity.save()
			return redirect('web:home')
	else:
		if request.user.is_authenticated:
			# can add commodity
			add_form = Add()
			context = {
				"add_form" : add_form,
				"css_name" : "add",
				"add" : "active"
				}
			return render(request, 'add.html', context)
		else:
			# redirect to login page
			sign_in_form = SignIn()
			context = {
				"sign_in_form" : sign_in_form,
				"css_name":"sign_in",
			}
			return render(request, 'sign_in.html', context)

def user_infos(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = UserInfos(request.POST, request.FILES)
			print(form.errors)
			if form.is_valid():
				bio = form['bio'].value()
				full_name = form['full_name'].value()
				job = form['job'].value()
				customer = form['customer'].value()
				phone_number = form['phone_number'].value()
				sex = form['sex'].value()
				birth_date = form['birth_date'].value()
				image = form.cleaned_data['image']
				address_lat = form.cleaned_data['address_lat']
				address_lon = form.cleaned_data['address_lon']
				try:
					custom_user = CustomUser.objects.get(user=request.user.id) # it's not correct
					custom_user.bio = bio
					custom_user.full_name = full_name
					custom_user.job = job
					custom_user.customer = customer
					custom_user.phone_number = phone_number
					custom_user.sex = sex
					custom_user.birth_date = birth_date
					custom_user.image = image
					custom_user.address_lat = address_lat
					custom_user.address_lon = address_lon
					custom_user.save()
				except CustomUser.DoesNotExist:
					custom_user = CustomUser(
						user=request.user,
						full_name=full_name,
						bio=bio,
						job=job,
						customer=customer,
						phone_number=phone_number,
						sex=sex,
						birth_date=birth_date,
						image=image,
						address_lat=address_lat,
						address_lon=address_lon
					)
					custom_user.save()
				return redirect('web:home')
		else:
			user_infos_form = UserInfos()
			context = {
				"user_infos_form" : user_infos_form,
				"css_name":"user_infos",
			}
			return render(request, 'user_infos.html', context)
	else:
		return redirect('web:sign_up')

@csrf_exempt
def like(request, pk):
	from django.http import JsonResponse
	print(request.POST.get('stuff_id'))
	commodity = get_object_or_404(Commodity, id=request.POST.get('stuff_id'))
	if commodity.likes.filter(id = request.user.id).exists():
		commodity.likes.remove(request.user)
	else:
		commodity.likes.add(request.user)
	# return redirect('web:home')
	# return HttpResponseRedirect(reverse('web:home', args=[str(pk)]))
	return JsonResponse()

def comment(request, pk):
	form = CommentSection(request.POST)
	body = form['body'].value()
	user = request.user
	commodity = get_object_or_404(Commodity, id=request.POST.get('stuff_id'))
	comment = Comment(
		commodity=commodity,
		user=user,
		body=body,
	)
	comment.save()
	return redirect('web:home')

def search_user(request):
	users = User.objects.all()
	context = {
		"users": users,
		"css_name" : "search",
		"search" : "active"
		}
	return render(request, 'search_user.html', context)

def search_commodity(request):
	commodities = Commodity.objects.all()
	context = {
		"commodities": commodities,
		"css_name" : "search",
		"search" : "active"
	}
	return render(request, 'search_commodity.html', context)