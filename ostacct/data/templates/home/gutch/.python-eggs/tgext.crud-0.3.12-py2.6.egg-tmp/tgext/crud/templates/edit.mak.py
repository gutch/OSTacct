# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317668287.035789
_template_filename='/home/gutch/.python-eggs/tgext.crud-0.3.12-py2.6.egg-tmp/tgext/crud/templates/edit.mak'
_template_uri='/home/gutch/.python-eggs/tgext.crud-0.3.12-py2.6.egg-tmp/tgext/crud/templates/edit.mak'
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
        value = context.get('value', UNDEFINED)
        model = context.get('model', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        menu_items = _mako_get_namespace(context, 'menu_items')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n')
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n  <div id="main_content">\n    ')
        # SOURCE LINE 14
        __M_writer(escape(menu_items.menu_items('../../')))
        __M_writer(u'\n  <div style="float:left;" class="crud_edit">\n    <h2 style="margin-top:1px;">Edit ')
        # SOURCE LINE 16
        __M_writer(escape(model))
        __M_writer(u'</h2>\n     ')
        # SOURCE LINE 17
        __M_writer(tmpl_context.widget(value=value, action='./') )
        __M_writer(u'\n  </div>\n  <div style="height:0px; clear:both;"> &nbsp; </div>\n  </div> <!-- end main_content -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        menu_items = _mako_get_namespace(context, 'menu_items')
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n  ')
        # SOURCE LINE 10
        __M_writer(escape(menu_items.menu_style()))
        __M_writer(u'\n  ')
        # SOURCE LINE 11
        __M_writer(escape(parent.header()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 8
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
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


