# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317651236.1722801
_template_filename=u'/home/gutch/ost/ostacct/ostacct/templates/master.mak'
_template_uri=u'/home/gutch/ost/ostacct/ostacct/templates/master.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer', 'sidebar_top', 'title', 'body_class', 'header', 'meta', 'sidebar_bottom', 'content_wrapper']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n                      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n<head>\n \n \n    ')
        # SOURCE LINE 7
        __M_writer(escape(self.meta()))
        __M_writer(u'\n    <title>')
        # SOURCE LINE 8
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        # SOURCE LINE 9
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer(u'" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        # SOURCE LINE 10
        __M_writer(escape(tg.url('/css/admin.css')))
        __M_writer(u'" />\n\n\n\n<meta name="description" content="Printable reports from Tennessee DOE ereporting" />\n<meta name="keywords" content="DOE,Tennessee,ereporting, e reporting, database eventcalendar, Ron Adelman, Fiscal Consultant," />\n<meta name="author" content="Ron Adelman" />\n<meta http-equiv="content-type" content="text/html;charset=UTF-8" />\n\n\t</head>\n\n\n<body class="')
        # SOURCE LINE 22
        __M_writer(escape(self.body_class()))
        __M_writer(u'">\n\n')
        # SOURCE LINE 24
        __M_writer(escape(self.header()))
        __M_writer(u'\n<ul id="nav">\n\t<li><a href="#"><a href="/index">Home</a></a></li>\n\n\t\n\n\t<li><a href=>E reporting</a>\n\t\t<ul>\n                    <li><a href="/SampleAFR.pdf">Sample - EXCEL AFR </a></li>  \n                     <li><a href="/SampleSubAFR.pdf">Sample - EXCEL AFR(Sub Fund)</a></li> \n                     <li><a href="/graphs.docx">Sample of some graphs</a></li> \n                    <li><a href="/WxPyETn">More WxPyETn</a></li>  \n\t\t    </ul>\n\t</li>\n\t<li><a href=>Local Finance</a>\n\t\t<ul>\n                    <li><a href="/accessit">Application Access </a></li>  \n                     <li><a href="/cal">Event Calendar</a></li> \n                     <li><a href="/manuals">Manuals & Misc</a></li> \n                    <li><a href="/workshops">Spring workshops</a></li>  \n\t\t    </ul>\n\t</li>\n\n\n\n</ul> \n\n  ')
        # SOURCE LINE 51
        __M_writer(escape(self.content_wrapper()))
        __M_writer(u'\n\n  \n  ')
        # SOURCE LINE 54
        __M_writer(escape(self.footer()))
        __M_writer(u'\n</body>\n \n')
        # SOURCE LINE 75
        __M_writer(u'\n\n')
        # SOURCE LINE 78
        __M_writer(u'\n')
        # SOURCE LINE 81
        __M_writer(u'\n\n')
        # SOURCE LINE 83
        __M_writer(u'\n')
        # SOURCE LINE 94
        __M_writer(u'\n\n')
        # SOURCE LINE 108
        __M_writer(u'\n\n')
        # SOURCE LINE 117
        __M_writer(u'\n')
        # SOURCE LINE 125
        __M_writer(u'\n\n\n\n\n')
        # SOURCE LINE 130
        if tg.auth_stack_enabled:
            # SOURCE LINE 131
            __M_writer(u'      <span>\n')
            # SOURCE LINE 132
            if not request.identity:
                # SOURCE LINE 133
                __M_writer(u'            <li id="login" class="loginlogout"><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer(u'">Login</a></li>\n')
                # SOURCE LINE 134
            else:
                # SOURCE LINE 135
                __M_writer(u'            <li id="login" class="loginlogout"><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer(u'">Logout</a></li>\n            <li id="admin" class="loginlogout"><a href="')
                # SOURCE LINE 136
                __M_writer(escape(tg.url('/admin')))
                __M_writer(u'">Admin</a></li>\n')
                pass
            # SOURCE LINE 138
            __M_writer(u'      </span>\n')
            pass
        # SOURCE LINE 140
        __M_writer(u'\n\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 118
        __M_writer(u'\n \n  <div class="foottext">\n    <p>School finance folks are super heros</p>\n  </div>\n  <div class="clearingdiv"></div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_top(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 84
        __M_writer(u'\n  <div id="sb_top" class="sidebar">\n      <h2>My Social network links</h2>\n      <ul class="links">\n        <li><a href="http://www.toddfarmtn.com/">Bed and Breakfast and More</a> - Pat Todds(from my office) business website</li>\n        <li><a href="http://www.thelifechurch.com/">The Life Church</a> Peggy and I changed to here Sept 2011 </li>\n        <li><a href="http://lisabrooksphotos.com/">Lisa Brooks Photography</a> Lisa Brooks(from my office) business website </li> \n      </ul>\n             I probably need to spend more time socializing and less time on the computer and working out.\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 83
        __M_writer(u'  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 77
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 110
        __M_writer(u'\n  <div id="header">\n  \t<h1>\n  \t\tWelcome OSTacct\n\t\t<span class="subtitle">The Inschool Accounting Application</span>\n\t</h1>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 79
        __M_writer(u'\n  <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar_bottom(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 96
        __M_writer(u'\n  <div id="sb_bottom" class="sidebar">\n      <h2>Developing TG2</h2>\n      <ul class="links">\n        <li><a href="http://trac.turbogears.org/query?status=new&amp;status=assigned&amp;status=reopened&amp;group=type&amp;milestone=2.1&amp;order=priority">TG2 Trac tickets</a> What\'s happening now in TG2 development</li>\n        <li><a href="http://trac.turbogears.org/timeline">TG Dev timeline</a> (recent ticket updates, svn checkins, wiki changes)</li>\n        <li><a href="http://svn.turbogears.org/trunk">TG2 SVN repository</a> For checking out a copy</li>\n        <li><a href="http://turbogears.org/2.1/docs/main/Contributing.html#installing-the-development-version-of-turbogears-2-from-source">Follow these instructions</a> For installing your copy</li>\n        <li><a href="http://trac.turbogears.org/browser/trunk">TG2 Trac\'s svn view</a> In case you need a quick look</li>\n        <li><a href="http://groups.google.com/group/turbogears-trunk"> Join the TG-Trunk Mail List</a> for TG2 discuss/dev </li>\n      </ul>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(u'\n\n    <div id="content">\n    <div>\n')
        # SOURCE LINE 61
        if page:
            # SOURCE LINE 62
            __M_writer(u'      <div class="currentpage">\n       Now Viewing: <span>')
            # SOURCE LINE 63
            __M_writer(escape(page))
            __M_writer(u'</page>\n      </div>\n')
            pass
        # SOURCE LINE 66
        __M_writer(u'\n      ')
        # SOURCE LINE 67

        flash=tg.flash_obj.render('flash', use_js=False)
        
        
        # SOURCE LINE 69
        __M_writer(u'\n')
        # SOURCE LINE 70
        if flash:
            # SOURCE LINE 71
            __M_writer(u'        ')
            __M_writer(flash )
            __M_writer(u'\n')
            pass
        # SOURCE LINE 73
        __M_writer(u'      ')
        __M_writer(escape(self.body()))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


