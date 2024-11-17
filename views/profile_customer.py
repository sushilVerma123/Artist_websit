from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.customer import Customer
from store.models.save import Save
from store.models.like import Like
from message.models.profile import Profile
from message.models.project_list import Project_list

class Profile_customer(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        profile_customer_id = str(request.get_full_path).split("?")[-1].split("'>>")[0]
        customer_profile= Profile.get_all_details(customer_id=profile_customer_id)
        project_lists = Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        data = {
            'categories': categories,
            'email': request.session.get('email'),
            'customer': Customer.objects.all(),
            'customer_profile': customer_profile,
            'profile': profile,
            'project_lists':project_lists,
        }
        return render(request, 'profile_customer.html', data)

