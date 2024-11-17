from django import template
from store.models.like import Like

register = template.Library()


@register.filter(name='username')
def username(product, customer):
    for i in customer:
        if product.customer_id == i.id:
            return i.username


@register.filter(name='change_bookmark_icon')
def change_bookmark_icon(product, get_bookmark_product):
    for i in get_bookmark_product:
        if int(i.save_product_id) == int(product.id):
            return True


@register.filter(name='change_like_icon')
def change_like_icon(product, get_like_product):
    for i in get_like_product:
        if i.like_product_id == int(product.id):
            return True


@register.filter(name='count_likes')
def count_likes(product):
    return len(Like.objects.filter(like_product_id=int(product.id)))


@register.filter(name="total_prices")
def total_prices(products):
    total = 0
    for i in products:
        total += i.prices
    return total


@register.filter(name="get_username")
def get_username(profile, customer):
    for i in customer:
        if profile.customer_id == i.id:
            return i.username


@register.filter(name="get_email")
def get_email(customer_profile, customer):
    for i in customer:
        if customer_profile.customer_id == i.id:
            return i.email


@register.filter('Count_project')
def Count_project(project_lists):
    if len(project_lists) == 0:
        return True
    else:
        return False

@register.filter('get_image_in_chat')
def get_image_in_chat(customer_model,all_profile_image):
    for i in all_profile_image:
        if customer_model.id==i.customer_id:
            return i.image

@register.filter(name="chat_username")
def chat_username(ids, customer):
    for i in customer:
        if int(ids) == i.id:
            return i.username
