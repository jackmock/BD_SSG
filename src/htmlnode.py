class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
        # child classes override this method

    def props_to_html(self):
        result_string = ""
        
        if not self.props:
            return result_string
        
        for prop, prop_val in self.props.items():
            result_string += f' {prop}="{prop_val}"'
        return result_string
    
    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have value")
            
        if self.tag is None:
            return self.value
            
        if self.props:
            props_str = ""
            for key, value in self.props.items():
                props_str += f' {key}="{value}"'
            return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        result = ''
        for child in self.children:
            result += child.to_html()
        return (f'<{self.tag}>{result}</{self.tag}>')