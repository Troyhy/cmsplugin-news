import sys
from os.path import join, dirname

from django.conf import settings


def get_test_runner():
    settings.configure(
        CACHE_BACKEND='locmem:///',
        DEBUG=True,
        TEMPLATE_DEBUG=True,
        DATABASE_SUPPORTS_TRANSACTIONS=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        SITE_ID=1,
        USE_I18N=True,
        MEDIA_ROOT='/media/',
        STATIC_ROOT='/static/',
        CMS_MEDIA_ROOT='/cms-media/',
        CMS_MEDIA_URL='/cms-media/',
        MEDIA_URL='/media/',
        STATIC_URL='/static/',
        ADMIN_MEDIA_PREFIX='/static/admin/',
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
        SECRET_KEY='key',
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            'django.template.loaders.eggs.Loader',
        ),
        TEMPLATE_CONTEXT_PROCESSORS=[
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.i18n",
            "django.core.context_processors.debug",
            "django.core.context_processors.request",
            "django.core.context_processors.media",
            'django.core.context_processors.csrf',
            "cms.context_processors.media",
            "sekizai.context_processors.sekizai",
            "django.core.context_processors.static",
        ],
        MIDDLEWARE_CLASSES=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'cms.middleware.multilingual.MultilingualURLMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.doc.XViewMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'cms.middleware.user.CurrentUserMiddleware',
            'cms.middleware.page.CurrentPageMiddleware',
            'cms.middleware.toolbar.ToolbarMiddleware',
        ],
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.staticfiles',
            'cms',
            'menus',
            'mptt',
            'cms.plugins.text',
            'cms.plugins.picture',
            'cms.plugins.file',
            'cms.plugins.flash',
            'cms.plugins.link',
            'cms.plugins.snippet',
            'cms.plugins.googlemap',
            'cms.plugins.teaser',
            'cms.plugins.video',
            'cms.plugins.twitter',
            'cms.plugins.inherit',
            'south',
            'sekizai',
            'cmsplugin_news',
        ],
        LANGUAGE_CODE="en",
        LANGUAGES=(
            ('en', 'English'),
            ('de', 'German'),
        ),
        CMS_LANGUAGES=(
            ('en', 'English'),
            ('de', 'German'),
        ),
        CMS_LANGUAGE_CONF={
            'de': ['de', 'en'],
            'en': ['de', 'de'],
        },
        CMS_SOFTROOT=True,
        CMS_MODERATOR=True,
        CMS_PERMISSION=True,
        CMS_PUBLIC_FOR='all',
        CMS_CACHE_DURATIONS={
            'menus': 0,
            'content': 0,
            'permissions': 0,
        },
        CMS_APPHOOKS=[],
        CMS_REDIRECTS=True,
        CMS_SEO_FIELDS=True,
        CMS_FLAT_URLS=False,
        CMS_MENU_TITLE_OVERWRITE=True,
        CMS_HIDE_UNTRANSLATED=False,
        CMS_URL_OVERWRITE=True,
        CMS_SHOW_END_DATE=True,
        CMS_SHOW_START_DATE=True,
        CMS_PLUGIN_PROCESSORS=tuple(),
        CMS_PLUGIN_CONTEXT_PROCESSORS=tuple(),
        CMS_SITE_CHOICES_CACHE_KEY='CMS:site_choices',
        CMS_PAGE_CHOICES_CACHE_KEY='CMS:page_choices',
        SOUTH_TESTS_MIGRATE=False,
        JUNIT_OUTPUT_DIR='.',
        TIME_TESTS=False,
        CMS_TEMPLATES=[('test_template.html', 'base')],
        TEMPLATE_DIRS=[join(dirname(__file__), 'test_setup', 'templates')],
        ROOT_URLCONF='cmsplugin_news.urls'
    )
    from south.management.commands import patch_for_test_db_setup
    patch_for_test_db_setup()
    from django.test.utils import get_runner
    return get_runner(settings)


def main():
    test_runner = get_test_runner()(verbosity=1, interactive=False)
    failures = test_runner.run_tests(['cmsplugin_news'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    main()
