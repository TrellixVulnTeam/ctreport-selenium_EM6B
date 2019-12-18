from ctreport_html.properties import status, priority,severity
from utility_classes import Status, Severity

def screenshot_section(test):
    c=''''''
    for log in test._logs:
        if log["type"] == "screenshot":
            c += '''
                <a href="#{}" target="_blank"> 
                    <i class="fas fa-image pl-2" style="font-size:30px; color:#aaa;"></i></i>
                </a>
            '''.format(log["screenshot"])
        elif log["type"] == "error":
            if log["screenshot"] is not None:
                c += '''
                    <a href="#{}" target="_blank"> 
                        <i id="#{}" class="fas fa-image pl-2" style="font-size:30px; color:#cb3434;"></i>
                    </a>
                '''.format(log["screenshot"],log["screenshot"].split('\\')[-1])
        elif log["type"] == "verify" or log["type"] == "assert":
            if log["screenshot"] is not None:
                c += '''
                     <a href="#{}" target="_blank"> 
                         <i id="#{}" class="fas fa-image pl-2" style="font-size:30px; color:#cb3434;"></i>
                     </a>
                 '''.format(log["screenshot"], log["id"])
    return c

def table_content(logs):
    c=''''''
    for log in logs:
        if log["type"] == "log":
            c +='''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">Log</td>
                    <td style="width: 70%;">{}</td>
                    <td style="width: 10%;"><span  class="extrasmall">{}</span></td>
                </tr>                
                '''.format(status[Status.PASS][0],status[Status.PASS][1],log["message"],log["start-time"])
        elif log["type"] == "error":
            type_= '''
            <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="">Error</a>
            '''
            screenshot_path=log["screenshot"]
            if screenshot_path is None:
                type_="Error"
            else:
                type_.format(screenshot_path.split('\\')[-1],screenshot_path.split('\\')[-1])
            c += '''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">
                    {}
                    </td>
                    <td style="width: 70%;">{} 
                        <br>
                        <span class="extrasmall">{}</span> 
                    </td>
                    <td style="width: 10%;"><span  class="extrasmall">{}</span></td>
                </tr>                
            '''.format(status[Status.FAIL][0],status[Status.FAIL][1], type_, log["message"], log["error"], log["start-time"])
        elif log["type"] == "broken":
            c +='''
                <tr class="border-bottom">
                    <td class="text-sm-center" style="width: 10%;"><i class="{}" style="{}"></i></td>
                    <td style="width: 10%;">Broken</td>
                    <td style="width: 70%; color:#F7464A;">{}</td>
                    <td style="width: 10%; "><span  class="extrasmall">{}</span></td>
                </tr>                
                '''.format(status[Status.BROKEN][0],status[Status.BROKEN][1],log["error"][:500],log["start-time"])
        elif log["type"] == "verify":
            type_ = '''
                        <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="">{}</a>
                    '''
            screenshot_path = log["screenshot"]
            if screenshot_path is None:
                type_ = "Verification"
            else:
                type_.format(log["id"], screenshot_path.split('\\')[-1],"Verification")
            if log["data-type"] is not "others":
                e_a_content='''
                    <td style="width: 70%">
                        <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                        Expected: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        Actual: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        <br/>
                    </td>
                '''.format(severity[log["severity"]][0], severity[log["severity"]][1],log["id"],log["id"])
            else:
               e_a_content = '''
                           <td style="width: 70%">
                               <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                               Expected: {}    Actual: {}
                               <br>
                           </td>
                       '''.format(severity[log["severity"]][0], severity[log["severity"]][1], log["expected"],
                                  log["actual"])
            c += '''
                    <tr class="border-bottom">
                        <td class="text-sm-center" style="width: 10%"><i class="{}" style="{}"></i></td>
                        <td style="width: 10%">{}</td>
                        {}
                        <td style="width: 10%"><span class="extrasmall">{}</span></td>
                    </tr>             
                   '''.format(status[log["status"]][0], status[log["status"]][1], type_, e_a_content, log["start-time"])
        elif log["type"] == "assert":
            type_ = '''
                        <a href="#{}" data-toggle="popover" data-trigger="hover" data-content="{}" data-original-title="" title="">{}</a>
                    '''
            screenshot_path = log["screenshot"]
            if screenshot_path is None:
                type_ = "Assertion"
            else:
                type_.format(log["id"], screenshot_path.split('\\')[-1], "Assertion")
            if log["data-type"] is not "others":
                e_a_content = '''
                    <td style="width: 70%">
                        <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                        Expected: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        Actual: 
                        &nbsp;
                        <i class="fas fa-ellipsis-h pointer" onclick="createmodal('{}')"></i>
                        &nbsp;
                        <br/>
                    </td>
                '''.format(severity[Severity.BLOCKER][0], severity[Severity.BLOCKER][1], log["id"], log["id"])
            else:
               e_a_content = '''
                           <td style="width: 70%">
                               <i class="{} pointer" onclick="expandFooter('info')" style="{}"></i>
                               Expected: {}    Actual: {}
                               <br>
                           </td>
                       '''.format(severity[Severity.BLOCKER][0], severity[Severity.BLOCKER][1], log["expected"],log["actual"])
            c += '''
                    <tr class="border-bottom">
                        <td class="text-sm-center" style="width: 10%"><i class="{}" style="{}"></i></td>
                        <td style="width: 10%">{}</td>
                        {}
                        <td style="width: 10%"><span class="extrasmall">{}</span></td>
                    </tr>             
                   '''.format(status[log["status"]][0], status[log["status"]][1], type_, e_a_content, log["start-time"])
    return c

def section(tests):
    index=0
    c=''''''
    for test in tests:
        section_head='''
        <li class="list-group-item font-weight-bold" style="background-color:rgb(0,0,0,0.1); display: flex; justify-content: space-between;">
            <span>{} {}</span>
            <i id="expand" class="fas fa-caret-square-down pointer" style=" font-size:x-large;" data-toggle="collapse" data-target="#moredetails{}" onclick='expandFunction("{}")'></i>
        </li>
        '''.format(test._id,test._name,index,test._id)

        more_details='''
        <li id="moredetails{}" class="list-group-item small panel-collapse collapse">
            <div class="row">
                <div class="col-5">
                    <div class="row">
                        <div class="col-3">Status</div>
                        <div class="col-9">
                        <i class="{}" style="{} font-size: 13px;"></i>
                        {}</div>
                    </div>
                    <div class="row">
                        <div class="col-3">Priority</div>
                        <div class="col-9">
                        <i class="{}" style="{} font-size: 13px;"></i>
                        {}</div>
                    </div>
                </div>
                <div class="col-7">
                <div class="row">
                        <div class="col-3">Start-time</div>
                        <div class="col-9">{}</div>
                    </div>
                    <div class="row">
                        <div class="col-3">End-time</div>
                        <div class="col-9">{}</div>
                    </div>
                    <div class="row">
                        <div class="col-3">Duration</div>
                        <div class="col-9">{}(H:MM:SS)</div>
                    </div>
                </div>
            </div>
            <div>
            <span>Description</span>
            <p>{}</p>
            </div>
        </li>
        '''.format(index,status[test._result][0],status[test._result][1],test._result.capitalize(),priority[test._priority][0],
                   priority[test._priority][1],test._priority.capitalize(),test._start_time,test._end_time,test._duration,test._description)

        test_steps = '''
        <li class="list-group-item">
            <table class="table medium table-borderless table-hover">
                <thead class="small border-bottom">
                    <tr>
                        <th class="text-sm-center" >STATUS</th>
                        <th>TYPE</th>
                        <th>DETAILS</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody class="small">
                    '''+table_content(test._logs)+'''
                </tbody>
            </table>
            '''+screenshot_section(test)+'''
        </li>
        '''.format()

        c += '''
        <div id="'''+test._id+'''" class="filterDiv1 '''+test._result+'''" style="padding-bottom: 20px;"> 
            <ul class="list-group">
                '''+section_head+'''
                '''+more_details+'''
                '''+test_steps+'''
            </ul>
        </div>         
        '''
        index+=1
    return c
def content(tests):
    c = '''
        <div class="col-sm-12 col-lg-7">
            <div id="search2">
                '''+section(tests)+'''
            </div>
        </div>
    '''
    return c