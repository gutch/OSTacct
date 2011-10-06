# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1317658015.372879
_template_filename='/home/gutch/ost/ostacct/ostacct/templates/eventcal.mak'
_template_uri='/home/gutch/ost/ostacct/ostacct/templates/eventcal.mak'
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
        weeklist = context.get('weeklist', UNDEFINED)
        current_month = context.get('current_month', UNDEFINED)
        events = context.get('events', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        current_day = context.get('current_day', UNDEFINED)
        current_yr = context.get('current_yr', UNDEFINED)
        current_no = context.get('current_no', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\t  \n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<link rel="stylesheet" type="text/css" media="screen" href="')
        # SOURCE LINE 8
        __M_writer(escape(tg.url('/css/calstyles.css')))
        __M_writer(u'" />  \t  \n<HTML>\n\n<script type="text/javascript">\nfunction update(){\nvar ThePath=\'/eventlist\';\nwindow.location =ThePath}\nfunction winprint(){\nwindow.print()\n}\n\nfunction next(m,y){\nif (m==12){\n   m=0;\n   y=y+1;}\nvar ThePath=\'/cal?month=\'+(m+1)+"&year="+ y;\nwindow.location =ThePath}\n\nfunction prior(m,y){\nif (m==1){\n     m=13;\n     y=y-1;}\nvar ThePath=\'/cal?month=\'+(m-1)+"&year="+ y;\nwindow.location =ThePath}\n\nfunction back(){\nvar ThePath=\'/index\';\nwindow.location=ThePath\n}\t \n\n</script>\n<head>\n\n\n<title>February 2007</title>\n\n</head>\n\n<body>\n<div id="container">\n<b class="rtop"><b class="r1"></b> <b class="r2"></b><b class="r3"></b> <b class="r4"></b></b>\n<table border="0">\n<tr>\n\n<td><FORM METHOD = "LINK" ACTION="index"><INPUT TYPE="SUBMIT" VALUE="Back to Index"></FORM></td>\n<td><INPUT TYPE="button" VALUE="PRIOR<<--MONTH" HEIGHT="30" WIDTH="150" BORDER="0" ONCLICK="prior(')
        # SOURCE LINE 53
        __M_writer(escape(current_no))
        __M_writer(u',')
        __M_writer(escape(current_yr))
        __M_writer(u')"</td>\n<td><INPUT TYPE="button" VALUE="NEXT-->>MONTH" HEIGHT="30" WIDTH="150" BORDER="0" ONCLICK="next(')
        # SOURCE LINE 54
        __M_writer(escape(current_no))
        __M_writer(u',')
        __M_writer(escape(current_yr))
        __M_writer(u')"</td>\n<td><FORM METHOD = "LINK" ACTION= "eventlist"><INPUT TYPE="SUBMIT" VALUE="EDIT CALENDAR EVENTS" ></FORM></td>\n\n</tr></table><br>\n <h1>')
        # SOURCE LINE 58
        __M_writer(escape(current_month))
        __M_writer(u', ')
        __M_writer(escape(current_yr))
        __M_writer(u'</h1 >\n<table id="month">\n\t<thead>\n\t\t<tr>\n\t\t\t<center><th class="weekend"><center>Sunday</center></th>\n\t\t\t<th><center>Monday</center></th>\n\t\t\t<th><center>Tuesday</center></th>\n\t\t\t<th><center>Wednesday</center></th>\n\n\t\t\t<th><center>Thursday</center></th>\n\t\t\t<th><center>Friday</center></th>\n\t\t\t<th class="weekend"><center>Saturday</center></th>\n\t\t</tr>\n\t</thead>\n\t<tbody>\n\n')
        # SOURCE LINE 74
        for sun, mon, tue, wed, thu, fri, sat in weeklist:
            # SOURCE LINE 75
            __M_writer(u'\t\t  <tr>\n')
            # SOURCE LINE 76
            if sun ==0:
                # SOURCE LINE 77
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 79
            if sun>0 and sun <> current_day:
                # SOURCE LINE 80
                __M_writer(u'                          <td class=weekend></span>')
                __M_writer(escape(sun))
                __M_writer(u'<div class=weekend><br>\n')
                # SOURCE LINE 81
                if events:
                    # SOURCE LINE 82
                    for m, d, y,devent in events: 
                        # SOURCE LINE 83
                        if d==sun:                              
                            # SOURCE LINE 84
                            if devent:
                                # SOURCE LINE 85
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 86
                                    if doc:                             									 
                                        # SOURCE LINE 87
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 88
                                    else:
                                        # SOURCE LINE 89
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 96
                __M_writer(u'                         <div class=weekend></div></td>\n')
                pass
            # SOURCE LINE 98
            if sun==current_day:
                # SOURCE LINE 99
                __M_writer(u'                          <td class=weekend></span><strong>')
                __M_writer(escape(sun))
                __M_writer(u'</strong?<div class=weekend><br>\n')
                # SOURCE LINE 100
                if events:
                    # SOURCE LINE 101
                    for m, d, y,devent in events: 
                        # SOURCE LINE 102
                        if d==sun:                              
                            # SOURCE LINE 103
                            if devent:
                                # SOURCE LINE 104
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 105
                                    if doc:                             									 
                                        # SOURCE LINE 106
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 107
                                    else:
                                        # SOURCE LINE 108
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 115
                __M_writer(u'                         <div class=weekend></div></td>\n')
                pass
            # SOURCE LINE 117
            __M_writer(u'\t\t \n')
            # SOURCE LINE 118
            if mon ==0:
                # SOURCE LINE 119
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 121
            if mon>0 and mon <> current_day:
                # SOURCE LINE 122
                __M_writer(u'                          <td class=day></span>')
                __M_writer(escape(mon))
                __M_writer(u'<div class=day><br>\n')
                # SOURCE LINE 123
                if events:
                    # SOURCE LINE 124
                    for m, d, y,devent in events: 
                        # SOURCE LINE 125
                        if d==mon:                              
                            # SOURCE LINE 126
                            if devent:
                                # SOURCE LINE 127
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 128
                                    if doc:                             									 
                                        # SOURCE LINE 129
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 130
                                    else:
                                        # SOURCE LINE 131
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 138
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 140
            if mon==current_day:
                # SOURCE LINE 141
                __M_writer(u'                          <td class=current></span><strong>')
                __M_writer(escape(mon))
                __M_writer(u'</strong?<div class=day><br>\n')
                # SOURCE LINE 142
                if events:
                    # SOURCE LINE 143
                    for m, d, y,devent in events: 
                        # SOURCE LINE 144
                        if d==mon:                              
                            # SOURCE LINE 145
                            if devent:
                                # SOURCE LINE 146
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 147
                                    if doc:                             									 
                                        # SOURCE LINE 148
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 149
                                    else:
                                        # SOURCE LINE 150
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 157
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 159
            __M_writer(u'\t\t\t\n')
            # SOURCE LINE 160
            if tue ==0:
                # SOURCE LINE 161
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 163
            if tue>0 and tue <> current_day:
                # SOURCE LINE 164
                __M_writer(u'                          <td class=day></span>')
                __M_writer(escape(tue))
                __M_writer(u'<div class=day><br>\n')
                # SOURCE LINE 165
                if events:
                    # SOURCE LINE 166
                    for m, d, y,devent in events: 
                        # SOURCE LINE 167
                        if d==tue:                              
                            # SOURCE LINE 168
                            if devent:
                                # SOURCE LINE 169
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 170
                                    if doc:                             									 
                                        # SOURCE LINE 171
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 172
                                    else:
                                        # SOURCE LINE 173
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 180
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 182
            if tue==current_day:
                # SOURCE LINE 183
                __M_writer(u'                          <td class=current></span><strong>')
                __M_writer(escape(tue))
                __M_writer(u'</strong?<div class=day><br>\n')
                # SOURCE LINE 184
                if events:
                    # SOURCE LINE 185
                    for m, d, y,devent in events: 
                        # SOURCE LINE 186
                        if d==tue:                              
                            # SOURCE LINE 187
                            if devent:
                                # SOURCE LINE 188
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 189
                                    if doc:                             									 
                                        # SOURCE LINE 190
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 191
                                    else:
                                        # SOURCE LINE 192
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 199
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 201
            __M_writer(u'\t\t\n')
            # SOURCE LINE 202
            if wed ==0:
                # SOURCE LINE 203
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 205
            if wed>0 and wed <> current_day:
                # SOURCE LINE 206
                __M_writer(u'                          <td class=day></span>')
                __M_writer(escape(wed))
                __M_writer(u'<div class=day><br>\n')
                # SOURCE LINE 207
                if events:
                    # SOURCE LINE 208
                    for m, d, y,devent in events: 
                        # SOURCE LINE 209
                        if d==wed:                              
                            # SOURCE LINE 210
                            if devent:
                                # SOURCE LINE 211
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 212
                                    if doc:                             									 
                                        # SOURCE LINE 213
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 214
                                    else:
                                        # SOURCE LINE 215
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 222
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 224
            if wed==current_day:
                # SOURCE LINE 225
                __M_writer(u'                          <td class=current></span><strong>')
                __M_writer(escape(wed))
                __M_writer(u'</strong?<div class=day><br>\n')
                # SOURCE LINE 226
                if events:
                    # SOURCE LINE 227
                    for m, d, y,devent in events: 
                        # SOURCE LINE 228
                        if d==wed:                              
                            # SOURCE LINE 229
                            if devent:
                                # SOURCE LINE 230
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 231
                                    if doc:                             									 
                                        # SOURCE LINE 232
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 233
                                    else:
                                        # SOURCE LINE 234
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 241
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 243
            __M_writer(u'\n\n')
            # SOURCE LINE 245
            if thu ==0:
                # SOURCE LINE 246
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 248
            if thu>0 and thu <> current_day:
                # SOURCE LINE 249
                __M_writer(u'                          <td class=day></span>')
                __M_writer(escape(thu))
                __M_writer(u'<div class=day><br>\n')
                # SOURCE LINE 250
                if events:
                    # SOURCE LINE 251
                    for m, d, y,devent in events: 
                        # SOURCE LINE 252
                        if d==thu:                              
                            # SOURCE LINE 253
                            if devent:
                                # SOURCE LINE 254
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 255
                                    if doc:                             									 
                                        # SOURCE LINE 256
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 257
                                    else:
                                        # SOURCE LINE 258
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 265
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 267
            if thu==current_day:
                # SOURCE LINE 268
                __M_writer(u'                          <td class=current></span><strong>')
                __M_writer(escape(thu))
                __M_writer(u'</strong?<div class=day><br>\n')
                # SOURCE LINE 269
                if events:
                    # SOURCE LINE 270
                    for m, d, y,devent in events: 
                        # SOURCE LINE 271
                        if d==thu:                              
                            # SOURCE LINE 272
                            if devent:
                                # SOURCE LINE 273
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 274
                                    if doc:                             									 
                                        # SOURCE LINE 275
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 276
                                    else:
                                        # SOURCE LINE 277
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 284
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 286
            __M_writer(u'\n')
            # SOURCE LINE 287
            if fri ==0:
                # SOURCE LINE 288
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 290
            if fri>0 and fri <> current_day:
                # SOURCE LINE 291
                __M_writer(u'                          <td class=day></span>')
                __M_writer(escape(fri))
                __M_writer(u'<div class=day><br>\n')
                # SOURCE LINE 292
                if events:
                    # SOURCE LINE 293
                    for m, d, y,devent in events: 
                        # SOURCE LINE 294
                        if d==fri:                              
                            # SOURCE LINE 295
                            if devent:
                                # SOURCE LINE 296
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 297
                                    if doc:                             									 
                                        # SOURCE LINE 298
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 299
                                    else:
                                        # SOURCE LINE 300
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 307
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 309
            if fri==current_day:
                # SOURCE LINE 310
                __M_writer(u'                          <td class=current></span><strong>')
                __M_writer(escape(fri))
                __M_writer(u'</strong?<div class=day><br>\n')
                # SOURCE LINE 311
                if events:
                    # SOURCE LINE 312
                    for m, d, y,devent in events: 
                        # SOURCE LINE 313
                        if d==fri:                              
                            # SOURCE LINE 314
                            if devent:
                                # SOURCE LINE 315
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 316
                                    if doc:                             									 
                                        # SOURCE LINE 317
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 318
                                    else:
                                        # SOURCE LINE 319
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 326
                __M_writer(u'                         <div class=day></div></td>\n')
                pass
            # SOURCE LINE 328
            __M_writer(u'  \n\t\t\n')
            # SOURCE LINE 330
            if sat ==0:
                # SOURCE LINE 331
                __M_writer(u'\t\t\t      <td class=previous></span><div class=previous></div></td>\n')
                pass
            # SOURCE LINE 333
            if sat>0 and sat <> current_day:
                # SOURCE LINE 334
                __M_writer(u'                          <td class=weekend></span>')
                __M_writer(escape(sat))
                __M_writer(u'<div class=weekend><br>\n')
                # SOURCE LINE 335
                if events:
                    # SOURCE LINE 336
                    for m, d, y,devent in events: 
                        # SOURCE LINE 337
                        if d==sat:                              
                            # SOURCE LINE 338
                            if devent:
                                # SOURCE LINE 339
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 340
                                    if doc:                             									 
                                        # SOURCE LINE 341
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 342
                                    else:
                                        # SOURCE LINE 343
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 350
                __M_writer(u'                         <div class=weekend></div></td>\n')
                pass
            # SOURCE LINE 352
            if sat==current_day:
                # SOURCE LINE 353
                __M_writer(u'                          <td class=weekend></span><strong>')
                __M_writer(escape(sat))
                __M_writer(u'</strong?<div class=weekend><br>\n')
                # SOURCE LINE 354
                if events:
                    # SOURCE LINE 355
                    for m, d, y,devent in events: 
                        # SOURCE LINE 356
                        if d==sat:                              
                            # SOURCE LINE 357
                            if devent:
                                # SOURCE LINE 358
                                for typ,Desc,doc in devent:
                                    # SOURCE LINE 359
                                    if doc:                             									 
                                        # SOURCE LINE 360
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br><a href="/eventdoc/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'/')
                                        __M_writer(escape(doc))
                                        __M_writer(u'">')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'</a>                               \n')
                                        # SOURCE LINE 361
                                    else:
                                        # SOURCE LINE 362
                                        __M_writer(u'\t\t\t\t')
                                        __M_writer(escape(typ))
                                        __M_writer(u'<br> ')
                                        __M_writer(escape(Desc))
                                        __M_writer(u'\n')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    pass
                # SOURCE LINE 369
                __M_writer(u'                         <div class=weekend></div></td>\n')
                pass
            # SOURCE LINE 371
            __M_writer(u'  \t\t  </tr>\n')
            pass
        # SOURCE LINE 373
        __M_writer(u'\t\t  \n\n\t</tbody>\n</table>\n</div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n  Welcome DOE Local Finance Event and Due Date Calendar\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


