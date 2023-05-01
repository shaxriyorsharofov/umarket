from django.utils.text import slugify


def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()
