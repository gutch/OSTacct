# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317650335.730118
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/data.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/data.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['sidebar_bottom', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        params = context.get('params', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(escape(parent.sidebar_top()))
        __M_writer(u'\n\n<h2>Content Type Dispatch</h2>\n<p>\nThis page shows how you can provide multiple pages\ndirectly from the same controller method.  This page is generated \nfrom the expose decorator with the template defintion provided.\nYou can provide a url with parameters and this page will display\nthe parameters as html, and the json version will express\nthe entries as JSON.  Here, try it out: <a href="/data.html?a=1&b=2">/data.html?a=1&b=2</a>\n</p>\n\n<p>Click here for the <a href="')
        # SOURCE LINE 19
        __M_writer(escape(tg.url('/data.json', params=params)))
        __M_writer(u'">JSON Version of this page.</a></p>\n<p>The data provided in the template call is: \n    <table>\n')
        # SOURCE LINE 22
        for key, value in params.iteritems():
            # SOURCE LINE 23
            __M_writer(u'        <tr>\n            <td>')
            # SOURCE LINE 24
            __M_writer(escape(key))
            __M_writer(u'</td>\n            <td>')
            # SOURCE LINE 25
            __M_writer(escape(value))
            __M_writer(u'</td>\n        </tr>\n')
            pass
        # SOURCE LINE 28
        __M_writer(u'    </table>\n\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_bottom(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  Welcome to TurboGears 2.1, standing on the shoulders of giants, since 2007\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


