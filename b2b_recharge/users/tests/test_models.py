from django.test import TestCase
from users.models import Seller


class SellerModelTest(TestCase):

    def setUp(self):
        self.seller1 = Seller.objects.create(name="Seller 1", credit=0)
        self.seller2 = Seller.objects.create(name="Seller 2", credit=0)

    def test_increase_credit(self):
        for _ in range(10):
            self.seller1.increase_credit(100)
        self.assertEqual(self.seller1.credit, 1000)

    def test_decrease_credit(self):
        self.seller1.increase_credit(1000)
        for _ in range(10):
            self.seller1.decrease_credit(100)
        self.assertEqual(self.seller1.credit, 0)

    def test_insufficient_credit(self):
        self.seller1.increase_credit(500)
        with self.assertRaises(ValueError):
            self.seller1.decrease_credit(1000)

    def test_multiple_sellers(self):
        self.seller1.increase_credit(500)
        self.seller2.increase_credit(1000)
        self.assertEqual(self.seller1.credit, 500)
        self.assertEqual(self.seller2.credit, 1000)