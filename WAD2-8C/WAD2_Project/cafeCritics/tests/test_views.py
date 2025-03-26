from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from cafeCritics.models import Cafe, Drink, UserProfile, Review
from django.contrib.auth.forms import PasswordChangeForm
from cafeCritics.forms import UserUpdateForm

#class UserAuthTests(TestCase):
#    def test_login_view(self):
#        User.objects.create_user(username='testuser', password='12345')
#        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
#        self.assertRedirects(response, expected_url=reverse('home_page'), status_code=302, target_status_code=200)
#
#    def test_logout_view(self):
#        response = self.client.get(reverse('logout'))
#        self.assertRedirects(response, expected_url=reverse('login'))

# Tests for home_view
class HomeViewTests(TestCase):
    # Sets up test
    def setUp(self):
        Cafe.objects.create(name='testcafe1', location='testlocation1', owner=User.objects.create_user(username='testuser1', password='12345'), average_rating=2.5)
        Cafe.objects.create(name='testcafe2', location='testlocation2', owner=User.objects.create_user(username='testuser2', password='123456'), average_rating=5.0)
        Drink.objects.create(name='testdrink1', price=2.5, cafe=Cafe.objects.get(name='testcafe1'), rating=3)
        Drink.objects.create(name='testdrink2', price=4.5, cafe=Cafe.objects.get(name='testcafe2'), rating=5)

    # Tests home_view status code and template
    def test_home_view(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/home.html')

    # Tests home_view context and list ordering    
    def test_home_view_context(self):
        response = self.client.get(reverse('home_page'))
        self.assertIn('top_cafes', response.context)
        self.assertIn('top_drinks', response.context)
        self.assertEqual(len(response.context['top_cafes']), 2)
        self.assertEqual(len(response.context['top_drinks']), 2)
        self.assertTrue(response.context['top_cafes'][0].average_rating > response.context['top_cafes'][1].average_rating)
        self.assertTrue(response.context['top_drinks'][0].rating > response.context['top_drinks'][1].rating)

# Tests for cafes_view
class CafesViewTests(TestCase):
    # Sets up test
    def setUp(self):
        Cafe.objects.create(name='testcafe1', location='testlocation1', owner=User.objects.create_user(username='testuser1', password='12345'), average_rating=2.5)
        Cafe.objects.create(name='testcafe2', location='testlocation2', owner=User.objects.create_user(username='testuser2', password='12345'), average_rating=5.0)
        Cafe.objects.create(name='testcafe3', location='testlocation3', owner=User.objects.create_user(username='testuser3', password='12345'), average_rating=4.0)

    # Tests cafes_view status code and template
    def test_cafes_view(self):
        response = self.client.get(reverse('cafeCritics:cafes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cafes.html')

    # Tests cafes_view context
    def test_cafes_view_context(self):
        response = self.client.get(reverse('cafeCritics:cafes'))
        self.assertIn('cafes', response.context)
        self.assertEqual(len(response.context['cafes']), 3)

# Tests for about_view
class AboutViewTests(TestCase):
    # Tests about_view status code and template
    def test_about_view(self):
        response = self.client.get(reverse('cafeCritics:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

# Tests for review_view
class ReviewViewTests(TestCase):
    # Sets up test
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cafe = Cafe.objects.create(name='testcafe', location='testlocation', owner=self.user, average_rating=4.0, slug='testcafe')
        #self.url = reverse('cafeCritics:review', kwargs={'cafe_name_slug': self.cafe.slug})

    # Tests review_view status code, template, form
    def test_review_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('cafeCritics:review', kwargs={'cafe_name_slug': self.cafe.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        self.assertContains(response, '<form')

    # Tests review_view form submission
    def test_review_view_submission(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('cafeCritics:review', kwargs={'cafe_name_slug': self.cafe.slug}),
                                    {'text': 'Amazing!', 'rating': 4})
        review = Review.objects.get(user=self.user, cafe=self.cafe)
        self.assertEqual(review.text, 'Amazing!')
        self.assertEqual(review.rating, 4)
        self.assertRedirects(response, reverse('cafeCritics:show_cafe', kwargs={'cafe_name_slug': self.cafe.slug}))

# Tests for show_cafe
class ShowCafeTests(TestCase):
    # Sets up test
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cafe = Cafe.objects.create(name='testcafe', location='testlocation', owner=self.user, average_rating=4.0, slug='testcafe')
        self.drink = Drink.objects.create(name='testdrink1', price=2.5, cafe=self.cafe, rating=3)
        self.review = Review.objects.create(user=self.user, cafe=self.cafe, rating=4)

    # Tests show_cafe status code and template
    def test_show_cafe(self):
        response = self.client.get(reverse('cafeCritics:show_cafe', kwargs={'cafe_name_slug': self.cafe.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cafe.html')

    # Tests show_cafe context
    def test_show_cafe_context(self):
        response = self.client.get(reverse('cafeCritics:show_cafe', kwargs={'cafe_name_slug': self.cafe.slug}))
        self.assertIn('cafe', response.context)
        self.assertIn('drinks', response.context)
        self.assertIn('reviews', response.context)
        self.assertEqual(response.context['cafe'], self.cafe)
        self.assertEqual(len(response.context['drinks']), 1)
        self.assertEqual(len(response.context['reviews']), 1)

# Tests for show_drinks
class ShowDrinksTests(TestCase):
    # Sets up test
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.cafe = Cafe.objects.create(name='testcafe', location='testlocation', owner=self.user, average_rating=4.0, slug='testcafe')
        self.drink = Drink.objects.create(name='testdrink1', price=2.5, cafe=self.cafe, rating=3)
        self.drink = Drink.objects.create(name='testdrink2', price=1.5, cafe=self.cafe, rating=4)

    # Tests show_drinks status code and template
    def test_show_cafe(self):
        response = self.client.get(reverse('cafeCritics:show_drinks', kwargs={'cafe_name_slug': self.cafe.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drinks.html')

    # Tests show_drinks context
    def test_show_cafe_context(self):
        response = self.client.get(reverse('cafeCritics:show_drinks', kwargs={'cafe_name_slug': self.cafe.slug}))
        self.assertIn('cafe', response.context)
        self.assertIn('drinks', response.context)
        self.assertEqual(response.context['cafe'], self.cafe)
        self.assertEqual(len(response.context['drinks']), 2)


