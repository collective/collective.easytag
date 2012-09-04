from Products.Five.browser.metaconfigure import ViewMixinForTemplates
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView


# The widget rendering templates need to be Zope 3 templates
class RenderWidget(ViewMixinForTemplates, BrowserView):
    index = ViewPageTemplateFile('widget.pt')
