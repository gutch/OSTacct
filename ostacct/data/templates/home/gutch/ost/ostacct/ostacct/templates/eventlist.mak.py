# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317674649.511318
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/eventlist.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/eventlist.mak'
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
        __M_writer(u'\n\n<script type="text/javascript">\nfunction edit(me){\nvar event=me.id;\nvar ThePath=\'/eventedit?id=\'+event;\nwindow.location =ThePath\n}\n</script>\n<script type="text/javascript">\nfunction delevent(me){\nvar event=me.id;\nvar ThePath=\'/delevent?id=\'+event;\nwindow.location =ThePath\n}\n</script>\n<script type="text/javascript">\n(document).ready(\n    function(){\njQuery("#grid").jqGrid(\'navGrid\',\'#pager\',\n  { edit:false,view:false,add:false,del:false,search:false,\n    beforeRefresh: function(){\n        alert(\'In beforeRefresh\');\n        grid.jqGrid(\'setGridParam\',{datatype:\'json\'}).trigger(\'reloadGrid\');\n    }\n  })\n\n</script>\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n<table border="0">\n<tr>\n<td><FORM METHOD = "LINK" ACTION= "AddEvent"><INPUT TYPE="SUBMIT" VALUE="ADD CALENDAR EVENTS" ></FORM></td>\n\n\n<td><FORM METHOD = "LINK" ACTION= "cal"><INPUT TYPE="SUBMIT" VALUE="BACK TO CALENDAR VIEW" ></FORM></td>\n</tr></table><br>\n\n ')
        # SOURCE LINE 41
        __M_writer(c.form().display() )
        __M_writer(u' \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n Calendar of Events\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


