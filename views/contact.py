from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from message.models.contact import Contact
from message.models.profile import Profile
from store.models.customer import Customer
from message.models.project_list import Project_list

class Contacts(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists = Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        data = {
            'email': request.session.get('email'),
            "categories": categories,
            'profile': profile,
            'customer': Customer.objects.all(),
            'project_lists':project_lists
        }
        return render(request, "contact.html", data)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_box = Contact(user_name=username, email=email, user_messages=message)
        contact_box.register()
        return redirect('contacts')
