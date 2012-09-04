import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from collective.easytag.testing import\
    COLLECTIVE_EASYTAG_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_EASYTAG_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        self.installed_prd = [p['id'] for p in qi_tool.listInstalledProducts()]

    def test_product_is_installed(self):
        """Validate that our products GS profile
        has been run and the product installed
        """
        pid = 'collective.easytag'

        self.assertTrue(pid in self.installed_prd,
                        'package appears not to have been installed')

    def test_dependencies(self):
        """Validate that product's dependencies are installed
        """
        dependencies = [
            'collective.z3cform.widgets'
        ]
        for prd in dependencies:
            self.assertTrue(prd in self.installed_prd,
                        '%s appears not to have been installed' % prd)
