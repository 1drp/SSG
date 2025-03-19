import unittest
from testVariables import *
from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equrlnone(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_equrl(self):
        node = TextNode("This is a text node", TextType.BOLD, "thing.place")
        node2 = TextNode("This is a text node", TextType.BOLD, "thing.place")
        self.assertEqual(node, node2)

    def test_1neq(self):
        node = TextNode("This is a text node.", TextType.BOLD, "thing.place")
        node2 = TextNode("This is a text node", TextType.BOLD, "thing.place")
        self.assertNotEqual(node, node2)

    def test_2neq(self):
        node = TextNode("This is a text node", TextType.BOLD, "thing.place")
        node2 = TextNode("This is a text node", TextType.ITALIC, "thing.place")
        self.assertNotEqual(node, node2)
    
    def test_3neq(self):
        node = TextNode("This is a text node", TextType.BOLD, "thing.place")
        node2 = TextNode("This is a text node", TextType.BOLD, "thing.other")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = tT1
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Fourscore and seven")

    def test_bold(self):
        node = tB1
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Fourscore and seven")

    def test_italic(self):
        node = tI1
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Fourscore and seven")
    
    def test_code(self):
        node = tC1
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Fourscore and seven")

    def test_link(self):
        node = tL3
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Don't panic.")
        self.assertEqual(html_node.props, {"href": "place.thing"})

    def test_image(self):
        node = tM3
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "place.thing", "alt": "Don't panic."})


if __name__ == "__main__":
    unittest.main()
