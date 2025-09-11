# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api
from plone.memoize.view import memoize
from datetime import datetime
from udala.alertak.vocabularies.where_to_show_alert import HOME

class AlertViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return "My message"

    def index(self):
        return super(AlertViewlet, self).render()

    @property
    @memoize
    def navigation_root(self):
        return api.portal.get_navigation_root(self.context)

    def show(self):
        now = datetime.now()

        if self.navigation_root.alert_show:
            if self.navigation_root.alert_where_to_show is HOME:
                if self.context.absolute_url() != self.navigation_root.absolute_url():
                    return False


            if (
                self.navigation_root.alert_start_date
                and self.navigation_root.alert_end_date
                and self.navigation_root.alert_start_date
                <= now
                <= self.navigation_root.alert_end_date
            ):
                return True
            if (
                self.navigation_root.alert_start_date
                and not self.navigation_root.alert_end_date
                and self.navigation_root.alert_start_date <= now
            ):
                return True
            if (
                self.navigation_root.alert_end_date
                and not self.navigation_root.alert_start_date
                and now <= self.navigation_root.alert_end_date
            ):
                return True
            if (
                self.navigation_root.alert_start_date is None
                and self.navigation_root.alert_end_date is None
            ):
                return True
        return False
