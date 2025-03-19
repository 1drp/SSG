import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        testNode = HTMLNode()
        with self.assertRaises(NotImplementedError):
            testNode.to_html()

    def test_0Prop(self):
        testNode = HTMLNode(tag="p",value="test")
        testProps = testNode.props_to_html()
        testResult = ""
        self.assertEqual(testProps, testResult)

    def test_1Prop(self):
        testNode = HTMLNode(props={"href": "thing.place"})
        testProps = testNode.props_to_html()
        testResult = ' href="thing.place"'
        self.assertEqual(testProps, testResult)

    def test_2Prop(self):
        testNode = HTMLNode(props={"href": "thing.place", "alpha": "beta"})
        testProps = testNode.props_to_html()
        testResult = ' href="thing.place" alpha="beta"'
        self.assertEqual(testProps, testResult)

if __name__ == "__main__":
    unittest.main()
