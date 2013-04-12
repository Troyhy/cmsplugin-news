News plugin for django-cms 2.x
===============================

This plugin provides a simple news feature for django-cms 2.0 and newer and
and tries to keep it as simple as possible without extras like tagging or
categories but while providing a news feed and menu integration.

Setup
-----

* Install django-cms (if you haven't done so already)

* Run `pip install cmsplugin-news` or download this package and run
  `python setup.py install` or add it in some other way to your current
  PYTHON_PATH

* Add 'cmsplugin_news' to INSTALLED_APPS

* If you're using South execute `python manage.py migrate`, Otherwise run
  `python manage.py syncdb` within your project directory.
* In order to integrate the news-plugin with your website, create a page and add
  the news application (and optionally the news menu) to it by modifying the
  relevant "advanced settings" of it.

Last tested with
----------------

* django-cms-2.2 and 2.3
* django: 1.3.4

History
-------

0.4.2:
    * Compatibility fix for Django 1.5

0.4:
    * New maintainer
    * RSS/Atom feed
    * CMS menu integration
    * Upgrade to django-cms 2.2 (and 2.3)

0.3:
    * Moved to beta phase
    * Tested with django-cms 2.0 final

0.2b:
    * Various bug fixes

0.2a/0.1a5:
    * Adds excerpt to news model
