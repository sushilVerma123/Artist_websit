from django.db import models
from store.models.customer import Customer
# from phone_field import PhoneField
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ("Female", 'Female'),
        ("Not Specified", 'Not Specified'),
    )
    full_name = models.CharField(max_length=50, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default="", null=True, blank=True)
    image = models.ImageField(upload_to='profile', null=True, blank=True, default='profile/person_icon.jpg')
    gender = models.CharField(choices=GENDER_CHOICES, default="Not Specified", max_length=20)
    mobile = models.IntegerField(default=0, null=True, blank=True,
                                 validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    address = models.CharField(max_length=500, default="", null=True, blank=True)
    instagram = models.URLField(max_length=500, null=True, blank=True)
    twitter = models.URLField(max_length=500, null=True, blank=True)
    facebook = models.URLField(max_length=500, null=True, blank=True)
    linkedin = models.URLField(max_length=500, null=True, blank=True)

    @staticmethod
    def get_all_details(customer_id):
        profile = Profile.objects.filter(customer=customer_id)
        if len(profile):
            return profile[0]
        else:
            return profile
