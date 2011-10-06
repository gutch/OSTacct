<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
                      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
 
 
    ${self.meta()}
    <title>${self.title()}</title>
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/css/style.css')}" />
    <link rel="stylesheet" type="text/css" media="screen" href="${tg.url('/css/admin.css')}" />



<meta name="description" content="Printable reports from Tennessee DOE ereporting" />
<meta name="keywords" content="DOE,Tennessee,ereporting, e reporting, database eventcalendar, Ron Adelman, Fiscal Consultant," />
<meta name="author" content="Ron Adelman" />
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />

	</head>


<body class="${self.body_class()}">

${self.header()}
<ul id="nav">
	<li><a href="#"><a href="/index">Home</a></a></li>

	

	<li><a href=>E reporting</a>
		<ul>
                    <li><a href="/SampleAFR.pdf">Sample - EXCEL AFR </a></li>  
                     <li><a href="/SampleSubAFR.pdf">Sample - EXCEL AFR(Sub Fund)</a></li> 
                     <li><a href="/graphs.docx">Sample of some graphs</a></li> 
                    <li><a href="/WxPyETn">More WxPyETn</a></li>  
		    </ul>
	</li>
	<li><a href=>Local Finance</a>
		<ul>
                    <li><a href="/accessit">Application Access </a></li>  
                     <li><a href="/cal">Event Calendar</a></li> 
                     <li><a href="/manuals">Manuals & Misc</a></li> 
                    <li><a href="/workshops">Spring workshops</a></li>  
		    </ul>
	</li>



</ul> 

  ${self.content_wrapper()}

  
  ${self.footer()}
</body>
 
<%def name="content_wrapper()">

    <div id="content">
    <div>
    % if page:
      <div class="currentpage">
       Now Viewing: <span>${page}</page>
      </div>
    % endif

      <%
      flash=tg.flash_obj.render('flash', use_js=False)
      %>
      % if flash:
        ${flash | n}
      % endif
      ${self.body()}
    </div>
</%def>

<%def name="body_class()">
</%def>
<%def name="meta()">
  <meta content="text/html; charset=UTF-8" http-equiv="content-type"/>
</%def>

<%def name="title()">  </%def>
<%def name="sidebar_top()">
  <div id="sb_top" class="sidebar">
      <h2>My Social network links</h2>
      <ul class="links">
        <li><a href="http://www.toddfarmtn.com/">Bed and Breakfast and More</a> - Pat Todds(from my office) business website</li>
        <li><a href="http://www.thelifechurch.com/">The Life Church</a> Peggy and I changed to here Sept 2011 </li>
        <li><a href="http://lisabrooksphotos.com/">Lisa Brooks Photography</a> Lisa Brooks(from my office) business website </li> 
      </ul>
             I probably need to spend more time socializing and less time on the computer and working out.
  </div>
</%def>

<%def name="sidebar_bottom()">
  <div id="sb_bottom" class="sidebar">
      <h2>Developing TG2</h2>
      <ul class="links">
        <li><a href="http://trac.turbogears.org/query?status=new&amp;status=assigned&amp;status=reopened&amp;group=type&amp;milestone=2.1&amp;order=priority">TG2 Trac tickets</a> What's happening now in TG2 development</li>
        <li><a href="http://trac.turbogears.org/timeline">TG Dev timeline</a> (recent ticket updates, svn checkins, wiki changes)</li>
        <li><a href="http://svn.turbogears.org/trunk">TG2 SVN repository</a> For checking out a copy</li>
        <li><a href="http://turbogears.org/2.1/docs/main/Contributing.html#installing-the-development-version-of-turbogears-2-from-source">Follow these instructions</a> For installing your copy</li>
        <li><a href="http://trac.turbogears.org/browser/trunk">TG2 Trac's svn view</a> In case you need a quick look</li>
        <li><a href="http://groups.google.com/group/turbogears-trunk"> Join the TG-Trunk Mail List</a> for TG2 discuss/dev </li>
      </ul>
  </div>
</%def>

<%def name="header()">
  <div id="header">
  	<h1>
  		Welcome OSTacct
		<span class="subtitle">The Inschool Accounting Application</span>
	</h1>
  </div>
</%def>
<%def name="footer()">
 
  <div class="foottext">
    <p>School finance folks are super heros</p>
  </div>
  <div class="clearingdiv"></div>
</div>
</%def>




    % if tg.auth_stack_enabled:
      <span>
          % if not request.identity:
            <li id="login" class="loginlogout"><a href="${tg.url('/login')}">Login</a></li>
          % else:
            <li id="login" class="loginlogout"><a href="${tg.url('/logout_handler')}">Logout</a></li>
            <li id="admin" class="loginlogout"><a href="${tg.url('/admin')}">Admin</a></li>
          % endif
      </span>
    % endif



</html>
