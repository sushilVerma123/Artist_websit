from django.views import View
from django.shortcuts import render, redirect
from store.models.products import Products
from store.models.categories import Categories
from message.models.profile import Profile
from store.models.customer import Customer
from message.models.project_list import Project_list

class Cart(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        cart = request.session.get('cart')
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists = Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        if not cart:
            request.session['cart'] = {}

        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        cart_detail = {
            'products': products,
            'categories': categories,
            'email': request.session.get('email'),
            'profile': profile,
            'customer': Customer.objects.all(),
            'project_lists':project_lists,
        }
        return render(request, 'cart.html', cart_detail)

    def post(self, request):
        product = request.POST.get('product_id')
        cart = request.session.get('cart')
        cart.pop(product)
        request.session['cart'] = cart
        return redirect('cart')
