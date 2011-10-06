# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317664626.45331
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/manuals.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/manuals.mak'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n <FORM><INPUT onclick=history.go(-1) type=button value=Back></FORM>\n\n    <h2>Links to Manuals, Tables and other Reference Materials for new Finance Directors(let me know if link is bad)</h2>\n<h2><center> Manuals</center></h2>\n    <p> <a href="/man/schacctman.pdf">LEA Accounting Manual</a></p>\n    <p> <a href="/man/CTASbudget2011.pdf">CTAS 2011 Budget Workshop Manual</a></p>\n<p> <a href="/man/July 2011TISUAPM-MarkUp.pdf">The new 2011 Internal School Uniform Accounting Policy Manual</a><font size= 1 color="red" > Changes Highlighted --Added 7/23/2011</font></p>\n<p> <a href="/man/Summary of Revisions to TN Internal SchoolManual_1.doc">Summary of Revisions to the Internal School Uniform Accounting Policy Manual</a></p>\n<h2><center> Reference Materials</center></h2>\n    <p> <a href="http://www.comptroller1.state.tn.us/ca/chart.asp">County Chart of Accounts</a></p>\n    <p> <a href="/man/GASB54.pdf">GASB 54 Crosswalk</a></p>\n    <p> <a href="/man/IND COST RATES 2011-2012.pdf">20011-2012 Indirect Cost Rates</a></p>\n    <p> <a href="/man/FundBalRes.doc">Fund Balance Resolution Sample needs to be passed every year</a></p>\n\n<p> <a href="/man/ARRA cheat sheet.xls">spread sheet that Wesley created gives ARRA SSMS CFDA Account and sub fund info</a><font size= 1 color="red" > Added 6/9/2011</font></p>\n<p> <a href="/man/2011-2012.xls">2011-2012 salary schedule</a><font size= 1 color="red" > Added 6/9/2011</font></p>\n<p> <a href="/man/2ndtier template.xls">MOE template for testing 2012 budget includes formulas for 2nd tier</a><font size= 1 color="red" > Added 6/9/2011</font></p>\n<p> <a href="/man/FTTTBUDGET_20CHANGE_20REQUEST_20FOR_20YEAR_20I_20Form[1]-1.docx">FTTT Budget amendment request pre 2011 for summer 2011</a><font size= 1 color="red" > Added 6/10/2011</font></p>\n<p> <a href="/man/FTTTBUDGETAMENDMENTWORKSHEET(1).xls">FTTT Amendment worksheet sample</a><font size= 1 color="red" > Added 6/10/2011</font></p>\n<p> <a href="/man/County_Fiscal_Year_End.pdf">Local Government Closing Instructions</a><font size= 1 color="red" > Added 6/13/2011</font></p>\n<p> <a href="/man/Combined_FYE.pptx">Local Government Closing Power Point</a><font size= 1 color="red" > Added 6/13/2011</font></p>\n<p> <a href="http://www.michie.com/tennessee/lpext.dll?f=templates&fn=main-h.htm&cp=tncode">Lexis Nexis Tennessee Code</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\nLinks to Reference Manuals, Tables, and Miscellaneous\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


