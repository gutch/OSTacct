# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317677102.5855179
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/schools.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/schools.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<script type="text/javascript">\nfunction eclub(me){\nvar schools_id=me.id;\nvar ThePath=\'/Chart/?schools_id=\'+schools_id;\nwindow.location =ThePath\n}\nfunction eact(me){\nvar schools_id=me.id;\nvar ThePath=\'/Chart/?schools_id=\'+schools_id;\nwindow.location =ThePath\n}\nfunction eacct(me){\nvar schools_id=me.id;\nvar ThePath=\'/Chart/?schools_id=\'+schools_id;\nwindow.location =ThePath\n}\n</script>\n\n')
        # SOURCE LINE 23
        __M_writer(u'\n\n\n\n ')
        # SOURCE LINE 27
        __M_writer(c.form().display() )
        __M_writer(u' \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n In School Accounting\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


