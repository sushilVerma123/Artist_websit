from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from message.models.profile import Profile
from store.models.customer import Customer
from message.models.project_list import Project_list

class About(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists =Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        data = {
            'email': request.session.get('email'),
            "categories": categories,
            'profile': profile,
            'customer': Customer.objects.all(),
            'project_lists' :project_lists
        }
        return render(request, "about.html", data)
