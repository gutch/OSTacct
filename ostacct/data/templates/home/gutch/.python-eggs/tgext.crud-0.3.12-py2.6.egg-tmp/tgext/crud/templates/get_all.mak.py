# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317650509.9260261
_template_filename='/home/gutch/.python-eggs/tgext.crud-0.3.12-py2.6.egg-tmp/tgext/crud/templates/get_all.mak'
_template_uri='/home/gutch/.python-eggs/tgext.crud-0.3.12-py2.6.egg-tmp/tgext/crud/templates/get_all.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header', 'body_class', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'menu_items', context._clean_inheritance_tokens(), templateuri=u'tgext.crud.templates.menu_items', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, u'menu_items')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        value_list = context.get('value_list', UNDEFINED)
        model = context.get('model', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        menu_items = _mako_get_namespace(context, 'menu_items')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n')
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(u'\n<div id="main_content">\n  ')
        # SOURCE LINE 13
        __M_writer(escape(menu_items.menu_items()))
        __M_writer(u'\n  <div style="float:left; width:80%">\n    <h1 style="margin-top:1px;">')
        # SOURCE LINE 15
        __M_writer(escape(model))
        __M_writer(u' Listing</h1>\n    <div style="margin:1ex 0; width:90%">\n      <a href=\'new\' class="add_link">New ')
        # SOURCE LINE 17
        __M_writer(escape(model))
        __M_writer(u'</a>\n')
        # SOURCE LINE 18
        if tmpl_context.paginators:
            # SOURCE LINE 19
            __M_writer(u'           <span style="margin-left:2em">')
            __M_writer(escape(tmpl_context.paginators.value_list.pager(link='../%ss'%model.lower())))
            __M_writer(u'</span>\n')
            pass
        # SOURCE LINE 21
        __M_writer(u'    </div>\n    <div class="crud_table" style="height:50%; width:90%">\n     ')
        # SOURCE LINE 23
        __M_writer(tmpl_context.widget(value=value_list, action='../'+model.lower()+'s.json', attrs=dict(style="height:200px; border:solid black 3px;")) )
        __M_writer(u'\n    </div>\n  </div>\n</div>\n<div style="clear:both;"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        menu_items = _mako_get_namespace(context, 'menu_items')
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(escape(menu_items.menu_style()))
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(parent.header()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'tundra')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        model = context.get('model', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(escape(tmpl_context.title))
        __M_writer(u' - ')
        __M_writer(escape(model))
        __M_writer(u' Listing\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


