from tg import config
from sqlalchemy import Table, ForeignKey, Column, types, Column, Integer, String,Date, Text, MetaData
from sqlalchemy.types import String, Unicode, UnicodeText, Integer, DateTime, \
                             Boolean, Float, Numeric
from sqlalchemy.orm import mapper, relation, backref, join
from ostacct.model import DeclarativeBase, metadata, DBSession, auth
from auth import Schools
from datetime import datetime

class LastRef(DeclarativeBase):
    __tablename__="lastref"
    id = Column(Integer,autoincrement=True, primary_key=True)
    lastrecpt = Column(Integer, nullable=True)
    lastdisburse = Column(Integer, nullable=True)
    lastje = Column(Integer, nullable=True)
    def __repr__(self):
        return '<LastRef = lastref:lastrecpt = %i, lastdisburse = %i, lastje - %i>' %(self.lastrecpt,self.lastdisburse,self.lastje)

class Bank(DeclarativeBase):
    __tablename__="bank"
    id = Column(Integer,autoincrement=True, primary_key=True)
    BankName = Column(String(50), nullable =False)
    accounts_id=Column(Integer,ForeignKey('accounts.id'))
    accounts = relation('Account', backref=backref('bank'),order_by=id)
    school = relation('Schools', backref=backref('bank'))
    school_id = Column(Integer, ForeignKey('schools.id'))
    def __repr__(self):
        return self.id

class Account(DeclarativeBase):
    __tablename__="accounts"
    id = Column(Integer,autoincrement=True, primary_key=True)
    AcctNo = Column(String(6), nullable=False)
    Description = Column(String(75), nullable=False)
    SchoolWide = Column(Boolean, nullable=False)
    SchoolActivity= Column(Boolean, nullable=False)
    def __repr__(self):
        return str(self.id)

class Sub(DeclarativeBase):
    __tablename__="subs"
    id = Column(Integer,autoincrement=True, primary_key=True)
    SubNo = Column(String(5), nullable=False)
    Description = Column(String(75), nullable=False)
    
    #schools_id = relation('Schools', secondary=schools_subs, backref='subs')
    def __repr__(self):
        return str(self.id)

class TempC(DeclarativeBase):
    __tablename__="tempc"
    id = Column(Integer,autoincrement=True, primary_key=True)
    aNo = Column(String(6), nullable=False)
    Description = Column(String(75), nullable=False)

class Activities(DeclarativeBase):
    __tablename__="activities"
    id = Column(Integer,autoincrement=True, primary_key=True)
    SubNo = Column(String(5), nullable=False)
    schools_id=Column(Integer,ForeignKey('schools.id'))
    school = relation('Schools', backref=backref('activities'),order_by=id)
    subs_id=Column(Integer,ForeignKey('subs.id'))
    subs = relation('Sub', backref=backref('activities'),order_by=id)
    def __repr__(self):
        return self.SubNo

class Clubs(DeclarativeBase):
    __tablename__="clubs"
    id = Column(Integer,autoincrement=True, primary_key=True)
    SubNo = Column(String(5), nullable=False)
    schools_id=Column(Integer,ForeignKey('schools.id'))
    school = relation('Schools', backref=backref('clubs'),order_by=id)
    subs_id=Column(Integer,ForeignKey('subs.id'))
    subs = relation('Sub', backref=backref('clubs'),order_by=id)
    def __repr__(self):
        return self.SubNo    

class Obj(DeclarativeBase):
    __tablename__="objs"
    id = Column(Integer,autoincrement=True, primary_key=True)
    ObjNo = Column(String(5), nullable=False)
    Description = Column(String(75), nullable=False)
    def __repr__(self):
        return self.ObjNo

                             
class Chart(DeclarativeBase):                         
    __tablename__="charts"
    id = Column(Integer,autoincrement=True, primary_key=True)
    AcctNo=Column(String(6), nullable=False)
    fund = relation('Fund', backref=backref('charts'),order_by=id)
    fundid = Column(Integer, ForeignKey('funds.id'))
    #bankid = Column(Integer, ForeignKey('bank.id'))
    #bank = relation('Bank',  backref='charts')
    schools_id=Column(Integer,ForeignKey('schools.id'))
    school = relation('Schools', backref=backref('charts'),order_by=id)
    accounts_id=Column(Integer,ForeignKey('accounts.id'))
    accounts = relation('Account', backref=backref('accounts'),order_by=id)

    def __repr__(self):
        return self.AcctNo
       #return '<Chart("%s")>' %(sacct + "   " + self.acctdescription)
        #return sacct + "   " + self.acctdescription

class Typ(DeclarativeBase):                         
    __tablename__="typs"
    id = Column(Integer, primary_key=True)
    typDescription = Column(String(50), nullable=False)
    
    def __repr__(self):
        return '<typDescription = "%s">' %(self.typDescription)

class Fund(DeclarativeBase):                         
    __tablename__="funds"
    id=Column(Integer,primary_key=True)
    fundDescription = Column(String(30))
    def __repr__(self):
        #return '<Fund("%s")>' % (self.fundDescription)
        return str(self.id)

class Payoree(DeclarativeBase):           
    __tablename__="payoree"
    id = Column(Integer,autoincrement=True, primary_key=True)
    service=Column(Boolean,nullable=False)
    fedid=Column(String,nullable=True)
    compname= Column(String(70), nullable=False)
    contname= Column(String(70), nullable=True)
    address= Column(String(70), nullable=True)
    city= Column(String(70), nullable=True)
    state= Column(String(2), nullable=True)
    zip= Column(String(10), nullable=True)
    tel=Column(String(20), nullable=True)              
    def __repr__(self):
             #return "<Payoree('%s')>"  %(self.payoreename)
        return '<payoree: id= "%s", service = "%s", fedid="%s", compname="%s", contname="%s", address="%s", city="%s", state="%s", zip="%s", tel="%s">' \
               % (self.id,  self.service, self.fedid, self.compname, self.contname, self.address, self.city, self.state, self.zip, self.tel)

class Po(DeclarativeBase):
    __tablename__= "po"
    id = Column(Integer,autoincrement=True, primary_key=True)
    payoreeid = Column(ForeignKey('payoree.id'), nullable=True)
    payoreename = relation('Payoree', order_by = id, backref = 'po')
    fund = relation('Fund', order_by=id, backref='po')
    fundid = Column(Integer, ForeignKey('funds.id'))
    ref = Column(Integer, nullable=False)                
    transdate = Column(DateTime, nullable=False)  
    chartid = Column(ForeignKey('charts.id'), nullable=True)
    chart = relation('Chart',order_by=Chart.id, backref='po') 
    subs_id=Column(Integer,ForeignKey('subs.id'))
    subs = relation('Sub', backref=backref('po'),order_by=id)
    amount = Column(Numeric(precision=2, scale=2, asdecimal=True))
    transactid= Column(ForeignKey('transact.id'), nullable=True)
    transact = relation('Transact',order_by=Chart.id, backref='po') 
    podate = Column(DateTime, nullable=False)
    #itemid= Column(ForeignKey('poitem'), nullable=True)
   # item = relation('Poitem',order_by=Poitem.id, backref='po') 
    
 

    
    
    
class Deposit(DeclarativeBase):
    __tablename__="deposit"
    id = Column(Integer,autoincrement=True, primary_key=True)
    total = Column(Numeric(precision=2, scale=2, asdecimal=True))
    #def __init__(self,receipt,fund,chart,transdate,payoreeid,itemdesc,total):
        #self.receipt=receipt
        #self.fund=fund.fundDescription
        #self.chart=str(chart.acct) + "   " + chart.acctdescription
        #self.transdate=transdate
        #self.payoree_id=payoree_id
        #self.itemdesc=itemdesc
        #self.total=total
    def __repr__(self):
        return "<Deposit('%-d')>" %(self.total)
                
class Receipt(DeclarativeBase):
    __tablename__="receipts"
    id = Column(Integer,autoincrement=True, primary_key=True)
    receipt = Column(Integer, nullable=False)
    fundDescription = relation('Fund', order_by = Fund.id, backref='deposit')
    fundid = Column(Integer, ForeignKey('funds.id'))
    chartid = Column(ForeignKey('charts.id'), nullable=True)
    chart = relation('Chart',order_by=Chart.id, backref='receipts')
    transdate = Column(DateTime, nullable=False)
    payoreeid = Column(ForeignKey('payoree.id'), nullable=True)
    payoreename = relation('Payoree', order_by = Payoree.id, backref = 'deposit')
    itemdesc = Column(String(100), nullable=True)
    #splitid = Column(ForeignKey('splits.id'), nullable=True)
    #split = relation('Split',order_by=Chart.id, backref='receipts')
    depositid = Column(ForeignKey('deposit.id'), nullable=True)
    deposit = relation('Deposit',order_by=Deposit.id, backref='receipts')
    amount = Column(Numeric(precision=2, scale=2, asdecimal=True))
    def __repr__(self):
        return "<Receipt(%i,'%s','%s',%date,%i,'%s','%-d')>" %(self.receipt,self.fundDescription,self.chart,self.transdate,self.payoreeid,self.itemdesc,self.deposit,self.total)


clas_table = Table("clas", metadata,
    Column("id", types.Integer,autoincrement=True, primary_key=True),
    Column("clasyear", types.Integer, nullable=True),
    Column("sponsor", types.String(100), nullable=True),
    )

class clas(object):
    pass


class Transtype(DeclarativeBase):                         
    __tablename__= "transtypes"
    id = Column(Integer, primary_key=True)
    transtypeDescription = Column(String(50), nullable=False)
    
    def __repr__(self):
        return '<Transtype( = "%s")>' %(self.transtypeDescription)

class Poitem(DeclarativeBase): 
    __tablename__="poitem"
    id = Column(Integer,autoincrement=True, primary_key=True)
    itemDescription=Column(String(150), nullable=True)
    

class Transact(DeclarativeBase):
    __tablename__="transact"
    id = Column(Integer,autoincrement=True, primary_key=True)
    transtypeid = Column(Integer, ForeignKey('transtypes.id'), nullable=False)
    transtype = relation('Transtype', order_by=id, backref = 'transact')
    fund = relation('Fund', order_by=id, backref='transact')
    fundid = Column(Integer, ForeignKey('funds.id'))
    ref = Column(Integer, nullable=False)                
    transdate = Column(DateTime, nullable=False)
    #po_id = Column(ForeignKey('po.po_id'), nullable=True)
    payoreeid = Column(ForeignKey('payoree.id'), nullable=True)
    payoreename = relation('Payoree', order_by = id, backref = 'transact')
    itemdesc = Column(String(100), nullable=True)
    chart = relation('Chart', order_by = id, backref = 'transact')
    chartid = Column(ForeignKey('charts.id'), nullable=True)
    #schart_id = Column(ForeignKey('charts.id'), nullable=True)
    #account = relation('Account', order_by = id, backref = 'transact')
    #accountid = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    obj = relation('Obj', order_by = Clubs.id, backref = 'transact')
    objid = Column(Integer, ForeignKey('objs.id'), nullable=True)
    schoolid = Column(Integer, ForeignKey('schools.id'), nullable=True)
    club = relation('Clubs', order_by = Clubs.id, backref = 'transact')
    clubid = Column(Integer, ForeignKey('clubs.id'), nullable=True)
    school = relation('Schools',order_by = id, backref='transact')
    bankid = Column(Integer, ForeignKey('bank.id'))
    bank = relation('Bank', order_by = Bank.id, backref='transact')
    depositid=Column(ForeignKey('deposit.id'), nullable=True)
    deposit = relation('Deposit', order_by = Deposit.id, backref='transact')
    amount = Column(Numeric(precision=2, scale=2, asdecimal=True))
    balance = Column(Numeric(precision=2, scale=2, asdecimal=True))
    #originator = Column(ForeignKey('tg_user.user.id'))
    #splitid = Column(ForeignKey('splits.id'), nullable=True)
    #split = relation('Split',order_by=Chart.id, backref='Transact')
        
    def __repr__(self):
        return "<Transact(%i,'%s','%s',%date,%i,'%s','%-d','%-d')>" %(self.ref,self.fundDescription,self.chart,self.transdate,self.payoreeid,self.itemdesc,self.amount,self.balance)
    
class TheEvent(DeclarativeBase):
    __tablename__= 'events'
    id=Column(Integer,autoincrement=True, primary_key=True)
    month= Column(Integer, nullable=False)
    day= Column(Integer, nullable=False)
    year= Column(Integer, nullable=False)
    typ= Column(String(50), nullable=False)
    Description= Column(String(50), nullable=False)
    hyperlink=Column(String(50),  nullable=True)
    doc_id=Column(Integer,ForeignKey('docs.id'))
    doc = relation('Doc', backref=backref('events'),order_by=id) 
    user_id=Column(Integer, ForeignKey('tg_user.user_id'))
    user = relation('User',backref=backref('events'))
    Date_entered = Column(DateTime, default=datetime.now)       
    #def __repr__(self):
       #return "<TheEvent(%i,%i,%i,'%s','%s')>" %(self.month, self.day, self.year,self.typ, self.Description) 
           

class Doc(DeclarativeBase):
    __tablename__= "docs"
    id = Column(Integer,autoincrement=True, primary_key=True)
    name=Column(Text(50), nullable=False)
    description=Column(String(50), nullable=True)
    def __repr__(self):
        return "<Doc(%i,'%s','%s')>" %(self.id, self.name, self.description)
          


mapper(clas, clas_table)
#mapper(club, club_table)
#mapper(vendor, vendor_table)
#mapper(po, po_table)
#mapper(transtype, transtype_table)
#mapper(trans, trans_table)
