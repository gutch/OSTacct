# -*- coding: utf-8 -*-
"""Main Controller"""
from tg import expose, flash, require, url, request, redirect,validate
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from tgext.admin.tgadminconfig import TGAdminConfig
from tgext.admin.controller import AdminController
from repoze.what import predicates
from ostacct.lib.base import BaseController
from ostacct.model import Schools, Bank, Fund, Account, Obj,Sub,TempC,Activities, Typ, TheEvent, Receipt, Chart,User,Deposit, Payoree,LastRef,Transtype,Transact, Clubs, Doc, DBSession, metadata
from ostacct import model
from ostacct.controllers.secure import SecureController
#from tgext.menu import navbar, sidebar, menu
from pylons import tmpl_context as c
from ostacct.controllers.error import ErrorController
import tw2.core as twc
import tw2.forms as twf
import tw2.dynforms as twd
from sqlalchemy.orm import eagerload
import transaction
from tw2.jqplugins.jqgrid.widgets.core import jqGridWidget
#import tw2.jqplugins.jqgrid
#from tw2.jquery.plugins.jqgrid.base import word_wrap_css
import re, datetime, calendar
from datetime import datetime
import os
import shutil
from pkg_resources import resource_filename
import simplejson as json
from webob import Request

__all__ = ['RootController']
def urlgetit():
    try:
        theurl=request.url
        usertest=int(theurl[theurl.find('=')+1:])
    except:
        usertest=0
    return usertest
#*****************************************************************
#NEW VENDOR FORM                                                          ****
#******************************************************************
class Newvendor(twf.TableForm):
    title ="New vendor"
    class namesfs(twf.FieldSet):
        class child(twf.TableLayout):
            id='names'
            Vendor_name=twf.TextField(size=50, validator=twc.Required)
            Contact_name=twf.TextField(size=50)
    class addressfs(twf.FieldSet):        
        class child(twf.TableLayout):
            id='address'
            #extra_reps = 1
            Address=twf.TextField(size=75)
    class citystatefs(twf.FieldSet):
        class child(twf.GridLayout):
            id='city_state'
            extra_reps = 1
            City=twf.TextField(size= 37)
            State=twf.TextField(size= 37)
            Zip=twf.TextField(size= 20)
    class For_feds(twf.FieldSet):
        class child(twd.HidingTableLayout):
            Type=twd.HidingRadioButtonList(label_text='Vendor type', options=('Service Only','Other'), 
                                           mapping={'Service Only':[ 'FedId']} )
            FedId=twf.TextField(size=20)

#*****************************************************************
#PO FORM                                                          ****
#******************************************************************
class PO(twf.TableForm):
    title ="Purchase Order"
    class venddate(twf.FieldSet):
        class child(twf.GridLayout):
            id='Po_number_and_date'
            extra_reps = 1
            Po_Date=twd.CalendarDatePicker()
            Po_number=twf.TextField(size= 20)
    class Vend(twf.FieldSet):
        class child(twf.TableLayout):
            id='Payee'
            options=DBSession.query(Payoree).all()#payoree.compname#.order_by(payoree.compname).all()
            opt=[]
            for r in options:
                opt.append(r.compname)
            Payee=twf.SingleSelectField(options=opt, label_text='Vendor')
    class Purchase(twf.FieldSet):
        class child(twd.GrowingGridLayout):
            Description = twf.TextField( size=45)
            Price = twf.TextField(size=20)
            Quantity =  twf.TextField(size=20)
            Amount =  twf.TextField(size=20)
    class  TotalPurchase(twf.TextField):
        size=20
    class Charge_to(twf.FieldSet):
        class child(twd.GrowingGridLayout):
            options=DBSession.query(Account).all()#payoree.compname#.order_by(payoree.compname).all()
            opt1=[]
            for r in options:
                opt1.append(r.AcctNo +  " - "+ r.Description)
            Account = twf.SingleSelectField(options=opt1, label_text='Accounts')
            Amount =  twf.TextField(size=20)
    class  Total_chart_to(twf.TextField):
        size=20  
   
#*****************************************************************
#Accountl setup                                                         ****
#******************************************************************
class curS():
    curSchool=""

class chartsel( twf.TableForm):

    class child(twd.Shuttle):
        id='chartsel'
        label="testing"
        default_selected=[]      
        options=[]
        #size=250
 #*****************************************************************
#school jqgrid setup                                                         ****
#****************************************************************** 
class school(jqGridWidget): 
    entity=DBSession.query(Schools).order_by(Schools.name)
    id='grid'    
    rows=15#kwargs.get('rows')
    page=1#kwargs.get('page')
    sord='desc'#kwargs.get('sord')
    name='schoolname'#kwargs.get('sidx')
    offset = (int(page)-1) * int(rows)
        #if (query):
            #d = {qtype:query}
           # allschools = DBSession.query(Schools).filter_by(**d)
        #else:
    allschools = DBSession.query(Schools).order_by(Schools.name)
    records = allschools.count()
    total=int(records)/int(rows)
    totaltest=total*rows
    if totaltest>total:total=total+1
    total=-1*-int(total)
    pageschools=allschools
    rows=[{'id':schools.id,'schoolname':schools.name,   'address':schools.address,  'city':schools.city, 'state':schools.state,
            'zip':schools.zipcode, 'gradespan':schools.gradespan, 
             'accounts':"<input style='height:22px;width:35px;' type='button' value='Acct'  id=%s" %"t"+str(schools.id)+ " onclick="'"return eacct(this)"'" />",
            'activities': "<input style='height:22px;width:35px;' type='button' value='Club'  id=%s" %"c"+str(schools.id)+ " onclick="'"return eact(this)"'" />",
            'clubs': "<input style='height:22px;width:35px;' type='button' value='Ath'  id=%s" %"a"+str(schools.id)+ " onclick="'"return eclub(this)"'" />"
           }for schools in pageschools]
   
   # rows = [{'id'  : str(schools.id),
     #           'cell':	[schools.name,schools.address,schools.city,schools.state,
    #                      schools.zipcode,schools.gradespan,
    #                    ]}for schools in pageschools]  
    options = {
        'pager' : 'module-0-demo_pager',                
        'caption' : 'Schools',
        'data' : rows,
        'datatype' : 'local',
        'colNames':[ 'School name','Address','City','State','Zip','Gradespan', 'Accounts', "Activities", "Clubs"],
        'colModel' : [
                   {'name':'schoolname', 'index':'schoolname', 'width':190, 'align':'left'},
                    {'name':'address', 'index':'address', 'width':190, 'align':'left'},
                    {'name':'city', 'index':'city', 'width':160, 'align':'left'},
                    {'name':'state', 'index':'state', 'width':40, 'align':'left'},
                    {'name':'zip', 'index':'zip', 'width':60, 'align':'left'},
                    {'name':'gradespan', 'index':'gradespan', 'width':85, 'align':'center'},
                    {'name':'accounts', 'index':'accounts', 'width':85, 'align':'center', 'sort':False},
                    {'name':'activities', 'index':'activities', 'width':85, 'align':'center', 'sort':False},
                    {'name':'clubs', 'index':'clubs', 'width':85, 'align':'center', 'sort':False},
                        ],
        'rowNum':15,
        'rowList':[10,20,50],
        'viewrecords':True,
        'imgpath': 'scripts/jqGrid/themes/green/images',
        'width': 900,
        'height': 'auto',

    }


class Event(twf.TableForm):
    action='advent'
    Event_Date=twf.CalendarDatePicker(validator=twc.DateValidator)
    Event_Type=twf.RadioButtonList(options= ("E_Report Due", "FACTS report due", "Printed Report Due","Emailed report due", "Local Finance Event", "Federal Programs  Event", "Application Due",   "Other Event"),value="Application Due",validator=twc.Required )
    Description=twf.TextField(size=45,validator=twc.Required)
    class Link_a_Doc(twf.FieldSet):
       class child(twf.GridLayout):
           id="Link_a_Document"
           extra_reps = 1
           upbut=twf.Button(value= "Upload Doc", attrs = {'onclick': 'window.location ="/uploadeventdoc"'})
           model.DBSession.flush()
           options=None 
           options=DBSession.query(Doc).all()
           opt=[]
           for r in options:
                opt.append(str(r.name))
           Select_a_Document_for_Event=twf.SingleSelectField(options=opt, label_text='Select a document to link to the event')   

class EditEvent(twf.TableForm):
    action='edvent'
    event_date=None
    Event_Type=None
    Description=None
    thisevent=None
    #valevent= request.environ['QUERY_STRING']
    valevent=urlgetit()
    try: 
	    #if valevent:valevent=int(valevent[valevent.find('=')+1:]) 
	    if valevent: thisevent=DBSession.query(TheEvent).filter_by(id=valevent).one()
	    Event_Date=twf.CalendarDatePicker(validator=twc.Required,value=str(thisevent.month)+"/"+str(thisevent.day)+"/"+str(thisevent.year))
	    Event_Type=twf.RadioButtonList(options= ("E_Report Due", "FACTS report due", "Printed Report Due","Emailed report due", "Local Finance Event", 	       "Federal Programs  Event", "Application Due",   "Other Event"),validator=twc.Required,value=thisevent.typ )
	    Description=twf.TextField(size=45,validator=twc.Required, value=thisevent.Description)
    except:
        pass   
	class Link_a_Doc(twf.FieldSet):
	    class child(twf.GridLayout):
		    id="Link_a_Document"
		    extra_reps = 1
            valevent=0
            valevent=urlgetit()
            print valevent
            upbut=twf.Button(value= "Upload Doc", attrs = {'onclick': 'window.location ="/uploadeventdoc"'})
            model.DBSession.flush()
            options=None 
            options=DBSession.query(Doc).all()
            opt=[]
            if valevent>0:
                thisevent=DBSession.query(TheEvent).filter_by(id=int(valevent)).one()                    
                for r in options:
                    opt.append(str(r.name))
                Select_a_Document_for_Event=twf.SingleSelectField(options=opt, label_text='Select a document to link to the event',value=thisevent.doc)   
            else:
                Select_a_Document_for_Event=twf.SingleSelectField(options=[], label_text='Select a document to link to the event')
    
class uploaddoc(twf.TableForm):
    action='uploadget'
    title = 'Doc_upload'
    class doc(twf.TableLayout):
        backbut=twf.Button(value= "Back to Add Event", attrs = {'onclick': 'window.location ="/AddEvent"'})
        Description=twf.TextField(size=100)
        FileLbl=twf.Label(text="_ will be replaced in file name with spaces")
        filename=twf.FileField()


#*****************************************************************
#event calendar jqgrid setup                                                         ****
#****************************************************************** 
class eventgrid(jqGridWidget): 
    #entity=DBSession.query(TheEvent).order_by(TheEvent.year,TheEvent.month,TheEvent.day)
    id='grid'
   # if kwargs:    
  #      rows=kwargs.get('rows')
   #     page=kwargs.get('page')
   #     sord=kwargs.get('sord')
   #     name=kwargs.get('sidx')
    #else:
    rows=15
    page=1
    sord='Date'
    name='Date'
    offset = (int(page)-1) * int(rows)
        #if (query):
            #d = {qtype:query}
           # allschools = DBSession.query(Schools).filter_by(**d)
        #else:
    model.DBSession.flush()
    allevents=None
    allevents = DBSession.query(TheEvent).order_by(TheEvent.year,TheEvent.month,TheEvent.day)
    #url=""
    records = allevents.count()
    total=int(records)/int(rows)
    totaltest=total*rows
    if totaltest>total:total=total+1
    total=-1*-int(total)
    pageevents=allevents
    rows=[{'id':events.id,'Date':str(events.month) +"/" + str(events.day) + "/" + str(events.year), 'Type':events.typ, 'Description':events.Description,'Document':"<a href= /eventdoc/" + (json.dumps(str(events.doc))[json.dumps(str(events.doc)).find(",")+1:json.dumps(str(events.doc)).rfind(",")].strip("'"))+ "/" +json.dumps(str(events.doc))[json.dumps(str(events.doc)).find(",")+1:json.dumps(str(events.doc)).rfind(",")].strip("'") +">"+json.dumps(str(events.doc))[json.dumps(str(events.doc)).find(",")+1:json.dumps(str(events.doc)).rfind(",")].strip("'")
+"</a>",
'Edit':"<input style='height:22px;width:35px;' type='button' value='Edit'  id=%s" %str(events.id)+ " onclick="'"return edit(this)"'" />",
'Delete':"<input style='height:22px;width:45px;' type='button' value='Delete'  id=%s" %str(events.id)+ " onclick="'"return delevent(this)"'" />"
           }for events in pageevents]
   

    options = {
        'pager' : 'module-0-demo_pager',                
        'caption' : 'Events',
        
        'data' : rows,
        'datatype' : 'local',
        'colNames':[ 'Date','Event Type','Event Desc','Events Documents','Edit','Delete'],#, '’showlink’Accounts', "Activities", "Clubs"],
        'colModel' : [
                  # {'name':'Month', 'index':'Month', 'width':40, 'align':'left'},
                    {'name':'Date', 'index':'Date', 'width':60, 'align':'left'},
                    #{'name':'Year', 'index':'Year', 'width':60, 'align':'left'},
                    {'name':'Type', 'index':'Type', 'width':150, 'align':'left'},
                    {'name':'Description', 'index':'Description', 'width':350, 'align':'left'},
                    {'name':'Document', 'index':'Document', 'width':200, 'align':'left'},
                    {'name':'Edit', 'index':'Edit', 'width':85, 'align':'center', 'sort':False},
                    {'name':'Delete', 'index':'Delete', 'width':85, 'align':'center', 'sort':False},
                       ],
        'rowNum':15,
        'rowList':[10,20,50],
        'viewrecords':True,
        'imgpath': 'scripts/jqGrid/themes/green/images',
        'width': 900,
        'height': 'auto',
        
    }
       
                              
class RootController(BaseController):
    """
    The root controller for the ostacct application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    secc = SecureController()

    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()
    
    #@navbar('index',sortorder=0 )
    @expose('ostacct.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')
        
   # @navbar('WxPyETn')
    @expose('ostacct.templates.WxPyETn')
    def WxPyETn(self):
        """Handle the 'about' page."""
        return dict(page='about')
 
    @expose('ostacct.templates.accessit')
    def accessit(self):
        """Links to access forms."""
        return dict(page='forms')

    @expose('ostacct.templates.SamAFR')
    def SamAFR(self):
        """link to sample AFR's"""
        return dict(page='Sample AFR')


    @expose('ostacct.templates.manuals')
    def manuals(self):
        """Link to manuals for new finance directors."""
        return dict(page='Manuals')


    @expose('ostacct.templates.workshops')
    def workshops(self):
        """Link to manuals for new finance directors."""
        return dict(page='Workshops')

    @expose('ostacct.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(params=kw)

    @expose('ostacct.templates.authentication')
    def auth(self):
        """Display some information about auth* on this application."""
        return dict(page='auth')

    @expose('ostacct.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('ostacct.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose('ostacct.templates.login')
    def login(self, came_from=url('/')):
        """Start the user login."""
        login_counter = request.environ['repoze.who.logins']
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')
        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from='/'):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ['repoze.who.logins'] + 1
            redirect('/login', came_from=came_from, __logins=login_counter)
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)
        redirect(came_from)

    @expose()
    def post_logout(self, came_from=url('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)
#++++++++START MY CON@TROLLERS+++++++++++++
    #@navbar('local Finance || calendar event')
    @expose('ostacct.templates.eventcal')
    def cal(self, *args, **kw):
        calendar.setfirstweekday(6)
        year = ['January', 
                    'February', 
                    'March', 
                    'April', 
                    'May', 
                    'June', 
                    'July', 
                    'August', 
                    'September', 
                    'October', 
                    'November', 
                    'December'] 
        
        today = datetime.date(datetime.now())  
        current = re.split('-', str(today)) 
        current_no = int(current[1]) 
        current_month = year[current_no-1] 
        current_day = int(re.sub('\A0', '', current[2])) 
        current_yr = int(current[0]) 
        month = calendar.monthcalendar(current_yr, current_no) 
        nweeks=len(month)
        weeklist=[]
        for w in range(0,nweeks): 
			weeklist.append(month[w])
        #event = DBSession.query(Event).filter_by(month=int(current_month)).all()
        if kw:

            if int(kw['month'])>current_no:
                current_no=int(kw['month'])
                current_yr=int(kw['year'])
                current_day=50
                month= calendar.monthcalendar(current_yr, current_no) 
                nweeks=len(month)
                current_month = year[current_no-1] 
                weeklist=[]
                for w in range(0,nweeks): 
                    weeklist.append(month[w])
            else:
                if int(kw['year'])>current_yr:
		    current_no=int(kw['month'])
		    current_yr=int(kw['year'])
		    current_day=50
		    month= calendar.monthcalendar(current_yr, current_no) 
		    nweeks=len(month)
		    current_month = year[current_no-1] 
		    weeklist=[]
		    for w in range(0,nweeks): 
		       weeklist.append(month[w])
		        
        even = DBSession.query(TheEvent).filter_by(month=int(current_no)).all()
        events=[]
        rawevents=[]
        doneday=[]
        dontdouble=False
        for row in even:
            if row:
                if row.doc:
                    doclink=row.doc.name
                    doclinkdesc=row.doc.description
                    public_dirname = os.path.join(os.path.abspath(resource_filename('ostacct', 'public')))
                    doc_dirname = os.path.join(public_dirname, 'eventdoc')
                else: doclink=None
                #doclink = os.path.join(doc_dirname, str(row.docs))
                rawevents.append([row.month,row.day,row.year,row.typ,row.Description,doclink]) 
            else:
                doc="something"
                doclink=""
                doclinkdesc=""
                rawevents.append([row.month,row.day,row.year,row.typ,row.Description,doclink])
        doneit=False
        dontdouble=[] 
        for m, d, y,typ,Desc,doc in rawevents:
            Thisday=d
            devent=[]           
            for m, d, y,typ,Desc,doc in rawevents:                 
                if d==Thisday:
                    devent.append((typ,Desc,doc))
                    devent.append(("-----------------------","",""))
            for row in dontdouble:
                if row==Thisday:
                    doneit=True
            dontdouble.append(Thisday)
            if doneit==False:                
                events.append((m,Thisday,y,devent))
                #events.append(("--","--","----","-----"))
            doneit=False         
        #events.append([row.month.day,row.year,row.typ,row.Description,doclink])  
        return dict(page='Calendar', year=year, today=today, current=current, current_no=current_no, 
                    current_month=current_month, current_day=current_day, current_yr=current_yr, 
                     month = month,  nweeks = nweeks , weeklist=weeklist,events=events)

    @require(predicates.has_permission('calendar', msg=l_('Only for Calendar Maintainers')))   
    @expose('ostacct.templates.eventedit')
    #@validate(Event, error_handler=AddEvent) 
    def AddEvent(self, *args, **kwargs):

    
       c.form=Event()
       

       return dict(page = "Add a New Event")
   
    @require(predicates.has_permission('calendar', msg=l_('Only for Calendar Maintainers')))
    @expose('ostacct.templates.eventedit')
    def eventedit(self, *args, **kwargs):


       EditEvent.valevent=urlgetit()
       c.form=EditEvent()
       return dict(page = "Edit an Event")

    @expose('ostacct.templates.eventedit.mak')
    #@validate(Event, error_handler=AddEvent)        
    def advent(self, *args, **kw):
       if kw:
           edate=re.split('/', str(kw['Event_Date']))
           emonth=int(edate[0])
           eday=int(edate[1])
           eyear=int(edate[2])
           C=model.TheEvent()
           C.month=emonth
           C.day=eday
           C.year=eyear
           if kw['Event_Type']: C.typ=kw['Event_Type']
           C.Description=kw['Description']
           try:
               adddoc=DBSession.query(Doc).filter_by(name=kw["Link_a_Document:0:Select_a_Document_for_Event"]).one()
           except:
               adddoc=None
           C.doc=adddoc
           model.DBSession.add(C)
           transaction.commit()
           model.DBSession.flush()
           flash(kw['Description'] +" was successfully added")
           redirect("eventlist")
       else:      
           flash("some sort of problem")
           redirect("AddEvent")


    @expose('ostacct.templates.simple_mako.mak')
    def delevent(self, *args, **kw):
        try:
            valevent= urlgetit()
    	    if valevent:
                for d in DBSession.query(TheEvent).filter_by(id=int(valevent)):
                    DBSession.delete(d)
                transaction.commit()
                model.DBSession.flush()
                msg= name + "was deleted"
                flash(msg)
                redirect("eventlist")
        except:
            msg= "  Oh shit"
            flash(msg)
            redirect('eventlist')
        return dict( page='Deleting an Event',msg=msg)
  

    @expose('ostacct.templates.eventedit.mak')
    #@validate(Event, error_handler=eventedit)        
    def edvent(self, *args, **kw):
        try:
           valevent= urlgetit()
    	   #if valevent:valevent=int(valevent[valevent.find('=')+1:]) 
    	   if valevent: thisevent=DBSession.query(TheEvent).filter_by(id=valevent).one()
           for d in DBSession.query(TheEvent).filter_by(id=int(ThisEvent)):
               DBSession.delete(d)
           transaction.commit()
           model.DBSession.flush()
           edate=re.split('/', str(kw['Event_Date']))
           emonth=int(edate[0])
           eday=int(edate[1])
           eyear=int(edate[2])
           C=model.TheEvent()
           C.month=emonth
           C.day=eday
           C.year=eyear
           if kw['Event_Type']: C.typ=kw['Event_Type']
           C.Description=kw['Description']
           try:
               adddoc=DBSession.query(Doc).filter_by(name=kw["Link_a_Document:0:Select_a_Document_for_Event"]).one()
           except:
               adddoc=None
           C.doc=adddoc
           model.DBSession.add(C)
           transaction.commit()
           model.DBSession.flush()
           flash(kw['Description'] +" was successfully added.--Add another.")
           redirect("AddEvent")
        except:      
           flash("some sort of problem")
           redirect("AddEvent")  


    @expose('ostacct.templates.ostacct')
    def uploadeventdoc(self, *args, **kw):
        c.form =uploaddoc()
        return dict(page = "Upload a file to link from event calendar")

    @expose('ostacct.templates.ostacct')
    def uploadget(self, *args, **kw):
       if kw:
           public_dirname = os.path.join(os.path.abspath(resource_filename('ostacct', 'public')))
           doc_dirname = os.path.join(public_dirname, 'eventdoc')
           fn=kw['doc:filename'].filename
           fn=str(fn).replace(" ","")
           C= model.Doc()
           C.name=fn    
           C.description=kw['doc:Description']
           model.DBSession.add(C)
           transaction.commit()        
           model.DBSession.flush()
           doc=DBSession.query(Doc).filter_by(name=str(fn)).one()
           doc_path = os.path.join(doc_dirname, str(doc.name))
           try:
               os.makedirs(doc_path)
           except OSError:
               #ignore if the folder already exists
               pass
           doc_path = os.path.join(doc_path, str(fn))
           f = file(doc_path, "w")
           f.write(kw['doc:filename'].value)
           f.close()
           newdoc_path=os.path.join(public_dirname, 'eventdoc')
           newdoc_path=os.path.join(newdoc_path, str(fn))
           shutil.copyfile(doc_path, fn)
           ostacct.remove_value('AddEvent')
 
           flash("Dccument was successfully created.")
           redirect("AddEvent")
       else:
           flash("some sort of problem")
           redirect("upload")

    @expose('ostacct.templates.eventlist')
    def eventlist(self, *args, **kwargs):
        c.form =  eventgrid()
        return dict( page='Event List')

  
    #@navbar('Vendor' )
    @expose('ostacct.templates.ostacct')
    def Vendor(self, *args, **kw):
        c.form =  Newvendor#().req()
        return dict( page='vendor')


    #@navbar('PO' )
    @expose('ostacct.templates.ostacct.mak')
    def PO(self, *args, **kw):
        c.form =  PO#().req()
        return dict( page='Purchase order')
        
    @expose('ostacct.templates.chart')
    def Chart(self, *args, **kwargs):
        curS.curSchools=kwargs
        self.data=kwargs
        tempsubAll=[]
        subfundsel=[]
        subfundAll=[]
        if kwargs:
            if 'schools_id' in kwargs:
                curSchool=kwargs['schools_id'][1:]
                subtype=kwargs["schools_id"][0]
                if subtype=="c":
                    flabel="Club Sub Funds"
                    selSchool = DBSession.query(Clubs).filter_by(schools_id=int(curSchool)).order_by(Clubs.SubNo).all()
                if subtype=="a":
                    flabel="Athletic Sub Funds"
                    selSchool = DBSession.query(Activities).filter_by(schools_id=int(curSchool)).order_by(Activities.SubNo).all()
                if subtype=="t":
                    flabel="Accounts"
                    selSchool = DBSession.query(Chart).filter_by(schools_id=int(curSchool)).order_by(Chart.AcctNo).all() 
                    for a in selSchool:
                        subfundsel.append(str(a.accounts.AcctNo)+" " +str(a.accounts.Description))
                    for r in DBSession.query(Account).order_by(Account.AcctNo).all():
                        includeit=True
                        for w in subfundsel:
                            if int(w[:4])==int(r.AcctNo):
                                includeit=False
                        if includeit==True and int(r.AcctNo)>1159: subfundAll.append(str(r.AcctNo)+" " +str(r.Description))
                            
                if subtype=="c" or subtype=="a": 
                    for a in selSchool:
                        subfundsel.append(str(a.SubNo)+" " +str(a.subs.Description))
                    for r in DBSession.query(Sub).order_by(Sub.SubNo).all():
                        if subtype=="c" and int(r.SubNo)>799 and int(r.SubNo)<900:
                            includeit=True
                            for w in subfundsel:
                                if int(w[:4])==int(r.SubNo):
                                    includeit=False
                            if includeit==True: subfundAll.append(str(r.SubNo)+" " +str(r.Description)) 
                        if subtype=="a" and int(r.SubNo)>599 and int(r.SubNo)<700:
                            includeit=True
                            for w in subfundsel:
                                if int(w[:4])==int(r.SubNo):
                                    includeit=False
                            if includeit==True: subfundAll.append(str(r.SubNo)+" " +str(r.Description))
            if 'chartsel' in kwargs:
                forFlash=[]
                NEWClubs=[]
                tClub=[]
                    #nSchool=[]
                nSchool=int(curS.curSchools['schools_id'][1:])#int(curSchool)
                subtype=subtype=curS.curSchools["schools_id"][0]#str(subtype)
                nSchool1=DBSession.query(Schools).filter_by(id=int(nSchool)).one()
                if subtype=="c" or subtype=="a":
                    for r in DBSession.query(Sub).order_by(Sub.SubNo).all():
                        if subtype=="c" and int(r.SubNo)>799 and int(r.SubNo)<900:
                            tClub.append(r)
                        if subtype=="a" and int(r.SubNo)>599 and int(r.SubNo)<700:
                            tClub.append(r)
                if subtype=="t":
                    for r in DBSession.query(Account).order_by(Account.AcctNo).all():
                        tClub.append(r)
                select=kwargs['chartsel'][0:-1].split(',')
                Items=()
                lkw=len(select)
                    #Items=pickle.dumps(kw['itemselector'])
                Items=(str(kwargs['chartsel'])[1:lkw])
                if lkw>0:
                    i=0
                    while i <lkw:
                        if subtype=="c" or subtype=="a":
                            if select[i][0:3] !="":
                                nClub=select[i][0:3]
                            else:
                                i=i+1
                                nClub=select[i][0:3]
                        if subtype=="t":
                            if select[i][0:4] !="":
                                nClub=select[i][0:4]
                            else:
                                nClub=select[i][0:4]
                        NEWClubs.append(nClub)
                        if subtype=="c" or subtype=="a" and nClub != "":Club1=DBSession.query(Sub).filter_by(SubNo=str(nClub)).one()
                        if subtype=="t":
                            Acct1=DBSession.query(Account).filter_by(AcctNo=str(nClub)).one()
                        if subtype=="c":
                            schclubs=DBSession.query(Schools).options(eagerload('clubs')).filter_by(id=int(nSchool)).one()
                            schclubClubs=schclubs.clubs
                        if subtype=="a":
                            schclubs=DBSession.query(Schools).options(eagerload('activities')).filter_by(id=int(nSchool)).one()
                            schclubClubs=schclubs.activities
                        if subtype=="t":
                            schclubs=DBSession.query(Schools).options(eagerload('charts')).filter_by(id=int(nSchool)).one()
                            schclubClubs=schclubs.charts
                        doit=True
                        for club in schclubClubs:
                            if str(club)==str(nClub):
                                doit=False
                        if doit==True:
                            if subtype=="c": C=model.Clubs()
                            if subtype=="a": C=model.Activities()
                            if subtype=="t": C=model.Chart()
                            if subtype=="c" or subtype=="a":
                                C.SubNo=str(nClub)
                                C.subs_id=int(Club1.id)
                                C.schools_id=nSchool1.id
                            if subtype=="t":
                                #C.AcctNo=str(nClub)
                                if Acct1.SchoolWide==True and Acct1.SchoolActivity==False:C.fundid=1
                                if Acct1.SchoolWide==False and Acct1.SchoolActivity==True:C.fundid=2
                                if Acct1.SchoolWide==True and Acct1.SchoolActivity==True:C.fundid=3
                                C.AcctNo=str(nClub)
                                C.accounts_id=int(Acct1.id)
                                C.schools_id=int(nSchool1.id)
                            model.DBSession.add(C)
                        i=i+1
                    transaction.commit()
                    model.DBSession.flush()
                if subtype=="c":
                    for d in DBSession.query(Clubs).filter_by(schools_id=int(nSchool)):
                        deleteit=True
                        if len(NEWClubs)>0:
                            for row in NEWClubs:
                                if row <>None:
                                    if int(d.SubNo)==int(row):
                                        deleteit=False
                        if deleteit==True:
                            DBSession.delete(d)
                    transaction.commit()
                    model.DBSession.flush()        

                if subtype=="a":
                    for d in DBSession.query(Activities).filter_by(schools_id=int(nSchool)):
                        deleteit=True
                        if len(NEWClubs)>0:
                            for row in NEWClubs:
                                if row <>None:
                                    if int(d.SubNo)==int(row):
                                        deleteit=False
                        if deleteit==True:
                            DBSession.delete(d)
                    transaction.commit()
                    model.DBSession.flush()
                if subtype=="t":
                    always=[1,20,15,16,17,18,19,6,7,8,9,10,11,12,13,14]
                    forFlash=[1100,1170,1410,1420,1430,1810,1910,2100,2300,2600,3200,3300,3400,3500,3600,3999]
                    for d in DBSession.query(Chart).filter_by(schools_id=int(nSchool)):
                
                        deleteit=True
                        if len(NEWClubs)>0:
                            for row in NEWClubs:
                                if row <>None:
                                    if int(d.accounts.AcctNo)==int(row):
                                        deleteit=False
                                    else:
                                        for z in always:
                                            if d.accounts.id==z:
                                                deleteit=False
                                for tt in forFlash:
                                    if int(row)==int(tt):forFlash.remove(tt)
                        if deleteit==True:
                            DBSession.delete(d)
                    transaction.commit()
                    model.DBSession.flush()
                    if len(forFlash)>0:
                        strFlash=""
                        for row in forFlash:
                            strFlash=strFlash+str(row)
                        flash("You tried to delete the following accounts that cannot be deleted!--- " + strFlash)

        chartsel.child.default_selected=subfundsel            
        chartsel.child.options=subfundAll
        c.form =  chartsel()
        schoolnam=DBSession.query(Schools).filter('id=%i'  %int(curSchool)).one()
        return dict( page=schoolnam.name)
        
        
    #@navbar('schools' )       
    @expose('ostacct.templates.schools')
    def schools(self, *args, **kw):
        c.form =  school()
        
        return dict( page='chart')
        
        
   
