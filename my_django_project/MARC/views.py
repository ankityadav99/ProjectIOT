from django.shortcuts import render, render_to_response, redirect
from rest_framework import viewsets
from .models import ProductInfo, ProductionProductInfo, ProductFeedback, ProductType
from .serializer import ProductInfoSerializer, \
    ProductionProductInfoSerializer, \
    ProductFeedbackSerializer
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserRegister, UserLogin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class ProductInfoView(viewsets.ModelViewSet):
    """
    ModelViewSet is going to takecare lot of stuff for us
    1) Perform all operation of HTTP (POST/PUT/GET)
    2) Dont have explicitilty mention these methods
    3) Mostly these methods are common and every one is doing the same, better to use inbuilt
    4) Also instead of handling every case explicitly we are using the ModelViewSet
    """
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


class ProductionProductInfoView(viewsets.ModelViewSet):
    queryset = ProductionProductInfo.objects.all()
    serializer_class = ProductionProductInfoSerializer


class ProductFeedbackView(viewsets.ModelViewSet):
    queryset = ProductFeedback.objects.all()
    serializer_class = ProductFeedbackSerializer


class UserRegistrationView(View):

    form_class = UserRegister
    template_name = 'registration/registration.html'
    #to diaply the blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit= False)

            #clean normailse the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password (password)
            user.save()

            #return user object if crententials are correct
            user = authenticate(username= username,password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form': form})


class UserLoginForm(View):

    Usermsg = ''
    form_class = UserLogin
    template_name = 'registration/login.html'

    #to diaply the blank form
    def get(self,request):
        #print("------>>>>>", request.session.items())
        if bool(request.session.items()) == False:

            if request.path == '/logout/':
                print ("logging out")
                logout_msg = True
                print (logout_msg)
            else:
                logout_msg = False
            request.session.flush()
            form = self.form_class(None)
            return render(request, self.template_name, {'form':form, 'logout_msg':logout_msg})
        else:
            print(" -->> Redirecting to home as already we have logged in")
            return redirect('/home')


    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #clean normailse the data
            username = form.login(request)
            if username is not None:
                if username.is_active:
                    login(request,username)
                    request.session['username'] = username.username
                    request.session['firstname'] = username.first_name
                    return redirect('/home')
            else:
                Usermsg = "In-correct login details"
        else:
            print ("Not a valid form")
        return render(request,
                      self.template_name, {'form': form,
                                            'login_message': "Invalid login credentials",
                                          })


@csrf_exempt
def logout(request):
    request.session.flush()
    return render_to_response('registration/logout.html', locals())


# Create your views here.
@csrf_exempt
def home(request):
    if 'username' in request.session:
        # This is capture product categories
        type_col = [prod_type.name.title() for prod_type in
                    ProductType._meta.get_fields() if prod_type.name != 'id']

        prod_catogeries = ProductType.objects.values()

        return render_to_response('index.html', locals())
    else:
        return redirect('/login', locals())


# Create a index page
def product_info(request):
    product_col = [product.name.title() for product in ProductInfo._meta.get_fields()]
    product_data = ProductInfo.objects.values()

    # This is capture product categories
    type_col = [prod_type.name.title() for prod_type in
                ProductType._meta.get_fields() if prod_type.name != 'id']

    prod_catogeries = ProductType.objects.values()



    return render_to_response('product.html', locals())


def production_product_info(request):
    production_product_col = \
        [prod_product.name.title() for prod_product in
         ProductionProductInfo._meta.get_fields()]


    prod_product_data = ProductionProductInfo.objects.values()

    return render_to_response('production_products.html', locals())

