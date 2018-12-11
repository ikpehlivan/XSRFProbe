#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#    XSRF Probe     #
#-:-:-:-:-:-:-::-:-:#

# Author: 0xInfection
# This module requires XSRFProbe
# https://github.com/0xInfection/XSRFProbe

from json import dumps
from ast import literal_eval
from bs4 import BeautifulSoup, Tag

def GeneratePoC(action, fields, method='POST', encoding_type='application/x-www-form-urlencoded'):
    """
     Generate a CSRF PoC using basic form data
     """
    content = BeautifulSoup("<html></html>", "html.parser")
    html_tag = content.find("html")
    title_tag = content.new_tag('title')
    title_tag.string = 'CSRF PoC'
    html_tag.append(title_tag)
    head_tag = content.new_tag('h2')
    head_tag.string = 'Your CSRF PoC'
    html_tag.append(head_tag)
    form_tag = content.new_tag("form", action=action, method=method, enctype=encoding_type)
    html_tag.append(form_tag)

    for field in literal_eval(fields):
        label_tag = content.new_tag('label')
        label_tag.string = field['label']
        field_tag = content.new_tag("input", type=field['type'], value=field['value'])
        field_tag['name'] = field['name']
        form_tag.append(label_tag)
        form_tag.append(field_tag)

    submit_tag = content.new_tag("input", type="submit", value='Submit')
    form_tag.append(submit_tag)
    br_tag = content.new_tag('br')
    html_tag.append(br_tag)
    footer_tag = content.new_tag('footer')
    html_tag.append(footer_tag)
    small_tag = content.new_tag('small')
    small_tag.string = '(i) This PoC form was generated by XSRFProbe.'
    footer_tag.append(small_tag)
    m = content.prettify()
    for i in m.splitlines():
        print('  '+i)
