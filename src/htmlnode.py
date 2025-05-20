class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
        # child classes will override this method

    def props_to_html(self):
        result_string = ""
        
        if not self.props:
            return result_string
        
        for prop, prop_val in self.props.items():
            result_string += f' {prop}="{prop_val}"'
        return result_string
    
    def __repr__(self):
        return(f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})")