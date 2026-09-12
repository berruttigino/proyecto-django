from django.test import TestCase
from django.urls import reverse
from .models import Author, Post
from .forms import PostSearchForm


class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='María', email='maria@test.com')

    def test_post_str_and_creation(self):
        post = Post.objects.create(
            title='Post de prueba',
            content='Contenido de prueba',
            author=self.author,
            publicado=True
        )
        self.assertEqual(Post.objects.count(), 1)
        self.assertTrue(post.publicado)


class PostSearchFormTest(TestCase):
    def test_form_valid_with_empty_query(self):
        form = PostSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_form_valid_with_query(self):
        form = PostSearchForm(data={'q': 'django'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['q'], 'django')


class PostListViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='María', email='maria@test.com')
        Post.objects.create(
            title='Introducción a Django',
            content='Contenido sobre Django',
            author=self.author,
            publicado=True
        )
        Post.objects.create(
            title='Tips de CSS',
            content='Contenido sobre CSS',
            author=self.author,
            publicado=True
        )
        Post.objects.create(
            title='Post sin publicar',
            content='No debería aparecer',
            author=self.author,
            publicado=False
        )

    def test_list_view_status_code(self):
        response = self.client.get(reverse('core:post-list'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_shows_only_published(self):
        response = self.client.get(reverse('core:post-list'))
        self.assertEqual(len(response.context['posts']), 2)

    def test_search_filters_by_title(self):
        response = self.client.get(reverse('core:post-list'), {'q': 'Django'})
        posts = response.context['posts']
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, 'Introducción a Django')

    def test_search_no_results(self):
        response = self.client.get(reverse('core:post-list'), {'q': 'inexistente'})
        self.assertEqual(len(response.context['posts']), 0)