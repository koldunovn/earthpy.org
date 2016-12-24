#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'EarthPy'
SITENAME = u'EarthPy'
SITEURL = 'http://earthpy.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
#IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output'))]
IGNORE_FILES = ['.ipynb_checkpoints']

#NOTEBOOK_DIR = '/home/magik/INTERNET/EARTHPY/earthpy.org/content2/notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Blogroll
LINKS =  (('Python for the Atmospheric and Oceanic Sciences', 'http://pyaos.johnny-lin.com/'),
          ('koldunov.net (in Russian)', 'http://koldunov.net'),
          ('OceanPython.org','http://oceanpython.org ' ),
          ('python4oceanographers', 'http://ocefpaf.github.io/')
         )

# Social widget
SOCIAL = ((' ', '#'),
         )

DEFAULT_PAGINATION = False
#TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 100
DISQUS_SITENAME = 'earthpy'
GOOGLE_ANALYTICS = 'UA-40120864-1'

