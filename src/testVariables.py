from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextType, TextNode

#tags
t0 = None
t1 = "p"
t2 = "b"
t3 = "h1"
tn = "Bob"

#values
v0 = None
v1 = "Fourscore and seven"
v2 = "Don't panic."
vn = 6

#props
p0 = None
p1 = {"href": "place.thing"}
p2 = {"href": "place.thing",
      "cuke": "pickle"}
pn = "unpossible"

#children    (t,v,c,p)
#LeafNodes   (o,r,x,o)
#ParentNodes (r,x,r,o)
c0     = None
cLv    = LeafNode(t0,v1,c0,p0)
cLtv   = LeafNode(t2,v2,c0,p0)
cLtvp  = LeafNode(t1,v2,c0,p1)
cLtvp2 = LeafNode(t2,v2,c0,p2)
#cLtvc  = LeafNode(t2,v2,[cLv],p0)           #Fails; has child
#cLtv0  = LeafNode(t1,v0,c0,p0)              #Fails; no value
cPtc   = ParentNode(t1,v0,[cLv],p0)
cPtcp  = ParentNode(t2,v0,[cLtv],p1)
cPtcp2 = ParentNode(t1,v0,[cLtv],p2)
cPtc2  = ParentNode(t1,v0,[cLtv, cLtv],p0)
cPtc3  = ParentNode(t1,v0,[cLv, cLv, cLtv],p0)
cPtcP  = ParentNode(t1,v0,[cPtc],p0)
cPtc2P  = ParentNode(t1,v0,[cLtv,cPtc],p0)
cPtcP2  = ParentNode(t1,v0,[cPtc,cPtc],p0)
cPtcPP  = ParentNode(t1,v0,[cPtcP,cLtv],p0)
#cPtvc  = ParentNode(t2,v2,[cLv],p0)         #Fails; has value
#cPt0c  = ParentNode(t0,v0,[cLv],p0)         #Fails; no tag
#cPtc0  = ParentNode(t1,v0,c0,p0)            #Fails; no child

#TextNodes (text,text_type,url=None)
tT1 = TextNode(v1,TextType.TEXT)
tT2 = TextNode(v0,TextType.TEXT)
tT3 = TextNode(v2,TextType.TEXT,"place.thing")
tT4 = TextNode(vn,TextType.TEXT)
tB1 = TextNode(v1,TextType.BOLD)
tB2 = TextNode(v0,TextType.BOLD)
tB3 = TextNode(v2,TextType.BOLD,"place.thing")
tB4 = TextNode(vn,TextType.BOLD)
tI1 = TextNode(v1,TextType.ITALIC)
tI2 = TextNode(v0,TextType.ITALIC)
tI3 = TextNode(v2,TextType.ITALIC,"place.thing")
tI4 = TextNode(vn,TextType.ITALIC)
tC1 = TextNode(v1,TextType.CODE)
tC2 = TextNode(v0,TextType.CODE)
tC3 = TextNode(v2,TextType.CODE,"place.thing")
tC4 = TextNode(vn,TextType.CODE)
tL1 = TextNode(v1,TextType.LINK)
tL2 = TextNode(v0,TextType.LINK)
tL3 = TextNode(v2,TextType.LINK,"place.thing")
tL4 = TextNode(vn,TextType.LINK)
tM1 = TextNode(v1,TextType.IMAGE)
tM2 = TextNode(v0,TextType.IMAGE)
tM3 = TextNode(v2,TextType.IMAGE,"place.thing")
tM4 = TextNode(vn,TextType.IMAGE)
#tO1 = TextNode(v1,TextType.BLOB)
#tO2 = TextNode(v0,TextType.BLOB)
#tO3 = TextNode(v2,TextType.BLOB,"place.thing")
#tO4 = TextNode(vn,TextType.BLOB)

