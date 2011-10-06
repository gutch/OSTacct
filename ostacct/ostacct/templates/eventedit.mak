<%inherit file="local:templates.master"/>
<%def name="title()">
Work with Calendar events
</%def>
<FORM><INPUT TYPE="button" VALUE="Back" onClick="history.go(-1);return true;"></FORM> 
 ${c.form.display()|n} 
