from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CreateRecord # Import your model
from django.db.transaction import on_commit

@receiver([post_save, post_delete], sender=CreateRecord)
def invalidate_my_model_cache(sender, instance, **kwargs):
    def _clear():
        print("deleting home_view cache after commit")
        cache.delete_pattern('*home_view*')

    on_commit(_clear)
