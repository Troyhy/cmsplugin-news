CMS integration:

CMS_APPLICATIONS_URLS = (
    ('news.urls', gettext('News')),
)
CMS_NAVIGATION_EXTENDERS = (
    ('news.navigation.get_nodes', gettext('News menu')),
)