import unittest
from app import app
class PortfolioTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_all_pages(self):
        for path in ["/", "/about", "/skills", "/projects", "/photography", "/journey", "/contact", "/resume"]:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 200)
    def test_contact_address(self):
        response = self.client.get("/contact").get_data(as_text=True)
        self.assertIn("58, Ranganathan Street, Podaturpet", response)
        self.assertNotIn("bala@example.com", response)
    def test_identity(self):
        text = self.client.get("/about").get_data(as_text=True)
        self.assertIn("BALASUBRAMANIAM", text)
        self.assertIn("BALA", text)
    def test_gallery_filter(self):
        page = self.client.get("/photography?category=Landscape").get_data(as_text=True)
        self.assertIn("A little closer to the sky", page)
        self.assertNotIn("After the rain", page)
    def test_invalid_pages(self):
        for path in ["/photo/20", "/project/20", "/unknown"]:
            self.assertEqual(self.client.get(path).status_code, 404)
        self.assertEqual(self.client.get("/photography?category=unknown").status_code, 400)
    def test_detail_pages(self):
        for path in ["/project/0", "/project/1", "/project/2", "/photo/0", "/photo/1", "/photo/2", "/photo/3"]:
            self.assertEqual(self.client.get(path).status_code, 200)
if __name__ == "__main__":
    unittest.main()
