from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import  Bookviewset, RegisterApi_lab,RegisterApi_member,Userviewset,Bookviewset_member,Bookviewset_all_book,Bookviewset_return


router = DefaultRouter()
router2= DefaultRouter()
router3= DefaultRouter()

router.register('bookdata',views.Bookviewset,basename='book')
router2.register('userdata',views.Userviewset,basename='user')
router3.register('all_book',views.Bookviewset_all_book,basename='all_book')
#router3.register('book_mem',views.Bookviewset_member,basename='book_mem')

#urlpatterns = router.urls
urlpatterns = [
    path('book/',include(router.urls)),
    path('user/',include(router2.urls)),
    path('books/',include(router3.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path("",views.home,name='home'),
    path("sign_in",views.sign_in,name='sign_in1'),
    path("sign_up",views.sign_up,name='sign_up1'),
    path("sign_in/librarian",views.sign_in_lib,name='librarian'),
    path("sign_in/member",views.sign_in_mem,name='member'),
    path("sign_up/librarian",views.sign_up_lib,name='librarian_sign_up'),
    path("sign_up/member",views.sign_up_mem,name='member_sign_up1'),
    path("create_librarian_user",views.create_lab_user,name='create_lab_user'),
    path("signing_in_lab",views.signing_in_labrarian,name='signing_in_l'),
    
    
    path("creating_memeber_user",views.create_mem_user,name='creating_mem_user'),
    path("signing_in_mem",views.signing_in_mem,name='signing_in_m'),

    path("log_out",views.log_out,name='log_out'),
    
    path("borrow/<int:id>",views.borrow,name='borrow'),
    path("my_account",views.my_account,name='my_account'),
    path("book_return/<int:id>",views.book_return,name='book_return'),
    path("myaccount/delete_account",views.acc_del,name='acc_del'),
    path("librarian_account",views.lab_my_account,name='lab_my_account'),
    path("librarian_account/manage_books",views.manage_books,name='manage_books'),
    path("librarian_account/manage_books/add_book",views.add_book,name='add_book'),
    path("librarian_account/manage_books/add_book/in_db",views.add_book_in_db,name='add_book_in_db'),
    path("librarian_account/manage_books/edit_book/<int:id>",views.edit_book,name='edit_book'),
    path("librarian_account/manage_books/edit_book/store_edited_book/<int:id>",views.store_edited_book,name='store_edited_book'),
    path("librarian_account/manage_books/delete_book/<int:id>",views.del_book,name='del_book'),
    
    

    path("librarian_account/manage_users",views.manage_users,name='manage_users'),
    path("librarian_account/manage_users/add_user",views.add_user,name='add_user'),
    path("librarian_account/manage_users/add_user_in_db",views.add_user_in_db,name='add_user_in_db'),
    path("librarian_account/manage_users/edit_user/<int:id>",views.edit_user,name='edit_user'),
    path("librarian_account/manage_users/edit_user/store_edited_user/<int:id>",views.store_edited_user,name='store_edited_user'),
    path("librarian_account/manage_users/del_user/<int:id>",views.del_user,name='del_user'),

    
    path('api/register_librarian', RegisterApi_lab.as_view()), # register labrarian
    path('api/register_member', RegisterApi_member.as_view()),  # register member
    path('api/borrow_book/<int:id>', Bookviewset_member.as_view()),   # borrow book as member
    path('api/return_book/<int:id>', Bookviewset_return.as_view()),   # return book as member
    #path('api/all_books', Bookviewset_member.as_view()),   # view all books as member
    
     
]
