from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.customer import Customer
from message.models.profile import Profile
import numbers
from message.models.project_list import Project_list


class Full_product_page(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        product_id = str(request.get_full_path).split("?")[-1].split("'>>")[0]
        product = Products.objects.filter(id=product_id)
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists =Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        data = {
            'email': request.session.get('email'),
            "categories": categories,
            "product": product[0],
            'customer': Customer.objects.all(),
            # 'category_id':category_id
            'profile': profile,
            'project_lists': project_lists
        }
        return render(request, "full_product_page.html", data)

    def post(self, request):
        productid = request.POST.get('productid')
        cart = request.session.get('cart')
        if productid:
            cart = request.session.get('cart')
            if cart:
                cart[productid] = 1
            else:
                cart = {}
                cart[productid] = 1
        request.session['cart'] = cart
        return redirect('cart')
