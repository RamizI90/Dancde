from django.test import TestCase

# Create your tests here.


class TestMonth(TestCase):

    def test_index(self):
        response = self.client.get('/months/')
        self.assertEqual(response.status_code, 200)

    def test_march(self):
        response = self.client.get('/months/March')
        self.assertEqual(response.status_code, 301)
        self.assertIn('<месяц март 31 день', response.content.decode())
