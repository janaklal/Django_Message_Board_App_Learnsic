from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.

class HelloHomePage(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/home/")
        self.assertAlmostEqual(response.status_code,200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("HomePage"))
        self.assertEqual(response.status_code,200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("HomePage"))
        self.assertTemplateUsed(response,"home.html")

    

class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/home/about/")
        self.assertEqual(response.status_code,200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("AboutPage"))
        self.assertEqual(response.status_code,200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("AboutPage"))
        self.assertTemplateUsed(response,"about.html")


