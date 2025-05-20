import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_1(self):
        node = HTMLNode("a", "Google", None, {"href": "https://google.com"})
        expected_result = ' href="https://google.com"'
        self.assertEqual(expected_result, node.props_to_html())
    
    def test_props_2(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev"})
        expected_result = ' href="https://boot.dev"'
        self.assertEqual(expected_result, node.props_to_html())

    def test_props_3(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev"})
        expected_result_without_whitespace = 'href="https://boot.dev"'
        self.assertNotEqual(expected_result_without_whitespace, node.props_to_html())
        
if __name__ == "__main__":
    unittest.main()