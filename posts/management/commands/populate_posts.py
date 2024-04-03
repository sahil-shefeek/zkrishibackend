import random
from django.core.management.base import BaseCommand
from posts.models import CommunityPost


class Command(BaseCommand):
    help = 'Populate CommunityPosts with mock data'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', type=int, default=10, help='Number of posts to add')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            username = f"User {i}"
            profile_picture_url = f"https://picsum.photos/id/{i}/200/300"  # Example profile picture URL
            caption = f"Caption {i}"
            CommunityPost.objects.create(username=username, profile_picture_url=profile_picture_url, caption=caption)
        self.stdout.write(self.style.SUCCESS(f'{count} mock posts added successfully'))
