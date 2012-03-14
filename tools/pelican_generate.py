# TODO: make it able to generate
# - drafts
# - pages
# - blog entries
# being able to get all the needed options

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
Date: $day
Title: $title
Tags: $tags
'''
}

# only the title is actually mandatory

# TODO: is there a way to validate things?
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Generate pages drafts and blog posts',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-m',
                        '--markup',
                        help='Article markup',
                        choices=('rst', 'md'),
                        default='rst')

    parser.add_argument('-t', '--type',
                        choices=('draft', 'blog', 'page'),
                        default='blog',
                        help='Type of entry to create')

    parser.add_argument('title',
                        help='Title of the article')

    return parser.parse_args()


def main():
    ns = parse_arguments()
    
