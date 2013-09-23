#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'EarthPy'
SITENAME = u'EarthPy'
SITEURL = 'http://earthpy.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
PLUGIN_PATH = '/home/magik/INTERNET/EARTHPY/pelican-plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook']

#NOTEBOOK_DIR = '/home/magik/INTERNET/EARTHPY/earthpy.org/content2/notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

MARKUP = ('md')
# Blogroll
LINKS =  (('Python for the Atmospheric and Oceanic Sciences', 'http://pyaos.johnny-lin.com/'),
          ('koldunov.net (in Russian)', 'http://koldunov.net'),
         )

# Social widget
SOCIAL = ((' ', '#'),
         )

DEFAULT_PAGINATION = False
#TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 100
DISQUS_SITENAME = 'earthpy'
GOOGLE_ANALYTICS = 'UA-40120864-1'

