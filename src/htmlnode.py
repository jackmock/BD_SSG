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
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        props_str = ''
        if self.props is not None:
            for i in self.props:
                props_str += (f' {i}="{self.props[i]}"')
        if self.tag is None:
            return f'{self.value}'
        else:
            return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'