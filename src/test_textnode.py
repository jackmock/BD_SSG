import unittest

from textnode import*

import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "boot.dev")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def split_test_1_delimiter(self):
        nodes = [TextNode("Look, `code` lives here!", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [TextNode("Look, ", TextType.TEXT), TextNode("code", TextType.CODE), TextNode(" lives here!", TextType.TEXT)])

    def split_test_2_delimiters(self):
        nodes = [TextNode("First `block` then `second`.", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [TextNode("First ", ...), TextNode("block", ...), ..., TextNode("second", ...), ...])

    def split_test_no_delimiters(self):
        nodes = [TextNode("Nothing special here.", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [TextNode("Nothing special here.", TextType.TEXT)])

    def split_test_unmatched_delimiter(self):
        nodes = [TextNode("Oh no, this is `not closed!", TextType.TEXT)]
        self.assertRaises(Exception)
    
    def split_test_non_text_type(self):
        bold_node = TextNode("I am bold!", TextType.BOLD)
        nodes = [bold_node]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [bold_node])
    

if __name__ == "__main__":
    unittest.main()