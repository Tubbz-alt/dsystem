#!/usr/bin/env python
"""
Dogtail script for generating unhelpful help file.

Scours the UI of a program, and generates a parody of a help file for that
program.

The resulting DocBook file is simply a reading back of the program's UI to you.

The idea is to highlight a gripe of mine (and many other people):
documentation should be more than this!

This script is licensed under the GPL.
"""
__author__ = 'David Malcolm <dmalcolm@redhat.com>'

from dogtail.tree import *
from dogtail.utils import *
import sys, cgi

def writePCDataElement(name, content):
    print(('<%s>%s</%s>' % (name, content, name)))

def generateUnhelpfulHelp(appName):
    try:
        app = root.application(appName)
    except SearchError:
        run(appName)
    print('<?xml version="1.0"?>')
    print('<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.1.2//EN" "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd">')
    print('<article>')

    taggedAppName = '<application>%s</application>'%cgi.escape(appName)

    # Artile info:
    print('\t<articleinfo>')
    writePCDataElement("title", "The Totally Definitive No-Nonsense Unhelpful Complete Guide to %s for Mannequins in 40 Days - Unleashed!"%taggedAppName)
    print('\t</articleinfo>')

    # Guts of the article:
    print('\t<sect1>')
    writePCDataElement("title", "Introduction")
    writePCDataElement("caution", "<para>Do not take these instructions seriously.  They are a parody of unhelpful help files found on many computer systems, and were autogenerated by <application>no-help-at-all</application></para>")
    writePCDataElement("para", "You can start %s by opening a terminal and typing the <command>%s</command> command."%(taggedAppName, cgi.escape(appName)))
    print('\t</sect1>')

    menus = app.findChildren(predicate.GenericPredicate(roleName="menu"))
    for menu in menus:
        print('\t<sect1>')
        writePCDataElement("title", "The <guimenu>%s</guimenu> menu"%cgi.escape(menu.name))
        writePCDataElement("para", "Use the <guimenu>%s</guimenu> menu to work with %ss"%(cgi.escape(menu.name), cgi.escape(menu.name.lower())))
        items = menu.findChildren(predicate.GenericPredicate(roleName="menu item"), recursive=False)
        if items!=None:
            for item in items:
                verb = item.name
                noun = menu.name
                print('\t\t<sect2>')
                writePCDataElement("title", "%sing a %s"%(cgi.escape(verb.title()), cgi.escape(noun.lower())))
                writePCDataElement("para", "To %s a %s, choose <guimenu>%s</guimenu> &gt; <guimenuitem>%s</guimenuitem>"%(cgi.escape(verb.lower()), cgi.escape(noun.lower()), cgi.escape(menu.name), cgi.escape(item.name)))
                print('\t\t</sect2>')
        print('\t</sect1>')

    print('</article>')

if __name__=='__main__':
    try:
        generateUnhelpfulHelp(sys.argv[1])
    except IndexError:
        print("####################################")
        print("please supply an application name on the cmdline")
        print("####################################")
