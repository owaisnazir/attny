import scraperwiki
import string
import urllib2
#scraperwiki.sqlite.execute("drop table bbb")
#scraperwiki.sqlite.execute("drop table missinglink")
#scraperwiki.sqlite.execute("create table bbb ('n1','add','ph','stat','email4','da','sou1')")
#scraperwiki.sqlite.execute("create table Missinglink (`Link`)")
mylist=[]
mylist.append(")


email6=""
beg=0
for index in range(len(mylist)):
        try:
            html = scraperwiki.scrape(mylist[index])
            c=len(html)
            a=html.find("returned no results")
            if (a>0):    
                print "out"
                continue # break loop and take next term          
            b=html.find("Your search for")
            d=html.find("results.<")
            i=html[b+35:-(c-d)]
            if int(i)>500:
                print "Term has more then 500 Result",i
                print link;
                scraperwiki.sqlite.execute("insert into Missinglink values (?)",(link))
                scraperwiki.sqlite.commit()
                continue # break loop and take next term
            n=int(i)
            for den in range(1,n):
                   stl= html.find("rowASRLodd",beg)
                   hy1=html.find("href=",stl)
                   hy2=html.find(">" ,hy1)
                   sou1=html[hy1+6:(hy2-1)]  
                   beg=hy2
                   html2 = scraperwiki.scrape("http://members.calbar.ca.gov"+sou1)
                   nm1=html2.find("End: Consumer Alert")
                   nm2=html2.find("Begin: Current Status")
                   add1=html2.find("Address:")
                   add2=html2.find("href",add1)
                   ph1=html2.find("Phone Number:")
                   ph2=html2.find("/tr",ph1)
                   st1=html2.find("Present")
                   st2=html2.find("Condition")
                   e1=html2.find("e-mail:")
                   e2=html2.find("<!-- It is")
                   estr=html2[e1:e2]
                   ce1=estr.find("Not Available")
                   if ce1<1:
                         em1=html2.find("display:inline;")
                         em2=html2.find("#",(em1-6))
                         em3=html2.find("{",em2)
                         email1=html2[em2+1:em3].strip()
                         email2=html2.find(email1)
                         email3=html2.find("span id",email2)
                         email4=html2[email2:email3].strip()
                         email5=html2.find(">",email2)
                         email6=html2[email5:email3].strip()
                         em1=0
                         em2=0
                         em3=0
                         email2=0
                         email3=0
                   else:
                         email6=""
                   d1=html2.find("tr1")
                   d2=html2.find("Admitted to The State Bar of California")
                   n1=html2[nm1+58:nm2-42].strip()
                   add=html2[add1+80:add2-40].strip()
                   add=add.replace("<br />","")
                   ph= html2[ph1+46:ph2-12].strip()
                   stat=html2[st1+38:st2-27].strip()
                   da=html2[d1+50:d2-43].strip()
                   Myaddress=add.replace(chr(34),"-")
                   print da
                   scraperwiki.sqlite.execute("insert into bbb values (?,?,?,?,?,?,?)",(n1,add,ph,stat,email6,da,sou1))
                   scraperwiki.sqlite.commit()
                   email6=""
        except urllib2.HTTPError, err:
            print err
            if err.getcode() == 404:
                continue #not a problem.  move on to next date.

