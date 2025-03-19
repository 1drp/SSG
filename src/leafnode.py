from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        if children is not None:
        # Future validation checks:
        # tags =None or in set of valid HTML tags
        # props =None or is dictionary with strings as both keys and values
        # move value check to constructor so that it doesn't depend on to_html being called.
            raise ValueError("LeafNode cannot have children")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        retString = f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        return retString

