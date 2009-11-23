ALPHA

Name: cmsplugin-news
Description: A news plugin for django-cms
Download: http://bitbucket.org/MrOxiMoron/cmsplugin-news/

Requirements:
- django-cms-2.0.0 final
- django: 1.1.1
+ requirements for django-cms-2.0

Last tested with:
- django-cms-2.0.0 final
- django: 1.1.1

Setup
- make sure requirements are installed and properly working
- add cmsplugin_news to python path
- add 'cmsplugin_news' to INSTALLED_APPS
- run 'python manage.py syncdb'
- Add the cmsplugin_news.urls to the CMS_APPLICATIONS_URLS setting 
- Add the cmsplugin_news.navigation.get_nodes to the CMS_NAVIGATION_EXTENDERS setting
- Create a page in cms and in the 'advanced settings' section of the admin for that page, for 'Navigation extenders' select 'news navigation' and for 'application' select 'news' (Restart of the server required due to caching!)
- Create the propper templates for your site, the ones included with the app are VERY basic

Todo and Tomaybes:
- Add more tests
- add to cms_plugins.py for plugins
 - month view with days that link to archive_day view
- Allow comments on news (add option to the news model for it)
- Optimize the navigation code, it works but there is probably a better way to do it.
- Add RSS feed
- Add optional author field
- Add optional end date to hide news again
- Add Tags
- Add translations (I can do the dutch one)
- Ideas other people come up with :D

Examples:

CMS_APPLICATIONS_URLS = (
    ('cmsplugin_news.urls', 'News'),
)
CMS_NAVIGATION_EXTENDERS = (
    ('cmsplugin_news.navigation.get_nodes','News navigation'),
)


Suggestion:
To avoid confusion add a "application" template to the CMS which is like other templates but without any placeholders.
That way users won't get tempted to fill the placeholders and then complain they don't show up ;-)
