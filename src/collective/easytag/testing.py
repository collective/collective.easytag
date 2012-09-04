# pylint: disable=W0613
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
# from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig


class CollectiveEasytag(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.easytag
        xmlconfig.file('configure.zcml',
                       collective.easytag,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.easytag:default')

COLLECTIVE_EASYTAG_FIXTURE = CollectiveEasytag()
COLLECTIVE_EASYTAG_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_EASYTAG_FIXTURE, ),
                       name="CollectiveEasytag:Integration")
