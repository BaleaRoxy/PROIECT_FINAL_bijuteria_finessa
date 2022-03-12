import stripe
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.conf import settings
from payments.utils import create_stripe_customer_model

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_stripe_customer(created, instance, **kwargs):
    if created:
        stripe_customer = stripe.Customer.create(
            email = instance.email,
            name = f'{ instance.first_name } {instance.last_name}',
            api_key=settings.STRIPE_SECRET_KEY
        )

        StripeCustomer.objects.create(user=instance, stripe_id=stripe_customer)