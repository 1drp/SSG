from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        if value is not None:
        # Future validation checks
            raise ValueError("ParentNode cannot have a value")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.children is None:
            raise ValueError("ParentNode must have children")
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        filler = ""
        for child in self.children:
            filler += child.to_html()
        retString = f"<{self.tag}{super().props_to_html()}>{filler}</{self.tag}>"
        return retString
