# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317650473.407408
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/about.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/about.mak'
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
        tg = context.get('tg', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(escape(parent.sidebar_top()))
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(escape(parent.sidebar_bottom()))
        __M_writer(u'\n  <div id="getting_started">\n    <h2>Architectural basics of a quickstart TG2 site.</h2>\n    <p>The TG2 quickstart command produces this basic TG site.  Here\'s how it works.</p>\n    <ol id="getting_started_steps">\n      <li class="getting_started">\n        <h3>Code my data model</h3>\n        <p> When you want a model for storing favorite links or wiki content, \n            the <strong>/model</strong> folder in your site is ready to go.</p>\n        <p> You can build a dynamic site without any data model at all. There \n            still be a default data-model template for you if you didn\'t enable \n            authentication and authorization in quickstart. If you have enabled\n            authorization, the auth data-model is ready-made.</p>\n      </li>\n      <li class="getting_started">\n        <h3>Design my URL structure</h3>\n        <p> The "<span class="code">root.py</span>" file under the \n            <strong>/controllers</strong> folder has your URLs.  When you \n            called the url or this page (<span class="code"><a href="')
        # SOURCE LINE 26
        __M_writer(escape(tg.url('/about')))
        __M_writer(u'">/about</a></span>), \n            the command went through the RootController class to the \n            <span class="code">about</span><span class="code">()</span> method.</p>\n        <p> Those Python methods are responsible to create the dictionary of\n             variables that will be used in your web views (template).</p>\n      </li>\n      <li class="getting_started">\n        <h3>Reuse the web page elements</h3>\n        <p> A web page viewed by user could be constructed by single or \n            several reusable templates under <strong>/templates</strong>. \n            Take \'about\' page for example, each reusable template generating \n            a part of the page.</p>\n\n        <p> <strong><span class="code">about.mak</span></strong> - This is the\n        template that created this page.  If you take a look at this template\n        you will see that there are a lot of wacky symbols, if you are not familiar\n        with <a href="http://www.makotemplates.org">Mako</a> you should probably\n        check out the docs on their site.  </p>\n        \n        <p>Let\'s take a look at what this template does in order of execution.\n        The first thing this template does\n        is inherit from <strong><span class="code">master.mak</span></strong>. We\'ll\n        go into the details of this later, but for now just know that this\n        template is allowed to both call on master.mak, and also override it\'s\n        capabilites.  This inheritance is what gives mako it\'s power to\n        provide reusable templates.\n        </p>\n        <p>But um, whats that \'local:\' stuff about? </p>\n        <p>\n        Well, TG wants to provide re-usable components like tgext.admin, and also\n        provide a way for you to use your default site layouts.  This is done\n        easily by providing a shortcut to the namespace of your project, so the\n        component template finder can find <strong>your</strong> master.html and format \n        itself the way you want it to.\n        </p>\n        <p> The next thing about.mak does is to create a function called title()\n        which provides the title for the document.  This overrides the title\n        method provided by master.mak, and therefore, when the template\n        is rendered, it will use the title provided by this funciton.\n        \n        <p>\n        Next, there are a couple of calls to the master template to set up the \n        boxes you see in the page over on the right, We\'ll examine what\n        these are in the master template in a second.  Finally, we get to the meat\n        of the document, and that\'s pretty much all about.mak does\n        </p>\n        \n        <p> <strong><span class="code">master.mak</span></strong> -\n        This template provides the overall layout for your project, and\n        allows you to override different elements of the overall structure\n        of your default look-and-feel.  Let\'s take a look at this template\n        from top to bottom again.</p>\n        <p>The first 15 lines provide an overall layout for the document,\n        with definitions for the header, title and body.  Each one of these\n        sections has been turned into a method that you can change within your\n        child templates, but you do not have to provide any single one of them\n        TurboGears extensions may however expect these methods to be provided\n        to display their content properly.  Keep this in mind if you decide\n        to alter your master.mak.  You are of course always free to modify\n        your master template, but doing so can render your extensions useless,\n        so tread carefully.</p>\n        \n        <p> The next section describes the overall layout for the body of the\n        document, with flash messages appearing at the top, and self.body()\n        appearing at the bottom.  self.body will take whatever is not defined\n        as a method in your child template and render it in this space.  This\n        is really useful because it allows you to be freestyle with your\n        body definition.  If you don\'t want to override any of the master\n        template defines, all you have to do is inherit the master, and then\n        provide the code you want to appear surrounded by your header and footer.\n        </p>\n        \n        <p>\n        Next are the title, header, footer and sidebar defines.  These are all of\n        course overriddable.\n        </p>\n        \n        <p>The final define sets up the menubar.  This provides some links,\n        as well as a way of highlighing the page you are currently on.\n        </p>\n      </li>\n    </ol>\n    <p>Good luck with TurboGears 2!</p>\n</div\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\nLearning TurboGears 2.1: Quick guide to the Quickstart pages.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


