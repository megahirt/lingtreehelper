#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
from string import Template
import utils
import lingtree

def savetofile(text):
    print "Content-Type: text/plain"
    print "Content-Disposition: attachment; filename=simple.txt"
    print
    print text

def printTemplate(variables):
    print "Content-Type: text/html; charset=utf-8"
    print

    # import 'result template' if result is not empty
    if variables['result'] != '':
        result = Template(utils.file2string('result.tpl'))
        result = result.substitute(variables)
        variables['result'] = result

    html = Template(utils.file2string('template.html'))
    print html.substitute(variables)


# main program
form = cgi.FieldStorage()

if form.has_key('savetofile'):
    savetofile(form['simple_text'].value)
elif form.has_key('mode') and form['mode'].value == 'restore':
    # read at most a 50K document
    printTemplate({'simple_text': form['file'].file.read(50000), 'result': ''})
else:
    if form.has_key('simple_text'):
        result = lingtree.convert(form['simple_text'].value)
        printTemplate({'simple_text': form['simple_text'].value, 'result': result})
    else:
        default_text = """
# an example
# erase this and compose your own

S =&gt; NP1 VP
NP1 =&gt; Lee
VP =&gt; V NP2
V =&gt; gets
NP2 =&gt; Det N
Det =&gt; the
N =&gt; idea
"""
        printTemplate({'simple_text': default_text, 'result': ''})
