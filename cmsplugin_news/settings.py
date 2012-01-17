from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _


def get_setting(name, default):
    """
    A little helper for fetching global settings with a common prefix.
    """
    parent_name = "CMSPLUGIN_NEWS_{}".format(name)
    return getattr(django_settings, parent_name, default)

"""
    Disables the latest news plugin
    Defaults to false
"""
DISABLE_LATEST_NEWS_PLUGIN = get_setting('DISABLE_LATEST_NEWS_PLUGIN', False)
FEED_SIZE = get_setting('FEED_SIZE', 10)
FEED_TITLE = get_setting('FEED_TITLE', _('News feed'))
FEED_DESCRIPTION = get_setting('FEED_DESCRIPTION', _('A feed full of news'))

