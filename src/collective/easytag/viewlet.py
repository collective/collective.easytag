# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from zope.security import checkPermission

# from zope.interface import implements
# from zope.component import getUtility, getMultiAdapter

from z3c.form import form, button, field
from z3c.form.interfaces import IFormLayer
from plone.z3cform import z2

# from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets import ViewletBase
# from plone.memoize.instance import memoizedproperty

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.z3cform.widgets.token_input_widget import TokenInputFieldWidget

# from ..interfaces import IStorage
# from ..interfaces import IPreferences
from .interfaces import IKeywordsForm
# from ..interfaces import IMarkable
# from ..utils import get_current_user
from . import messageFactory as _


# class MarkFormAdapter(object):
#     implements(IMarkForm)

#     def __init__(self, context):
#         self.context = context

#     @property
#     def member_id(self):
#         return get_current_user(self.context).getProperty('id')

#     @property
#     def storage(self):
#         return IStorage(self.context)

#     def get_read(self):
#         return self.member_id in self.storage

#     def set_read(self, value):
#         if value:
#             self.storage.add(self.member_id)
#         else:
#             self.storage.remove(self.member_id)

#     read = property(get_read, set_read)


class KeywordsForm(form.Form):
    template = ViewPageTemplateFile("form.pt")
    fields = field.Fields(IKeywordsForm)
    fields['keywords'].widgetFactory = TokenInputFieldWidget

    ignoreContext = True

    @button.buttonAndHandler(_(u'Add'))
    def handleAdd(self, action):
        # pylint: disable=W0613, W0612
        data, errors = self.extractData()
        if errors:
            return

        def encode_tag(tag):
            if not isinstance(tag, unicode):
                tag = tag.decode('utf-8')
            return tag

        tags = [encode_tag(t) for t in self.context.Subject()]
        a = [tags.append(t) for t in data['keywords'] if t not in tags]
        import pdb; pdb.set_trace( )
        self.context.setSubject(tags)
        self.context.reindexObject(idxs=['Subject'])


class Viewlet(ViewletBase):

    index = ViewPageTemplateFile("viewlet.pt")

    # @memoizedproperty
    # def settings(self):
    #     settings = getUtility(IRegistry).forInterface(IPreferences)
    #     return settings

    def update(self):
        super(Viewlet, self).update()
        self.form = u''
        if checkPermission('cmf.ModifyPortalContent', self.context):
            z2.switch_on(self, request_layer=IFormLayer)
            self.form = KeywordsForm(aq_inner(self.context), self.request)
            self.form.update()

    def available(self):
        return True

    # def is_visible(self):
    #     """Whether to show the viewlet or not.

    #     Returns ``True`` if the current user is authenticated
    #     and the context is within the list of content types
    #     that are set to support this behavior
    #     (``allowed_types`` in the preferences),
    #     ``False`` otherwise.
    #     """
    #     ps = getMultiAdapter(
    #         (self.context, self.request),
    #         name="plone_portal_state"
    #     )

    #     if ps.anonymous():
    #         return False
    #     if self.context.portal_type not in self.settings.allowed_types:
    #         return False
    #     return True

    # def is_read(self):
    #     """Whether the current user has already read this content.

    #     Returns ``True`` if this is the case,
    #     ``False`` otherwise
    #     """
    #     current_user = get_current_user(self.context)
    #     storage = IStorage(self.context)
    #     return current_user.getProperty('id') in storage
