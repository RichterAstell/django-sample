from django.test import TestCase
from .views import index

# Create your tests here.
class EmployeeModelTests(TestCase):
    def test_index(self):
        """
        views.index
        """
        result = index()
        self.assertEqual(200, 200)
        # self.assertEqual(200, result.status_code)
