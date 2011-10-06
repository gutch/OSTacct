# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317650509.9355121
_template_filename=u'/home/gutch/.python-eggs/tgext.crud-0.3.12-py2.6.egg-tmp/tgext/crud/templates/menu_items.mak'
_template_uri=u'/home/gutch/.python-eggs/tgext.crud-0.3.12-py2.6.egg-tmp/tgext/crud/templates/menu_items.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['menu_style', 'menu_items']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_style(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<style>\n#menu_items {\n  padding:0px 12px 0px 2px;\n  list-style-type:None;\n  float:left; \n  padding-left:0px;\n  }\n</style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,path='../'):
    context.caller_stack._push_frame()
    try:
        sorted = context.get('sorted', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n    <div id="menu_items">\n        <ul>\n')
        # SOURCE LINE 15
        if hasattr(tmpl_context, 'menu_items'):
            # SOURCE LINE 16
            for lower, item in sorted(tmpl_context.menu_items.iteritems()):
                # SOURCE LINE 17
                __M_writer(u'            <li><a href="')
                __M_writer(escape(path))
                __M_writer(escape(lower))
                __M_writer(u's">')
                __M_writer(escape(item.__name__))
                __M_writer(u'</a></li>\n')
                pass
            pass
        # SOURCE LINE 20
        __M_writer(u'        </ul>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


