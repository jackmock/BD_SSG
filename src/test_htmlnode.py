import unittest

from htmlnode import *

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)
        
if __name__ == "__main__":
    unittest.main()