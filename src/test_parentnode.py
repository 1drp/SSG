import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from testVariables import *

class TestParentNode(unittest.TestCase):
    def test_Value(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(t2,v2,[cLv],p0)
        self.assertEqual(str(context.exception), "ParentNode cannot have a value")

    def test_noTag(self):
        testNode = ParentNode(t0,v0,[cLv],p0)
        with self.assertRaises(ValueError) as context:
            testNode.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")
    
    def test_noChild(self):
        testNode = ParentNode(t1,v0,c0,p0)
        with self.assertRaises(ValueError) as context:
            testNode.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_cPtc(self):
        testResult = cPtc.to_html()
        testExpected = "<p>Fourscore and seven</p>"
        self.assertEqual(testResult, testExpected)

    def test_cPtcp(self):
        testResult = cPtcp.to_html()
        testExpected = '<b href="place.thing"><b>Don\'t panic.</b></b>'
        self.assertEqual(testResult, testExpected)

    def test_cPtc2(self):
        testResult = cPtc2.to_html()
        testExpected = '<p><b>Don\'t panic.</b><b>Don\'t panic.</b></p>'
        self.assertEqual(testResult, testExpected)

    def test_cPtcP(self):
        testResult = cPtcP.to_html()
        testExpected = '<p><p>Fourscore and seven</p></p>'
        self.assertEqual(testResult, testExpected)

    def test_cPtc2P(self):
        testResult = cPtc2P.to_html()
        testExpected = '<p><b>Don\'t panic.</b><p>Fourscore and seven</p></p>'
        self.assertEqual(testResult, testExpected)

    def test_cPtcPP(self):
        testResult = cPtcPP.to_html()
        testExpected = '<p><p><p>Fourscore and seven</p></p><b>Don\'t panic.</b></p>'
        self.assertEqual(testResult, testExpected)


if __name__ == "__main__":
    unittest.main()
