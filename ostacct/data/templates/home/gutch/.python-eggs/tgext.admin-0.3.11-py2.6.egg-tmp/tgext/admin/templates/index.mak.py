# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317650504.174423
_template_filename='/home/gutch/.python-eggs/tgext.admin-0.3.11-py2.6.egg-tmp/tgext/admin/templates/index.mak'
_template_uri='/home/gutch/.python-eggs/tgext.admin-0.3.11-py2.6.egg-tmp/tgext/admin/templates/index.mak'
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
        models = context.get('models', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<div style="height:0px;"> &nbsp; </div>\n    <h2>TurboGears Admin</h2>\n    This is a fully-configurable administrative tool to help you administer your website.\n    Below is links to all of your models.<br/>    They will bring you to a listing of the objects\n    in your database.\n\n<table class="admin_grid">\n')
        # SOURCE LINE 14
        for model in models:
            # SOURCE LINE 15
            __M_writer(u'    <tr py:for="model in models">\n      <td>\n        <a href=\'')
            # SOURCE LINE 17
            __M_writer(escape(model.lower()))
            __M_writer(u's/\' class="edit_link">')
            __M_writer(escape(model))
            __M_writer(u'</a>\n      </td>\n    </tr>\n')
            pass
        # SOURCE LINE 21
        __M_writer(u'</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\nTurbogears Administration System\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


