<%inherit file="local:templates.master"/>

<script type="text/javascript">
function eclub(me){
var schools_id=me.id;
var ThePath='/Chart/?schools_id='+schools_id;
window.location =ThePath
}
function eact(me){
var schools_id=me.id;
var ThePath='/Chart/?schools_id='+schools_id;
window.location =ThePath
}
function eacct(me){
var schools_id=me.id;
var ThePath='/Chart/?schools_id='+schools_id;
window.location =ThePath
}
</script>

<%def name="title()">
 In School Accounting
</%def>



 ${c.form().display() | n} 
