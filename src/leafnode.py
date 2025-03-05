from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        match (self.tag, self.value):
            case (_, None):
                raise ValueError()
            case (None | "", _):
                return self.value
            case _:
                return f"<{self.tag}>{self.value}</{self.tag}>"
