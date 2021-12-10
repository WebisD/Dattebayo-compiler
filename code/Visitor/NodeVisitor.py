class NodeVisitor(object):
    def visit(self, node, indentation=None):
        """ Visit the node

        """
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)

        return visitor(node, indentation)

    def generic_visit(self, node):
        """ Raise a custom exception

        """
        raise Exception('No visit_{} method'.format(type(node).__name__))
