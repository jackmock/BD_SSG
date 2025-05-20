import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_1(self):
        node = HTMLNode("This is a text node", TextType.BOLD)
    
    def test_props_2(self):
        node = TextNode("This is a text node", TextType.BOLD)

    def test_props_3(self):
        node = TextNode("This is a text node", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()