class TeXMLError(Exception):
    pass


class NotNestable(TeXMLError):
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

    def __str__(self):
        return "'{}' element cannot be nested within a '{}' element".format(
            self.child, self.parent
        )
        

class NotAnElement(TeXMLError):
    def __init__(self, obj):
        self.obj_type = type(obj)

    def __str__(self):
        return "'{}' object is not an element".format(self.obj_type)


class InvalidAttribute(TeXMLError):
    def __init__(self, attr, element=None):
        """
            :param attr: The invalid attribute
            :param element: The element associated with the attribute (optional)
        """
        self.attr = attr
        self.element = element

    def __str__(self):
        if self.element:
            return "attribute '{}' is invalid for element '{}'".format(
                self.attr, 
                self.element
            )
        else:
            return "invalid attribute '{}'".format(self.attr)


class InvalidOption(TeXMLError):
    def __init__(self, option, attr=None):
        """
            :param option: The invalid option 
            :param attr: The attribute associated with the option (optional)
        """
        self.option = option
        self.attr = attr

    def __str__(self):
        if self.attr:
            return "option '{}' is invalid for attribute '{}'".format(
                self.option, 
                self.attr
            )
        else:
            return "invalid option '{}'".format(self.option)

