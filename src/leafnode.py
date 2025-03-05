from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        match (self.tag, self.value, self.props):
            case (_, None, _):
                raise ValueError()
            case (None | "", _, _):
                return self.value
            case _:
                propstring = self.props_to_html()
                return f'<{self.tag}{" "+propstring if propstring else ""}>{self.value}</{self.tag}>'
