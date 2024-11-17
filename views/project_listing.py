from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from message.models.profile import Profile
from store.models.customer import Customer
from message.models.project_list import Project_list


class Project_listing(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists=Project_list.objects.filter(checkpoint=True).order_by('-datetime')
        data = {
            'email': request.session.get('email'),
            "categories": categories,
            'profile': profile,
            'customer': Customer.objects.all(),
            'project_lists':project_lists
        }
        return render(request, "project_listing.html", data)

    def post(self, request):
        project_title = request.POST.get('project_title')
        project_email = request.POST.get('project_email')
        project_description = request.POST.get("project_description")
        customer_id = request.session.get('customer_id')
        project = Project_list(title=project_title, email=project_email, description=project_description,
                               customer=Customer(id=customer_id))
        project.save()
        return redirect('project_listing')
