<%inherit file="local:templates.master"/>
<%def name="title()">
 In School Accounting
</%def>
 ${c.form().display() | n} 
