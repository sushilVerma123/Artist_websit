from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from store.models.products import Products
from store.models.customer import Customer
from store.models.save import Save
from store.models.like import Like
from message.models.profile import Profile
from message.models.project_list import Project_list
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Homepage(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        categoriesid = request.GET.get('categories')
        search_str = request.GET.get('search')
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        project_lists = Project_list.objects.filter(checkpoint=True).order_by('-datetime')

        extra_message = ""
        if search_str is not None:
            products = Products.get_products_by_titile_name(search_str).order_by('-datetime')
            if len(products) == 0:
                extra_message = 'No product found'
            else:
                extra_message = search_str
        elif categoriesid:
            products = Products.get_all_products_by_categoryid(categoriesid).order_by('-datetime')
            extra_message = Categories.objects.filter(id=categoriesid)[0]
        else:
            products = Products.get_all_products().order_by('-datetime')

        get_bookmark_product = Save.get_save_product_of_customer(customer_id)
        get_like_product = Like.get_like_product_of_customer(customer_id)

        # pagination
        p = Paginator(products, 20)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)

        data = {
            'products': products,
            'categories': categories,
            'email': request.session.get('email'),
            'customer': Customer.objects.all(),
            'get_bookmark_product': get_bookmark_product,
            'get_like_product': get_like_product,
            'extra_message': extra_message,
            'profile': profile,
            'project_lists': project_lists,
            'page_obj': page_obj,

        }
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
        return render(request, 'homepage.html', data)

    def post(self, request):
        bookmark_product_id = request.POST.get("bookmark")
        like_product_id = request.POST.get('like')
        # customer_id = request.POST.get('product_customer_id')
        customer_id = request.session.get('customer_id')
        if bookmark_product_id is not None and customer_id is not None:
            if len(Save.check_product_already_save(customer_id, bookmark_product_id)) == 0:
                bookmark = Save(save_product_id=bookmark_product_id, save_customer_id=customer_id)
                bookmark.save()
            else:
                save = Save.objects.filter(save_product_id=bookmark_product_id)
                save.delete()

        if like_product_id is not None and customer_id is not None:
            if len(Like.check_product_already_like(customer_id, like_product_id)) == 0:
                likes = Like(like_product_id=like_product_id, lke_customer_id=customer_id)
                likes.save()
            else:
                like = Like.objects.filter(like_product_id=like_product_id)
                like.delete()

        return redirect('homepage', )
