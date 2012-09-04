from zope import schema
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

from . import messageFactory as _


class IKeywordsForm(Interface):
    keywords = schema.List(
        title=_(u'Keywords'),
        description=_(u'Add keywords to this content'),
        value_type=schema.TextLine(),
        required=True,
    )


class IBrowserLayer(IDefaultPloneLayer):
    """The browser layer of the package
    """
