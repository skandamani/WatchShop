from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WatchesUploads,Wishlist, Cart, WatchReview, CartItem
from .forms import UploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    watches = WatchesUploads.objects.all()
    context = {'watches_t' : watches}
    return render(request, "home.html", context)

def About(request):
    return render(request, "about.html")


#function based view
@login_required(login_url="/login")
def Upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()

    return render(request, "WatchUpload.html", {'form': form})

#class based view

from django.views import View
from django.utils.decorators import method_decorator

class UploadClass(View):

    @method_decorator(login_required)
    def get(request):
        form = UploadForm()
        return render(request, "WatchUpload.html", {'form': form})
    
    @method_decorator(login_required)
    def post(request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "WatchUpload.html", {'form': form})



from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login, logout
def login_page(request):
    if request.method == "POST":
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username= user_name, password = password)

            if user is not None: 
                login(request,user)
                return redirect('home')
            return  render(request, "login.html", {'form': form})


    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form})


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404
def show_product(request,id):
    product = get_object_or_404(WatchesUploads, id=id)
    reviews_obj = WatchReview.objects.filter(product=product)
    return render(request, 'product.html', {'product': product, 'reviews': reviews_obj})


#WishList

def addtowish(request,id):
    user= request.user
    product= WatchesUploads.objects.get(id=id)
    obj1,created = Wishlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

@login_required(login_url="/login")
def show_wishlist(request):
    user = request.user
    wish_object = Wishlist.objects.get(user=user)
    return render(request, 'wishlist.html', {'user_products': wish_object.products.all()})


def removewish(request,id):
    product_rm = WatchesUploads.objects.get(id=id)

    wish_obj= Wishlist.objects.get(user=request.user)
    wish_obj.products.remove(product_rm)
    return render(request, 'wishlist.html', {'user_products': wish_obj.products.all()})


#Cart

def addtocart(request,id):
    #check if user has cart or not
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    #fetch the product with given id
    product= WatchesUploads.objects.get(id=id)


    #create a cart item using product abd user
    cart_item, created = CartItem.objects.get_or_create(user= user_cart, product=product)
    cart_item.product=product
    cart_item.save()
    return redirect('home')

@login_required(login_url="/login")
def show_cart(request):
    #user- cart : get this user cart

    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_objects = user_cart.cartitem_set.all()
    return render(request, 'cart.html', {'user_products': cart_objects})


def removecart(request,id):
    product_rm = WatchesUploads.objects.get(id=id)

    cart_obj= CartItem.objects.get(user=request.user)
    cart_obj.product.remove(product_rm)
    return render(request, 'cart.html', {'user_products': cart_obj.product.all()})


from django.http import JsonResponse
def show_data(request):
    start_text = request.GET.get('param1')
    watches = list(WatchesUploads.objects.filter(name__startswith= start_text).values_list())

    print("This is my parameter", request.GET.get('param1'))
    message = {
                    "name": "Hello Ram",
                    "watches": watches
              }
    return JsonResponse(message)


    


