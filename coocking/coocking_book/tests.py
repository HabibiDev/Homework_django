from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import *
# Create your tests here.

class PostTestCase(TestCase):
	category_name = 'test_category'
	@classmethod
	def setUpClass(cls):
		super().setUpClass()
		cls.category = Category.objects.create(name=cls.category_name, is_active = True)


	def test_post_list(self):
		p = Post.objects.create(title='title', content = 'content', category = self.category)
		post_list_url = reverse('posts:post_list')
		r = self.client.get(post_list_url)
		print(r.context)
		self.assertEquals(r.status_code,200)
		self.assertEquals(len(r.context['post_list']),1)

	def test_post_add(self):
		post_params = {'title':'title2', 'content' : 'content2', 'category' : self.category}
		count_posts = Post.objects.count()
		self.client.post('posts:add_post', data = post_params)
		self.assertEquals(Post.objects.count(), count_posts + 1)