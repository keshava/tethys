

class TethysGizmoOptions(dict):
    """
    Base class for Tethys Gizmo Options objects.
    """

    def __init__(self, attributes='', classes=''):
        """
        Constructor for Tethys Gizmo Options base.
        """
        # Initialize super class
        super(TethysGizmoOptions, self).__init__()

        # Dictionary magic
        self.__dict__ = self

        self.attributes = attributes
        self.classes = classes


class SecondaryGizmoOptions(dict):
    """
    Base class for Secondary Tethys Gizmo Options objects.
    """

    def __init__(self):
        """
        Constructor for Tethys Gizmo Options base.
        """
        # Initialize super class
        super(SecondaryGizmoOptions, self).__init__()

        # Dictionary magic
        self.__dict__ = self