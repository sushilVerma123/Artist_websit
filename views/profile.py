from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.customer import Customer
from message.models.form import Add_form
from message.models.profile import Profile
from message.models.project_list import Project_list


class Profiles(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists = Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        form = Add_form()
        data = {
            'categories': categories,
            'email': request.session.get('email'),
            'form': form,
            'profile': profile,
            'customer': Customer.objects.all(),
            'project_lists': project_lists

        }
        return render(request, 'profile_form.html', data)

    def post(self, request):
        form = Add_form(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer_id = request.session.get('customer_id')
            obj.save()
            messages.success(request, 'File upload successful')
            return redirect('homepage')
        else:
            return redirect('profile')

# <h5 class="my-3">{{profile|get_username:customer}}</h5>
