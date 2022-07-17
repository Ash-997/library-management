from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Book
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer_lab, RegisterSerializer_lab, UserSerializer,RegisterSerializer_memeber,Bookserializers,Bookserializers_member
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Create your views here.

def home(request):
    books = Book.objects.all()
    context = {'Books':books}
    return render(request,'home.html',context=context)

def sign_in(request):
    return render(request,'sign_in.html')

def sign_in_lib(request):
    return render(request,'sign_in_lib_form.html')

def sign_in_mem(request):
    return render(request,'sign_in_mem_form.html')

def sign_up(request):
    return render(request,'sign_up.html')

def sign_up_lib(request):
    return render(request,'sign_up_labr_form.html')

def sign_up_mem(request):
    return render(request,'sign_up_mem_form.html')

def create_lab_user(request):
    username = request.POST.get("lib_user_name")
    password = request.POST.get("lib_password")
    user = User.objects.create_user(username=username,password=password,is_staff=True)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    print(username)
    print(password)
    return HttpResponseRedirect(reverse('library_app:home'))


def signing_in_labrarian(request):
    username = request.POST.get("l_name")
    password = request.POST.get("l_pass")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_staff == True:
             login(request, user)
        else:
            return HttpResponse("invalid credentials")
    else:
        return HttpResponse("invalid credentials")
    return HttpResponseRedirect(reverse('library_app:home'))


def create_mem_user(request):
    username = request.POST.get("m_name")
    password = request.POST.get("m_pass")
    user = User.objects.create_user(username=username,password=password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    print(username)
    print(password)
    return HttpResponseRedirect(reverse('library_app:home'))

def signing_in_mem(request):
    username = request.POST.get("m_name")
    password = request.POST.get("m_pass")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_staff == False:
        
            login(request, user)
        else:
            return HttpResponse("invalid credentials")
    else:
        return HttpResponse("invalid credentials")
    return HttpResponseRedirect(reverse('library_app:home'))


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('library_app:home'))



def borrow(request,id):
    current_user = request.user
    book = Book.objects.get(id=id)
    cu = str(current_user)
    print(cu)
    book.status = cu
    book.save()
    return HttpResponseRedirect(reverse('library_app:home'))

def my_account(request):
    current_user = request.user
    book = Book.objects.filter(status=current_user.username)
    context = {'Books':book}
    return render(request,'my_books.html',context=context)



def book_return(request,id):
    book = Book.objects.get(id=id)
    book.status = None
    book.save()
    return HttpResponseRedirect(reverse('library_app:my_account'))


def acc_del(request):
    current_user = request.user
    current_user.delete()
    return HttpResponseRedirect(reverse('library_app:home'))


def lab_my_account(request):
    return render(request,'lab_account.html')

def manage_books(request):
    book = Book.objects.all()
    context = {'books':book}
    return render(request,'manage_books.html',context=context)

def add_book(request):
    return render(request,'add_book.html')

def add_book_in_db(request):
    book_name = request.POST.get("book_name")
    book_auth_name = request.POST.get("book_auth_name")
    book = Book(name=book_name,author=book_auth_name)
    book.save()
    return HttpResponseRedirect(reverse('library_app:manage_books'))

def edit_book(request,id):
    book = Book.objects.get(id=id)
    context = {'book_data':book}
    return render(request,'edit_book.html',context=context)

def store_edited_book(request,id):
    book_name = request.POST.get("book_name")
    book_auth_name = request.POST.get("book_auth_name")
    book = Book.objects.get(id=id)
    book.name = book_name
    book.author = book_auth_name
    book.save()
    return HttpResponseRedirect(reverse('library_app:manage_books'))

def del_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('library_app:manage_books'))


def manage_users(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request,'manage_users.html',context=context)

def add_user(request):
    return render(request,'add_users.html')


def add_user_in_db(request):
     username = request.POST.get("user_name")
     password = request.POST.get("user_password")
     user = User.objects.create_user(username=username,password=password)
     user.save()
     return HttpResponseRedirect(reverse('library_app:manage_users'))


def edit_user(request,id):
    user = User.objects.get(id=id)
    context = {'user_data':user}
    return render(request,'edit_user.html',context=context)


def store_edited_user(request,id):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.get(id=id)
    
    books = Book.objects.filter(status=user.username)
    for book in books:
        book.status = username
        book.save()
    user.username = username
    user.password = password
    user.save()
    return HttpResponseRedirect(reverse('library_app:manage_users'))
    
def del_user(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('library_app:manage_users'))

#Register API for librarian
class RegisterApi_lab(generics.GenericAPIView):
    serializer_class = RegisterSerializer_lab
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

#Register API for member
class RegisterApi_member(generics.GenericAPIView):
    serializer_class = RegisterSerializer_memeber
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


# for add , edit , delete books
class Bookviewset(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = Bookserializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

# for add , edit , delete user
class Userviewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]



#borrow book api
class Bookviewset_member(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = Bookserializers_member

    
    def put(self, request,id, *args,  **kwargs):
        
        book = Book.objects.get(id=id)
        if book == None:
            return Response({ "message": "book not exist", })
        user = request.data
        print(user['status'])
        vef_user= None
        try:
            vef_user = User.objects.get(username=user['status'])
        except:
            pass
        if vef_user:
            if book.status == None:
                if vef_user.is_staff == False:
                    book.status = str(user['status'])
                    book.save()
                    return Response({ "message": "updated", })
                else:
                    return Response({"message": "action can only performed by member user",})
            else:
                return Response({"message": "book is alread borrowed",})
        else:
            return Response({"message": "user does not exist",})

        
# get all books as a member
class Bookviewset_all_book(viewsets.ReadOnlyModelViewSet):

    queryset = Book.objects.all()
    serializer_class = Bookserializers
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]        
    
        
# return a book        
class Bookviewset_return(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = Bookserializers_member

    
    def put(self, request,id, *args,  **kwargs):
        
        book = Book.objects.get(id=id)
        if book == None:
            return Response({ "message": "book not exist", })
        user = request.data
        print(user['status'])
        vef_user= None
        try:
            vef_user = User.objects.get(username=user['status'])
        except:
            pass
        if vef_user:
            if str(book.status) == str(vef_user):
                if vef_user.is_staff == False:
                    book.status = None
                    book.save()
                    return Response({ "message": "return successful", })
                else:
                    return Response({"message": "action can only performed by member user",})
            else:
                return Response({"message": "book is not owned by you",})
        else:
            return Response({"message": "user does not exist",})   

