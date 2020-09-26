

class TreeNode:
    def __init__(self, token=None):
        self.token = token

    def crawl_tree(self):
        raise NotImplementedError


class OneNode(TreeNode):
    """
    first, second, csv, nsv
    """
    def __init__(self, token=None, format="NO FORMAT SET"):
        super().__init__(token)
        self.format = format
        self.children = []
        # self.sym_table = [*sym_table]

    def add_child(self, node):
        self.children.append(node)

    def crawl_tree(self):
        if "first" in self.format:
            first = oneprint(self.children[0])
            self.format = self.format.replace("first", first)
        if "second" in self.format:
            second = oneprint(self.children[1])
            self.format = self.format.replace("second", second)
        if "csv" in self.format:
            csv = ",".join(oneprint(node) for node in self.children)
            self.format = self.format.replace("csv", csv)
        if "nsv" in self.format:
            nsv = "\n".join(oneprint(node) for node in self.children)
            self.format = self.format.replace("nsv", nsv)
        return self.format


def oneprint(node):
    if node is None:
        return ""
    if isinstance(node, OneNode):
        return node.crawl_tree()
    if node.value:
        return node.value
