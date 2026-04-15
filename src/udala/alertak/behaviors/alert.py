from plone import schema
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from udala.alertak import _
from udala.alertak.vocabularies.where_to_show_alert import HOME
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IAlertMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IAlert(model.Schema):
    """ """

    model.fieldset(
        "alerts",
        label=_("label_schema_alerts", default="Alerts"),
        fields=[
            "alert_show",
            "alert_title",
            "alert_text",
            "alert_link",
            "alert_link_text",
            "alert_start_date",
            "alert_end_date",
            "alert_where_to_show",
        ],
    )

    alert_show = schema.Bool(
        title=_("Show alert"),
        description=_("If checked, the alert will be shown in the site"),
        required=False,
        default=False,
    )

    alert_title = schema.TextLine(
        title=_("Alert title"),
        description=_("Give in a title for the alert"),
        required=False,
    )

    alert_text = RichText(
        title=_("Alert text"),
        description=_("Give in a text for the alert"),
        required=False,
    )

    alert_link = schema.TextLine(
        title=_("Alert link"),
        description=_("If given, the alert title will be a link to this URL"),
        required=False,
    )

    alert_link_text = schema.TextLine(
        title=_("Alert link text"),
        description=_("If given, this text will be shown as the link text"),
        required=False,
    )

    alert_start_date = schema.Datetime(
        title=_("Alert start date"),
        description=_("If entered, the alert will be shown starting from this date"),
        required=False,
    )

    alert_end_date = schema.Datetime(
        title=_("Alert end date"),
        description=_("If entered, the alert will be shown untils this date"),
        required=False,
    )

    alert_where_to_show = schema.Choice(
        title=_("Where to show the alert"),
        description=_(
            "Select the sections of the site where the alert will be shown. "
            "If none is selected, the alert will be shown in all sections."
        ),
        required=False,
        vocabulary="udala.alertak.WhereToShowAlert",
        default=HOME,
    )


@implementer(IAlert)
@adapter(IAlertMarker)
class Alert:
    def __init__(self, context):
        self.context = context

    @property
    def alert_show(self):
        if safe_hasattr(self.context, "alert_show"):
            return self.context.alert_show
        return None

    @alert_show.setter
    def alert_show(self, value):
        self.context.alert_show = value

    @property
    def alert_title(self):
        if safe_hasattr(self.context, "alert_title"):
            return self.context.alert_title
        return None

    @alert_title.setter
    def alert_title(self, value):
        self.context.alert_title = value

    @property
    def alert_text(self):
        if safe_hasattr(self.context, "alert_text"):
            return self.context.alert_text
        return None

    @alert_text.setter
    def alert_text(self, value):
        self.context.alert_text = value

    @property
    def alert_link(self):
        if safe_hasattr(self.context, "alert_link"):
            return self.context.alert_link
        return None

    @alert_link.setter
    def alert_link(self, value):
        self.context.alert_link = value

    @property
    def alert_link_text(self):
        if safe_hasattr(self.context, "alert_link_text"):
            return self.context.alert_link_text
        return None

    @alert_link_text.setter
    def alert_link_text(self, value):
        self.context.alert_link_text = value

    @property
    def alert_start_date(self):
        if safe_hasattr(self.context, "alert_start_date"):
            return self.context.alert_start_date
        return None

    @alert_start_date.setter
    def alert_start_date(self, value):
        self.context.alert_start_date = value

    @property
    def alert_end_date(self):
        if safe_hasattr(self.context, "alert_end_date"):
            return self.context.alert_end_date
        return None

    @alert_end_date.setter
    def alert_end_date(self, value):
        self.context.alert_end_date = value

    @property
    def alert_where_to_show(self):
        if safe_hasattr(self.context, "alert_where_to_show"):
            return self.context.alert_where_to_show
        return None

    @alert_where_to_show.setter
    def alert_where_to_show(self, value):
        self.context.alert_where_to_show = value
