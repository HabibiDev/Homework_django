from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import *
# Create your tests here.


class DishTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.ingredient_1 = Ingredient.objects.create(
            name='Ингредиент№1', weight=500)
        cls.ingredient_2 = Ingredient.objects.create(
            name='Ингредиент№2', weight=500)
        cls.dish_1 = Dish.objects.create(title='dish1', description='description1', )
        cls.dish.ingredient.set([cls.ingredient_1, cls.ingredient_2])

    def test_order_add(self):
        count
        o = Order.objects.create(
            dish=self.dish_1, content='content', category=self.category)
        post_list_url = reverse('posts:post_list')
        r = self.client.get(post_list_url)
        print(r.context)
        self.assertEquals(r.status_code, 200)
        self.assertEquals(len(r.context['post_list']), 1)

    def test_post_add(self):
        post_params = {'title': 'title2',
                       'content': 'content2', 'category': self.category}
        count_posts = Post.objects.count()
        self.client.post('posts:add_post', data=post_params)
        self.assertEquals(Post.objects.count(), count_posts + 1)
