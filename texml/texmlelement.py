from lxml import etree
from types import FunctionType
from .exceptions import TeXMLError

class TeXMLElement:
    _name = ''
    _attributes = {}
    _nouns = []
    
    def __init__(self, *args, **kwargs):
        #set all attributes to None
        self.__dict__ = dict.fromkeys(self._attributes)

        #The text content inside the tag
        self.text = args[0] if args else None

        for attr, value in kwargs.items():

            #raise error if invalid attribute
            if attr not in self._attributes:
                raise TeXMLError(
                    "attribute '{}' not allowed for element '{}'".format(
                        attr, 
                        self._name
                    )
                )
            
            #raise error if invalid option
            options = self._attributes.get(attr)
            if options:

                #if options is a list
                if type(options) in (list, tuple):
                    if value not in options:
                        raise TeXMLError(
                            "option '{}' not allowed for attribute '{}'".format(
                                value,
                                attr
                            )
                        )

                #if options is a function
                elif type(options) == FunctionType:
                    if not options(value):
                        raise TeXMLError(
                            "option '{}' not allowed for attribute '{}'".format(
                                value,
                                attr
                            )
                        )

            setattr(self, attr, value)

        self.children = []

    def append(self, element):
        if not isinstance(element, TeXMLElement):
            raise TeXMLError("element must be of type '{}'".format(TeXMLElement.__name__))

        if element._name not in self._nouns:
            raise TeXMLError(
                "'{}' element cannot be nested in a '{}' element".format(
                    element._name,
                    self._name
                )
            )

        self.children.append(element)
        return self

    def __str__(self):
        e = self.to_element()
        return etree.tostring(e, pretty_print=True, encoding='unicode')

    def to_dict(self, to_element=False):
        """
            :param to_element: If True, exclude attributes with None values
                and convert to str.
            :type to_element: bool
        """
        d = {}
        for attr in self._attributes:
            value = getattr(self, attr)
            
            if to_element:
                if value is None:
                    continue

                if type(value) == bool:
                    value = str(value).lower()
                else:
                    value = str(value)

            d[attr] = value

        return d

    def to_element(self, parent=None):
        attrib = self.to_dict(to_element=True)

        if parent is None:
            e = etree.Element(self._name, attrib=attrib)
        else:
            e = etree.SubElement(parent, self._name, attrib=attrib)

        if self.text:
            e.text = self.text

        for child in self.children:
            child.to_element(parent=e)

        return e
