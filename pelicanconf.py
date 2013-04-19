#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'EarthPy'
SITENAME = u'EarthPy'
SITEURL = 'http://earthpy.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
PLUGINS = ['pelican.plugins.ipythonnb']
MARKUP = ('md', 'ipynb')
# Blogroll
LINKS =  (('Python for the Atmospheric and Oceanic Sciences', 'http://pyaos.johnny-lin.com/'),
          ('koldunov.net (in Russian)', 'http://koldunov.net'),
         )

# Social widget
SOCIAL = ((' ', '#'),
         )

DEFAULT_PAGINATION = False
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 100
DISQUS_SITENAME = 'earthpy'
GOOGLE_ANALYTICS = 'UA-40120864-1'

