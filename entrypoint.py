import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_service.settings")
django.setup()

from service.models import Post

posts = [
    {
        'author':'bill gates',
        'title':'Thank you for invite me!',
        'content':'Lorem ipsum dolor sit amet',
    },
    {
        'author':'steve jobs',
        'title':'Thank you for join us!',
        'content':'consectetur adipiscing elit. Nullam luctus tincidunt quam in eleifend.',
    }
]

post_list = [Post(**post_dict) for post_dict in posts]
Post.objects.bulk_create(post_list)
