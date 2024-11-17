from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from message.models.profile import Profile
from store.models.customer import Customer
from message.models.project_list import Project_list


class Project_list_me(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists = Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        my_project_lists = Project_list.objects.filter(customer_id=customer_id).order_by('-datetime')
        data = {
            'email': request.session.get('email'),
            "categories": categories,
            'profile': profile,
            'customer': Customer.objects.all(),
            'project_lists': project_lists,
            'my_project_lists': my_project_lists
        }
        return render(request, "project_list_me.html", data)

    def post(self, request):
        close_project_id = request.POST.get('close_project')
        project = Project_list.objects.get(id=close_project_id)
        project.checkpoint = False
        project.save()
        return redirect('project_list_me')
