# -*- coding: utf-8 -*-
from udala.alertak.behaviors.alert import IAlertMarker
from udala.alertak.testing import UDALA_ALERTAK_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class AlertIntegrationTest(unittest.TestCase):

    layer = UDALA_ALERTAK_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_alert(self):
        behavior = getUtility(IBehavior, 'udala.alertak.alert')
        self.assertEqual(
            behavior.marker,
            IAlertMarker,
        )
