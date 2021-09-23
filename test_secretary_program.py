import unittest
from unittest.mock import patch
from main import check_document_existance, get_doc_owner_name, add_new_shelf, delete_doc, get_doc_shelf, add_new_doc


class TestSecretaryUnitTest(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_check_document_existance(self):
        self.assertEqual(True, check_document_existance("2207 876234"), msg="значение False")

    @patch("builtins.input", return_value='10006')
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual("Аристарх Павлов", get_doc_owner_name())

    def test_add_new_shelf(self):
        self.assertEqual(("4", True), add_new_shelf("4"))

    def test_add_new_shelf_exist(self):
        self.assertEqual(("3", False), add_new_shelf("3"))

    @patch("builtins.input", return_value='11-2')
    def test_delete_doc(self, mock_input):
        self.assertEqual(("11-2", True), delete_doc())

    @patch("builtins.input", return_value="10006")
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual("2", get_doc_shelf())

    @patch("builtins.input", return_value="3")
    @patch("builtins.input", return_value="Andrey")
    @patch("builtins.input", return_value="license")
    @patch("builtins.input", return_value="123")
    def test_add_new_doc(self, *args):
        self.assertEqual("3", add_new_doc())
