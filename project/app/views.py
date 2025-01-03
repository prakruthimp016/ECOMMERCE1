from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .forms import identify,EmailForm,RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import ProductItem,Product,ProductCategory



# Create your views here.
def  create_user(request):
    fm=RegisterForm()
    context={
        'form':fm
    }
    if request.method == 'POST':
        fm=RegisterForm(data=request.POST)
        if fm.is_valid():

            fm.save()
            
            return redirect('signin')
           
    return render(request,'register.html',context)

def signin(request):
    fm=AuthenticationForm()
    context={
        'form':fm
    }
    if request.method == 'POST':
        fm=AuthenticationForm(data=request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                if user.is_authenticated:
                    login(request,user)
                    messages.success(request,'user account created successfully')
                    return redirect('home')
                    
                messages.error(request,'invalid username and password')
                # return HttpResponse('invalid username and password')
    return render(request,'login.html',context)

@login_required(login_url='/signin/')
def home(request):
    return render(request,'home.html')

def signout(request):
    return redirect('signin')

@login_required(login_url='/signin/')
def PasswordChange(request):
    username=request.user
    user=User.objects.get(username=username)
    fm=PasswordChangeForm(user)
    context={
        'form':fm
    }
    if request.method== 'POST':
        fm=PasswordChangeForm(user,data=request.POST)
        if fm.is_valid():
            user=fm.save()
            return HttpResponse('Password changed')
            send_mail('user login',
                    user.username+'password change',
                    'prakruthimp016@gmail.com',
                    [email],
                     fail_silently=True)
            
        return HttpResponse('invalid password')
    return render(request,'pwd_change.html',context)


def reset_password(request, username):
        user = User.objects.get(username=username)  
        fm = SetPasswordForm(user) 
        context = {
            'form': fm,
        }
        if request.method == "POST":
            form = SetPasswordForm(user, data=request.POST)  
            if form.is_valid():
                form.save() 
                messages.success(request, "Password has been reset successfully.")
                return redirect("login") 
            else:
                messages.error(request, "Please correct the errors below.")
       
        return render(request, 'resetpwd.html', context)



    
def identifyview(request):
    fm=identify()
    context={
        'form':fm
    }
    if request.method == 'post':
        fm=identify(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                url='/resetpwd/'+username+'/'
                return redirect(url)
            return redirect('signin')
    return render(request,'identify.html',context)
    
# display product
def product(request):
    products = ProductItem.objects.all()
    context={
        'products':products
    }
    return render(request,'product.html',context)

# single product
def product_details(request,slug):
    if ProductItem.objects.filter(slug=slug).exists():
        product = ProductItem.objects.get(slug=slug)

        context={
            'products':product,
        }
        return render(request,'products_details.html',context)
    return HttpResponse('Product does not exist')


def category_detail(request, slug):
    if ProductCategory.objects.filter(slug=slug).exists():
        category = ProductCategory.objects.get(slug=slug)
        
        products=Product.objects.filter(product_category__exact=category)
        product_items=ProductItem.objects.filter(product__in=products)
        context={
                 
            'products':    product_items
        }
        return render(request, 'category_detail.html', context)
    return HttpResponse('invalid category')


def home(request):
    categories=ProductCategory.objects.all()
    products = ProductItem.objects.all()
    context={
        'categories':categories,
        'products':products
    }
    return render(request,'home.html',context)