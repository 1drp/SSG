
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Basic validity checks for all HTMLNode objects
        if not (tag is None or isinstance(tag,str)):
            # Need to create Enum to use for tag validity checks
            raise ValueError("Tag must be a valid HTML tag")
        
        if not (value is None or isinstance(value,str)):
            raise TypeError("Value must be a string")
        
        if children is not None:
            if not isinstance(children,list):
                raise TypeError("Children must be in a list")
            for child in children:
                if not isinstance(child,HTMLNode):
                    raise ValueError("All children must be HTMLNodes")
        
        if props is not None:
            if not isinstance(props, dict):
                raise TypeError("Props must be a dictionary")
            for k, v in props.items():
                if not isinstance(k,str) or not isinstance(v,str):
                    raise ValueError("All keys and values in props must be strings")
        
        # Set attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        pstring = ""
        if self.props is not None:
            for p in self.props:
                pstring += " " + p + '="' + self.props[p] + '"'
        return pstring 

    def __repr__(self):
        print(f"tag: {self.tag}")
        print(f"value: {self.value}")
        print(f"children: {self.children}")
        print(f"props: {self.props_to_html()}")
