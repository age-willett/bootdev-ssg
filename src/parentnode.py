from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: [HTMLNode], props: dict = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        match (self.tag, self.children, self.props):
            case (None | "", _, _):
                raise ValueError("missing tag")
            case (_, None, _):
                raise ValueError("missing children")
            case _:
                if type(self.children) is not list:
                    raise TypeError("children is not a list")
                propstring = self.props_to_html()
                return f"<{self.tag}{' ' + propstring if propstring else ''}>{''.join([c.to_html() for c in self.children])}</{self.tag}>"
