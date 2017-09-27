import arrow

from magazines.models import Purchase


def subscription_created(sender, **kwargs):
    ipn_obj = sender
    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    Purchase.objects.create(magazine_id=magazine_id, user_id=user_id, subscription_end=arrow.now().replace(weeks=+4).datetime)


def subscription_was_cancelled(sender, **kwargs):
    ipn_obj = sender
    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    purchase = Purchase.objects.get(user_id=user_id, magazine_id=magazine_id)
    purchase.subscription_end = arrow.now().datetime
    purchase.save()
