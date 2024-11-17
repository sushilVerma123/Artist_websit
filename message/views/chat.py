from django.views import View
from django.shortcuts import render, redirect
from store.models.categories import Categories
from message.models.profile import Profile
from store.models.customer import Customer
from django.urls import reverse
from message.models.chat_message import ChatMessage
class Chat(View):
    def get(self, request):
        categories = Categories.get_all_categories()
        customer_id = request.session.get('customer_id')
        profile = Profile.get_all_details(customer_id)
        search_name=request.GET.get('search_name')
        all_profile_image = Profile.objects.only('image','customer')
        receiver_id=request.GET.get('receiver_id')
        chat_nav_info=Profile.get_all_details(receiver_id)
        all_chat=ChatMessage.objects.filter(sender_id=customer_id) | ChatMessage.objects.filter(receiver_id=customer_id)
        ordered_all_chat = all_chat.order_by('timestamp')
        # for i in ordered_all_chat:
        #     print(i)
        # print(type(receiver_id))
        if search_name is None:
            customer= Customer.objects.all()
        else:
            customer=Customer.objects.filter(username__icontains=search_name)
        chat_detail={
            'categories':categories,
            'customer_id':customer_id,
            'email':request.session.get('email'),
            'profile': profile,
            'customer': customer,
            'all_profile_image':all_profile_image,
            'receiver_id':receiver_id,
            'chat_nav_info':chat_nav_info,
            'ordered_all_chat':ordered_all_chat

        }
        return render(request, "chat.html", chat_detail)
    def post(self,request):
        sender_id = request.session.get('customer_id')
        receiver_id = request.GET.get('receiver_id')
        message_content = request.POST.get('text_message')
        if sender_id and receiver_id and message_content:
            message = ChatMessage(sender=Customer(id=sender_id), receiver=Customer(id=receiver_id), message=message_content)
            message.save()
        redirect_url = reverse('chat') + f'?receiver_id={receiver_id}'
        return redirect(redirect_url)

