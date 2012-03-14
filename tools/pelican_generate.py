import argparse

from time import localtime
from string import Template

# check how localtime can actually work

ENTRY = {
    'rst': '''
$title
##############

:date: $day $time
:tags: $tags
:category: $category
:author: Alexis Metaireau
''',
'markdown': '''
Date: 2010-12-03
Title: My super title
Tags: thats, awesome
Slug: my-super-post

This is the content of my super blog post.
'''
}

# only the title is actually mandatory
