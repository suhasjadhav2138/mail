from django.shortcuts import render
from django.shortcuts import render, RequestContext, render_to_response, get_object_or_404
from  django.db import backends
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.contrib.auth.models import User
from .models import *
from form import *
# from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
import os, hashlib, random, platform
from django.utils import timezone
import email, getpass, imaplib
import json as json
import time, datetime
import string
import json
# from termcolor import colored
# import re



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
state_dict = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District of Columbia",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
}


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'


def date_check(x):
    if x == 'Jan':
        mon = 1

    elif x == 'Feb':
        mon = 2

    elif x == 'Mar':
        mon = 3

    elif x == 'Apr':
        mon = 4

    elif x == 'May':
        mon = 5

    elif x == 'Jun':
        mon = 6

    elif x == 'Jul':
        mon = 7

    elif x == 'Aug':
        mon = 8

    elif x == 'Sep':
        mon = 9

    elif x == 'Oct':
        mon = 10

    elif x == 'Nov':
        mon = 11

    else:
        mon = 12

    return mon


def get_first_text_block(email_message_instance):
    NI = ['jobs-noreply@cybercoders.com', 'applyonline@dice.com', \
          'invitations@linkedin.com', 'linkedin@e.linkedin.com', 'linkedin@e.linkedin.com']
    print "[" + email_message_instance["From"] + "] :" + email_message_instance["Subject"]
    if email_message_instance["From"] in NI or 'linkedin' in email_message_instance["From"]:
        return "cool"
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                print "ICE COOOOOOL"
                return part.get_payload()

    elif maintype == 'text':
        # print "COOOOOOL"

        return "Not so COOL"


        # def mainfunc(statename, u, p):
        #     detach_dir = '.'  # directory where to save attachments (default: current)
        #     # user = raw_input("Enter your GMail username:")
        #     # pwd = getpass.getpass("Enter your password: ")
        #     cool = []
        #     count_list = []
        #     c2 = []
        #
        #     field = statename
        #     if field.isdigit():
        #         print "\n Please enter valid state name....\nABORTING !!"
        #         exit()
        #     user = u  # "kunjan.dhoble@consultadd.in"  'kun2233dh@gmail.com'
        #     pwd = p  # "changeiscool"     "kdrocks@31"
        #     # anshi241215@gmail.com    ,   anscon2015
        #
        #
        #     # SWAPNIL
        #     # "sung52me@gmail.com",   "h0907joy@gmail.com"       , "joyguru291@gmail.com",
        #     # "ha904ra@gmail.com"   ,        "um09bh@gmail.com"
        #
        #     # pwd= consultadd505
        #     # SWAPNIL
        #
        #     # SUJO
        #
        #     # 2809sjt@gmail.com  ...           pwd=sushant@2814
        #     # 9692sjp@gmail.com
        #     # 2809sjp@gmail.com
        #     # 2196rt@gmail.com
        #
        #     # SUJO
        #
        #
        #     date_list = []
        #     kd = []
        #     d1 = {}
        #     d = {}
        #
        #     count = 0
        #     a = []
        #     list_of_em = []
        #     t = 0
        #
        #
        #     # Today's date:
        #     today, today1 = "", ""
        #     today += time.strftime("%d") + " " + time.strftime("%b")
        #     print "TODAY: ", today
        #     yy = int(time.strftime("%Y"))
        #     mm = int(time.strftime("%m"))
        #     dd = int(time.strftime("%d"))
        #     print "Check date:", dd, mm, yy
        #
        #     print user
        #
        #     for indx in range(len(user)):
        #         # print colored('USERNAME :', 'red', 'on_grey', attrs="bold")
        #
        #         print color.BOLD + color.OKBLUE + "USERNAME :" + color.END + "\v " + \
        #               color.HEADER + color.RED + color.UNDERLINE + (user[indx]) + color.END
        #
        #
        #         # connecting to the gmail imap server
        #
        #         m = imaplib.IMAP4_SSL("imap.gmail.com")
        #
        #         m.login(user[indx], pwd[indx])
        #
        #
        #         # m.select("[Gmail]/All Mail") #SELECTS ALL THE MAILBOXES
        #         # here you a can choose a mail box like INBOX instead
        #         # use m.list() to get "LIST all the mailboxes" -"INBOX",, "[Gmail]",,"[Gmail]/All Mail"
        #         m.select("INBOX")  # (SELECTS ONLY INBOX)
        #
        #         # print m.list()
        #         # resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
        #
        #         result, items = m.uid('search', None, "ALL")  # search and return uids instead
        #         # print "before",items
        #         items = items[0].split()  # getting the mails id
        #         items = items[::-1]  # Reverse List to get latest EM first
        #
        #         print items
        #         count_list.append(len(items))
        #
        #         # number_emails= len()
        #
        #         date_list = []
        #         kd = []
        #         d1 = {}
        #         d = {}
        #
        #         count = 0
        #         a = []
        #         list_of_em = []
        #         t = 0
        #
        #         None_list = []
        #         mail_id = []
        #         sender = []
        #         sub = []
        #         msg = []
        #         date = []
        #         lnth = len(items)
        #         nxt = []
        #         final = ""
        #         for idx, emailid in enumerate(items):
        #             # result, data = m.fetch(emailid, '(RFC822)')
        #
        #             result, data = m.uid("fetch", emailid,
        #                                  '(RFC822)')  # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        #             email_body = data[0][1]  # getting the mail content
        #             mail = email.message_from_string(email_body)  # parsing the mail content to get a mail object
        #             count = 0
        #             # CHECK DATE
        #             dt = ""
        #             dt = mail["Date"].split(', ', 1)
        #             print mail['Date'], "kd :  ", dt
        #
        #             # print "OSM"
        #             if len(dt) == 1:
        #                 dt = dt[0].split(' 2016')
        #             else:
        #                 dt = dt[1].split(' 2016')
        #             dt = dt[0]
        #             x = dt.split()
        #             # yr=""
        #             mon = date_check(x[1])
        #
        #             day = int(x[0])
        #             yr = 2016
        #             print "mail date", day, mon, yr
        #
        #             date_1 = datetime.datetime(yr, mon, day)
        #             date_2 = datetime.datetime(yy, mm, dd)
        #             diff = (date_2 - date_1).days
        #             print "GAP: ", diff
        #
        #             if diff > 5:
        #                 break
        #
        #             if mail.is_multipart():
        #                 for payload in mail.get_payload():
        #                     if count != 0:
        #                         break
        #                     # if payload.is_multipart(): ...
        #                     count += 1
        #                     # print "RIDDICKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
        #                     final = payload.get_payload()
        #             else:
        #                 print "POSITIVE", emailid
        #                 nxt.append(mail.get_payload())
        #
        #             salutation = ["Greetings", "Hello", "Hi", "Dear"]
        #             for j in salutation:
        #
        #                 if j in final:
        #                     txt = final.split(j)
        #                     final = txt[1]
        #                     # print "salutation",j
        #                     break
        #
        #             signoff = ["Regards", "regards", "Thank", "thank", "Thanks", "thanks", "Best", "best", "Truly", "truly",
        #                        "Sincerely", "sincerely", "Yours", "yours"]
        #
        #             for off in signoff:
        #                 if off in final:
        #                     txt = final.split(off)
        #                     msg.append(txt[0])
        #                     t += 1
        #                     break
        #                 else:
        #                     msg.append(final)
        #
        #             if len(msg) == 0:
        #                 print "Continue", emailid, mail['From'], " \t  ", mail['Date']
        #
        #                 continue
        #             sender.append(mail["From"])
        #             sub.append(mail["Subject"])
        #             em_content = {}
        #
        #             """
        #             NI=['jobs-noreply@cybercoders.com','applyonline@dice.com',\
        #                   'invitations@linkedin.com','linkedin@e.linkedin.com','no-reply@accounts.google.com',\
        #                     'linkedin@e.linkedin.com','diceadvisor@e-mail.dice.com']
        #
        #             "mail@koovs.co.in","no-reply@accounts.google.com","messaging-digest-noreply@linkedin.com",\
        #             "invitations@angel.co","replies@e.join.me"
        #
        #             if (mail["From"].split()[-1][1:-1]) not in NI:
        #             """
        #             # http://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
        #             # http://stackoverflow.com/questions/3633140/nested-for-loops-using-list-comprehension
        #             # http://stackoverflow.com/questions/18551458/how-to-frame-two-for-loops-in-list-comprehension-python
        #             #
        #             if "jobs@techfetch.com" not in mail["From"] and "@cybercoders.com" not in mail[
        #                 "From"] and "mail@koovs.co.in" not in mail["From"] and "LinkedIn" not in mail["From"] \
        #                     and "diceadvisor@e-mail.dice.com" not in mail["From"] and "no-reply@accounts.google.com" not in \
        #                     mail["From"]:
        #                 em_content['From'] = mail["From"]
        #                 em_content['Subject'] = mail["Subject"]
        #                 if len(msg[0]) != 2:
        #                     em_content['Body'] = msg[0]
        #                 else:
        #                     st = 0
        #                     for i in msg[0]:
        #                         if st == 0:
        #                             # print i,"iiiiiiiiiiiiiiiiiiiii"
        #                             st += 1
        #                             em_content['Body'] = str(i)
        #                             # print "em_content",em_content
        #                             # print "ZEROhgjghjg",len(msg[0])
        #                         else:
        #                             print "test fail"
        #                 msg = []
        #                 if idx == 0:
        #                     a.append(dt)
        #                     list_of_em.append(em_content)
        #
        #                     d[dt] = em_content
        #                     print "in"
        #                 elif idx == len(items) - 1:
        #                     print "elif"
        #                     list_of_em.append(em_content)
        #                     d[a[0]] = list_of_em
        #                     if dt not in a:
        #                         d[dt] = em_content
        #                     a, list_of_em = [], []
        #
        #
        #                 else:
        #                     print "else"
        #                     if dt not in a:
        #                         print "else in", list_of_em
        #                         if len(list_of_em) == 0:
        #                             a.append(dt)
        #                             list_of_em.append(em_content)
        #                             d[a[0]] = list_of_em
        #
        #
        #                         else:
        #                             d[a[0]] = list_of_em
        #                             a = []
        #                             a.append(dt)
        #                             list_of_em = []
        #                             list_of_em.append(em_content)
        #                             # print "ELSE .........ajskAJH  IF"
        #                     else:
        #                         # print "ELSE////////////ELSE"
        #                         list_of_em.append(em_content)
        #
        #         # date.append(mail["Date"])
        #         # l1=['date1','date1','date1','date2','date2']#LIST OF DATES
        #         # lnth=len(kd)
        #         # for idx, val in enumerate(kd):
        #
        #         # print list_of_em
        #         a, list_of_em, msg = [], [], []
        #         if len(d.values()) == 0 or len(d) == 0:
        #             d1[user[indx]] = ''
        #         else:
        #             d1[user[indx]] = dict(d)
        #
        #         with open(os.path.join(BASE_DIR + '/json', str(user[indx]) + '.json'), 'wb') as out:
        #             json.dump(str(d1), out, indent=2, separators=(",", ":"), sort_keys=True, ensure_ascii=True)
        #
        #             # json_data=open('/home/consultadd6/Desktop/'+str(user[l])+'.json').read()
        #             # kd = json.loads(json_data)
        #
        #
        #
        #             #
        #             # for i in range(len(msg)):
        #             #     if field in msg[i]:
        #             #         a = ""
        #             #
        #             #         a += "SENDER :\t" + str(sender[i]) + "\t"
        #             #         a += "SUBJECT:\t" + sub[i]
        #             #         # print "SENDER: ",sender[i]
        #             #         # print "SUBJECT: ",sub[i]
        #             #         # print "GOTCHA!!!!!!\n \n",msg[i]
        #             #         c1.append(a)
        #             #         c2.append(msg[i])
        #             #
        #             # cool.append(c1)
        #             # cool.append(c2)
        #             # print "Length1", len(c1)
        #             # print "Length2", len(c2)
        #             # print "LIST OF IDS CONTAINING KEYWORD\n",c1
        #     return count_list

        #
        # def retrieve_em(statename, gm_id):
        #     # state=statename
        #     acro_state_u = str(statename).upper()
        #     state_t = state_dict[str(statename)]
        #
        #     state_u = state_dict[str(statename).upper()]
        #     final_dict = {}
        #     user_email = []
        #     sender_list, sub_list, em_body_list, em_date, cool, user_email = [], [], [], [], [], []
        #     for name in gm_id:
        #         list_data = []
        #         user_email.append(str(name))
        #         json_data = open(os.path.join(BASE_DIR + '/json', str(name) + '.json')).read()
        #         kd = json.loads(json_data)
        #         # print kd['anshi241215@gmail.com']['27 Oct'][1]['From']  #This is OSM ABOUT PYTHON :D:D:D
        #         kd = eval(kd)
        #
        #         for it, val in kd.iteritems():
        #             if val != '':
        #                 for it1, val1 in val.iteritems():  # it1 gives date of mail
        #                     for i in val1:
        #                         a = re.compile(r'\b%s\b' % (state_u))
        #                         b = re.compile(r'\b%s\b' % (state_t))
        #                         c = re.compile(r'\b%s\b' % (acro_state_u))
        #                         # print i['Body'],"BBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n"
        #
        #                         if a.search(i['Body']) or b.search(i['Body']) or c.search(i['Body']) \
        #                                 or a.search(i['Subject']) or b.search(i['Subject']) or c.search(i['Subject']):
        #                             list_data.append([str(i['From']), str(i['Subject']), str(i['Body'])])
        #
        #                             # sender,sub,em_body="","",""
        #                             # sender+=str(i['From'])
        #                             # sub+=str(i['Subject'])
        #                             # em_body+=str(i['Body'])
        #                             # sender_list.append(sender)
        #                             # sub_list.append(sub)
        #                             # em_body_list.append(em_body)
        #                             # em_date.append(it1)
        #                             # else:
        #                             #     sender_list.append('')
        #                             #     sub_list.append('')
        #                             #     em_body_list.append('')
        #                             #     em_date.append('')
        #
        #         final_dict[name] = list_data
        #
        #
        #     #
        #     # print kd['anshi241215@gmail.com']['27 Oct'][1]['From']  #This is OSM ABOUT PYTHON :D:D:D
        #
        #
        #     #
        #     # cool.append(sender_list)
        #     # cool.append(sub_list)
        #     # cool.append(em_body_list)
        #     # cool.append(user_email)
        #     # cool.append(em_date)
        #     # print kd['anshi241215@gmail.com']
        #     print final_dict
        #     return final_dict, user_email


        # @login_required
        # def filter_res_view(request):
        #
        #     if request.GET:
        #         print "GETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
        #
        #         # URL hit to avoid loss of data on refresh
        #     if request.POST:
        #         print "POSTTTTTTTTTTTTTTTT"
        #     form1 = request.POST
        #     print form1,"oooooooooooooooooooooooooooooooooooooo"
        #     userid = request.user.id
        #     print userid
        #
        #     a = edit_profile.objects.get(user_id=userid)
        #
        #     u_name = User.objects.get(id=userid)
        #     b = a.id_field
        #     c = a.pass_field
        #     ids = b.split(',')
        #     pwd = c.split(',')
        #     print ids
        #     print pwd
        #     e_ids =ids
        #     if form1 is not None and len(form1) == 3 and form1.has_key('state'):
        #         print "FORM INPUTS : \n", form1
        #         res = str(form1['state'])
        #         # create json files
        #
        #         k = mainfunc(res, ids, pwd)
        #         res, user_mails = retrieve_em(res, ids)
        #
        #         # sndr= res[0]
        #         # hdr = res[1]
        #         # msg = res[2]
        #         # print sndr
        #         # print hdr
        #
        #         username = u_name.username
        #         u_email = u_name.email
        #         ln = len(res)
        #
        #     else:
        #         # print "FORM INPUTS : \n",form1
        #         # form1['state']='New Jersey'
        #         # res=str(form1['state'])
        #         # res=mainfunc(res)
        #         # hdr=res[0]
        #         # msg=res[1]
        #
        #         # ln=len(msg)
        #         res, user_mails = retrieve_em("IL", ids)
        #
        #         username = u_name.username
        #         u_email = u_name.email
        #         ln=len(res)
        #         # print "USERNAME: ",form1['username']
        #         # print "STATE : ",form1['state']
        #     # return render_to_response('kdmail/filter_res.html',
        #     #                               {'form': form1,'res_sender':sndr, 'res_header': hdr, 'res_msg': msg, 'res_user_mail':user_mails,'username':username,'email':u_email,'size': ln},
        #     #                               context_instance=RequestContext(request))
        #     return render_to_response('kdmail/filter_res.html',
        #                               {'form': form1, 'res_msg': res, 'res_user_mail': user_mails,"email_id":ids,  'username': username,
        #                                'email': u_email, 'size': ln},
        #                               context_instance=RequestContext(request))

        # else:
        #     return HttpResponseRedirect('/getmail/results/')


# @login_required
# def global_filter_res_view(request):
#     if request.GET:
#         print "GETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
#
#         # URL hit to avoid loss of data on refresh
#     if request.POST:
#         print "POSTTTTTTTTTTTTTTTT"
#     form1 = request.POST
#     print form1
#     userid = request.user.id
#     print userid
#
#     a = edit_profile.objects.get(user_id=userid)
#
#     b = a.id_field
#     c = a.pass_field
#     ids = b.split(',')
#     pwd = c.split(',')
#     print ids
#     print pwd
#     if form1 is not None and len(form1) == 3 and form1.has_key('state'):
#         print "FORM INPUTS : \n", form1
#         res = str(form1['state'])
#         # k=mainfunc(res,ids,pwd)
#         res = retrieve_em(res, ids)
#         sndr = res[0]
#         hdr = res[1]
#         msg = res[2]
#         dt = res[3]
#         print "\v\nSENDER:", sndr
#
#         ln = len(msg)
#     else:
#         # print "FORM INPUTS : \n",form1
#         # form1['state']='New Jersey'
#         # res=str(form1['state'])
#         # res=mainfunc(res)
#         # hdr=res[0]
#         # msg=res[1]
#
#         # ln=len(msg)
#         sndr, hdr, msg, dt, ln = 0, 0, 0, 0, 0
#
#         # print "USERNAME: ",form1['username']
#         # print "STATE : ",form1['state']
#     return render_to_response('kdmail/global_filter_res.html',
#                               {'form': form1, 'res_date': dt, 'res_sender': sndr, 'res_header': hdr, 'res_msg': msg,
#                                'size': ln},
#                               context_instance=RequestContext(request))


def welcome(request):
    if request.POST:
        print "cool"
        form2 = request.POST
        print form2
        return HttpResponseRedirect('/getmail/results/')

    stats_data = user_stats.objects.all()
    # stats_data = json.dumps(stats_data)
    # print stats_data

    # get all dates when requirements was not none
    dates = []
    requirement_emails = []
    for i in stats_data:
        if i.date_added not in dates:
            # print i.technology
            dates.append(i.date_added)
        if i.requested_email not in requirement_emails:
            requirement_emails.append(i.requested_email)

    print dates
    print requirement_emails
    tech_stats = {}
    list_technologies = []
    temp_dict = {}

    for i in dates:

        for data in stats_data:
            if i == data.date_added:
                if data.technology in temp_dict:
                    temp_dict[str(data.technology)] = temp_dict[data.technology] + data.requirements_count
                    if temp_dict not in list_technologies:
                        list_technologies.append(temp_dict)
                else:

                    temp_dict[str(data.technology)] = data.requirements_count
                    if temp_dict not in list_technologies:
                        list_technologies.append(temp_dict)



            (tech_stats[i]) = list_technologies

    print tech_stats
    a = {}
    b = []
    a['value'] = 1000
    a['color'] = "#46BFBD"
    a['highlight'] = "#5AD3D1"
    a['label'] = "Kitchen"

    b.append(a)
    a = {}
    a['value'] = 2000
    a['color'] = "#46BFBD"
    a['highlight'] = "#5AD3D1"
    a['label'] = "Mobile"

    b.append(a)
    a = {}
    a['value'] = 6000
    a['color'] = "#46BFBD"
    a['highlight'] = "#5AD3D1"
    a['label'] = "Home"

    b.append(a)
    b_json = json.dumps(str(b))
    b_json = json.loads(b_json)
    b_json = eval(b_json)

    print type(b_json)

    #     {
    #         value: 1000,
    #         color: "#FDB45C",
    #         highlight: "#FFC870",
    #         label: "Home"
    #     },
    # {
    #         value: 1000,
    #         color: "#FDB45C",
    #         highlight: "#FFC870",
    #         label: "Home"
    #     }

    return render_to_response('kdmail/welcome.html', {'b_json': b_json},
                              context_instance=RequestContext(request))


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_view(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = MyForm(request.POST)
        args['form'] = form
        if form.is_valid():
            userid = request.user.id
            print userid, "oooooooooooooooo"
            user = User.objects.get(id=userid)
            user.is_active = True
            print form, "oooooooooooooooooooooooooooo"
            form.save()  # save user to database if form is valid

            return HttpResponseRedirect('/getmail/confirm/')
    else:
        args['form'] = MyForm()

    return render_to_response('kdmail/register.html', args, context_instance=RequestContext(request))


def auth_view(request):
    # args = {}
    # args.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    print "COOL", username, password
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)

        # d=1
        # -----------------------------------my test-----------------------------------------

        userid = request.user.id
        print "USERID : ", userid
        my_test = edit_profile.objects.get(user_id=userid)
        my_data = my_test.consultant_name
        print my_data, "mydata"
        if my_data == "Enter Candidates Name":

            return HttpResponseRedirect('/getmail/add_ids/')


        else:

            return HttpResponseRedirect('/getmail/')



            # --------------------------------------end test----------------------------------------------
            # return HttpResponseRedirect('/fmar/locate/')

    else:
        return HttpResponseRedirect('/getmail/invalid/')


def register_confirm(request):
    # check if user is already logged in and if he is redirect him to some other url, e.g. home
    # if request.user.is_authenticated():
    #     HttpResponseRedirect('')
    #
    # # check if there is UserProfile which matches the activation key (if not then display 404)
    # user_profile = get_object_or_404(EmailUser)
    #

    # if the key hasn't expired save user and set him as active and render some template to confirm activation
    # # user = user_profile.user
    # user.is_active = True
    # user.save()
    # username=request.POST.get('username','')
    # print"user",username
    # password=request.POST.get('password','')
    # user=auth.authenticate(username=username,password=password)
    #
    # if user is not None and user.is_active:
    #     auth.login(request,user)
    # auth_view(request);
    return render_to_response('kdmail/register_confirm.html')
    # username=request.POST.get('username','')
    # password=request.POST.get('password','')
    # user=auth.authenticate(username=username,password=password)
    #
    # if user is not None and user.is_active:
    #     auth.login(request,user)
    #     return render_to_response('shwekd/profile.html')


def login_view(request):
    c = {}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/getmail/already_loggedin/')
    else:
        c.update(csrf(request))
        return render_to_response('kdmail/login.html', c)


def invalid_view(request):
    return render_to_response('kdmail/invalid.html')


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/getmail/login/')


@login_required
def unable_login_view(request):
    return render_to_response('kdmail/unable_login.html')


@login_required
def add_ids_view(request):
    try:
        instance = edit_profile.objects.get(user=request.user)
    except edit_profile.DoesNotExist:
        instance = None

    if request.method == 'POST':
        print("oooooooooooooooooooooooooooooooooooooooooooooo")
        form = edit_profile_form(request.POST or None, request.FILES, instance=instance)
        print(form, "akhahkgd")
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            # if form1 is not None and len(form1) == 3 and form1.has_key('state'):
            #     print "FORM INPUTS : \n", form1
            #     res = str(form1['state'])
            #     res = mainfunc(res)
            #     hdr = res[0]
            #     msg = res[1]
            #
            #     ln = len(msg)
            # else:
            #     # print "FORM INPUTS : \n",form1
            #     # form1['state']='New Jersey'
            #     # res=str(form1['state'])
            #     # res=mainfunc(res)
            #     # hdr=res[0]
            #     # msg=res[1]
            #
            #     # ln=len(msg)
            #     hdr, msg, ln = 0, 0, 0
            #
            # # print "USERNAME: ",form1['username']
            # # print "STATE : ",form1['state']
            # return render_to_response('kdmail/filter_res.html',
            #                       {'form': form, 'res_header': hdr, 'res_msg': msg, 'size': ln},
            #                       context_instance=RequestContext(request))


            # message.succes('SAVED')
            # print form.pass_field

            return HttpResponseRedirect('/getmail/add_ids/')

        else:
            print form.errors
    else:

        form = edit_profile_form(instance=instance)

    return render(request, 'kdmail/add_ids.html', {'form': form}, context_instance=RequestContext(request))
