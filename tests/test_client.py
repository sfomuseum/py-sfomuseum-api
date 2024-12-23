import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from sfomuseum.api.client import OAuth2Client

class TestClient(unittest.TestCase):

    def test_client(self):
        token = "TOKEN"
        cl = OAuth2Client(token)
        self.assertIsInstance(cl, OAuth2Client)

if __name__ == "__main__":
    unittest.main()
