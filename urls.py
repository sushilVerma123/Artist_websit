# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from store.views.homepage import Homepage
from store.views.sign_up import Sign_up
from store.views.sign_in import Sign_in
from store.views.sign_out import Sign_out
from store.views.otp import Otp
from store.views.post import Post
from store.views.add import Add
from store.views.about import About
from store.views.contact import Contacts
from message.views.chat import Chat
from store.views.cart import Cart
from store.views.full_productt_page import Full_product_page
from store.views.profile import Profiles
from store.views.profile_customer import Profile_customer
from store.views.project_listing import Project_listing
from store.views.project_list_me import Project_list_me
from store.middleware.auth import auth_middleware

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('sign-up', Sign_up.as_view(), name='signup'),
    path('sign-in', Sign_in.as_view(), name='signin'),
    path('sign-out', Sign_out.as_view(), name='signout'),
    path('post', auth_middleware(Post.as_view()), name='post'),
    path('add', auth_middleware(Add.as_view()), name='add'),
    path('otp', auth_middleware(Otp.as_view()), name='otp'),
    path('chat', auth_middleware(Chat.as_view()), name='chat'),
    path('about', About.as_view(), name='about'),
    path('contact', Contacts.as_view(), name='contacts'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('product_page', Full_product_page.as_view(), name='productpage'),
    path('profile_page', auth_middleware(Profiles.as_view()), name="profile"),
    path('project_listing', auth_middleware(Project_listing.as_view()), name="project_listing"),
    path('profile_customer', auth_middleware(Profile_customer.as_view()), name="customer_profile"),
    path('project_list_me', auth_middleware(Project_list_me.as_view()), name="project_list_me")

]
