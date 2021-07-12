from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class SnackTests(TestCase):
    def test_snack_list_status_code(self):
        url = reverse('snack')
        actual_status_code = self.client.get(url).status_code
        expected_status_code = 200
        self.assertEqual(actual_status_code,expected_status_code)



    def test_snack_list_template(self):
            url = reverse('snack')
            response = self.client.get(url)
            actual = 'snack_list.html'
            self.assertTemplateUsed(response, actual)
