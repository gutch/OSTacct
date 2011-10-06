# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317650335.959218
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/environ.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/environ.mak'
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
        environment = context.get('environment', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(escape(parent.sidebar_top()))
        __M_writer(u'\n<h2>The WSGI nature of the framework</h2>\n  <p>In this page you can see all the WSGI variables your request object has, \n     the ones in capital letters are required by the spec, then a sorted by\n     component list of variables provided by the Components, and at last\n     the "wsgi." namespace with very useful information about your WSGI Server</p>\n  <p>The keys in the environment are: \n  <table>\n')
        # SOURCE LINE 15
        for key in sorted(environment):
            # SOURCE LINE 16
            __M_writer(u'      <tr>\n          <td>')
            # SOURCE LINE 17
            __M_writer(escape(key))
            __M_writer(u'</td>\n          <td>')
            # SOURCE LINE 18
            __M_writer(escape(environment[key]))
            __M_writer(u'</td>\n      </tr>\n')
            pass
        # SOURCE LINE 21
        __M_writer(u'  </table>\n\n  </p>\n\n\n')
        # SOURCE LINE 26
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
        __M_writer(u'\n  Learning TurboGears 2.1: Information about TG and WSGI\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


