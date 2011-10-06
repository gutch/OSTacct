# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317651236.1537831
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/index.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/index.mak'
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
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(escape(parent.sidebar_top()))
        __M_writer(u'\n\n<div id="getting_started">\n  <h2>openschooltech  (what is it?)</h2>\n  <p>Just a name -- A Tennessee DOE Fiscal Consultant Picked for his web-site. </p>\n  <ol id="what_is_it">\n    <li class="getting_started">\n      <h3>Why does he need a web-site?</h3>\n      <p> Its me; Ron Adelman and my hobby is developing computer applications and I wanted to make them available even if they aren\'t ever used.  I know they are useful and until you try them you won\'t ever know how useful they really are.  Also, the DOE web-site seems to have been neglected for Local Finance stuff so I have some links to some reference material.  If you can think of some vague hard to find links or reference material I have omitted, then please email me. </p>\n    </li>\n\n    <li class="getting_started">\n      <h3>What else?</h3>\n      <p> That is all for now, but work is ongoing for an opensource webbased school accounting application\n\t  as-well-as a church web-site that will highlight the various ministries within the church. <br>\n\nAs of 09/16/2011 I haven\'t done any work on the school accounting application, but am picking up some knowledge that could be used in that endeavor when I get back to it.<br><br>  Will probably get back to it now.  I just applied for Medicare and want this done when I retire, but first I need to set up some pages for Grandchildren pictures.  This is the youngest below.\n  </p>\n<img src="pictures/jack/JK439.jpg" height=150 width= 120 border="0"> </a>\n<img src="pictures/jack/JK474.jpg" height=150 width= 120 border="0"> </a>\n<img src="pictures/jack/JK497.jpg" height=150 width= 120 border="0"> </a>\n<img src="pictures/jack/JK501.jpg" height=150 width= 120 border="0"> </a>\n  </ol>\n</div>\n<div class="clearingdiv" />\n<div class="notice"> My mission for retirement is to give my wants priority over my needs.\n</div>\n\n')
        # SOURCE LINE 35
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
        __M_writer(u'\n  Welcome to OpenSchoolTech.com: A worthy effort at greatness\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


