<%inherit file="local:templates.master"/>

<script type="text/javascript">
function edit(me){
var event=me.id;
var ThePath='/eventedit?id='+event;
window.location =ThePath
}
</script>
<script type="text/javascript">
function delevent(me){
var event=me.id;
var ThePath='/delevent?id='+event;
window.location =ThePath
}
</script>
<script type="text/javascript">
(document).ready(
    function(){
jQuery("#grid").jqGrid('navGrid','#pager',
  { edit:false,view:false,add:false,del:false,search:false,
    beforeRefresh: function(){
        alert('In beforeRefresh');
        grid.jqGrid('setGridParam',{datatype:'json'}).trigger('reloadGrid');
    }
  })

</script>

<%def name="title()">
 Calendar of Events
</%def>
<table border="0">
<tr>
<td><FORM METHOD = "LINK" ACTION= "AddEvent"><INPUT TYPE="SUBMIT" VALUE="ADD CALENDAR EVENTS" ></FORM></td>


<td><FORM METHOD = "LINK" ACTION= "cal"><INPUT TYPE="SUBMIT" VALUE="BACK TO CALENDAR VIEW" ></FORM></td>
</tr></table><br>

 ${c.form().display() | n} 
