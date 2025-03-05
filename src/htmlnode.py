class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: "HTMLNode" = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return " ".join([f'{k}="{v}"' for k, v in self.props.items()]) if self.props else ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, o):
        return self.__repr__() == o.__repr__()
