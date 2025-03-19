import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_child(self):
        with self.assertRaises(ValueError) as context:
            LeafNode(tag="h1",value="Bob",children=["George","Karla"])
        self.assertEqual(str(context.exception), "LeafNode cannot have children")

    def test_noValue(self):
        testNode = LeafNode(tag="p",props=None)
        with self.assertRaises(ValueError) as context:
            testNode.to_html()
        self.assertEqual(str(context.exception), "LeafNode must have a value")

    def test_noTag(self):
        testNode = LeafNode(value="This is a test",props={"No": "Yes"})
        testResult = testNode.to_html()
        testExpected = "This is a test"
        self.assertEqual(testResult, testExpected)

    def test_ValTag(self):
        testNode = LeafNode(tag="b",value="This is a test")
        testResult = testNode.to_html()
        testExpected = "<b>This is a test</b>"
        self.assertEqual(testResult, testExpected)

    def test_ValTagProp(self):
        testNode = LeafNode(tag="b",value="This is a test",props={"No": "Yes"})
        testResult = testNode.to_html()
        testExpected = '<b No="Yes">This is a test</b>'
        self.assertEqual(testResult, testExpected)

    def test_ValTagProps(self):
        testNode = LeafNode(tag="b",value="This is a test",props={"No": "Yes","Maybe": "Baby"})
        testResult = testNode.to_html()
        testExpected = '<b No="Yes" Maybe="Baby">This is a test</b>'
        self.assertEqual(testResult, testExpected)


if __name__ == "__main__":
    unittest.main()
