#!/usr/bin/python3.10
# 老秦官网 wcnb.love

import random 
from time import strftime ,localtime ,time ,sleep 
import json ,os ,re 
from webbrowser import open as dss 
import uuid 
try:
    import requests
    import urllib3 
    from urllib .parse import quote 
except:
    print("requests库未安装，尝试安装中")
    sleep(3)
    os.system("pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple")
    os.system("pip install requests")
    import requests
    from urllib .parse import quote 
    import urllib3 
    printt("成功安装requests库")
    
try:
    import lxml.html
except:
    print("lxml库未安装，尝试安装中")
    sleep(3)
    os.system("pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple")
    os.system("pkg install libxml2")
    os.system("pkg install libxslt")
    os.system("pip install lxml")
    import lxml.html
    printt("成功安装lxml库")

urllib3 .disable_warnings ()   
etree =lxml .html .etree 

def configs ():
    try :
        OOOOO000O00O00OOO =requests .get ("http://wcnb.love/66.json",timeout =5 ,verify =False ).json ()
    except :
        input ("连接服务器超时，回车退出程序")
        exit (0 )
    if OOOOO000O00O00OOO ["version"]==0 :
        printt ("工具停止使用:\n{}".format (OOOOO000O00O00OOO ["content"]))
    if OOOOO000O00O00OOO ["version"]>1.02 :
        printt ("检测到更新:\n更新版本号:{}\n更新内容:{}".format (OOOOO000O00O00OOO ["version"],OOOOO000O00O00OOO ["content"]))
        OOOOO0O000O000000 =requests .get (OOOOraindropO000O00O00OOO ["download"])
        with open ('知乎解析'+str (OOOOO000O00O00OOO ["version"])+'.exe','wb')as O0OOOOO00O000OO00 :
            O0OOOOO00O000OO00 .write (OOOOO0O000O000000 .content )
        if int (OOOOO000O00O00OOO ["force"])==1 :
            printt ('当前版本为强制更新，已下载到工具运行目录下')
            requests .get ("http://zhihu.hanbao16.top/log.php?log=更新成功&machine="+str (get_machine_code ()),timeout =5 ,verify =False )
            input ("回车退出")
            exit (0 )
        else :
            printt ('已下载到工具运行目录下')
    else :
        printt ("当前为最新版")
    if get_machine_code ()in OOOOO000O00O00OOO ["prohibit"]:
        input ("机器被封禁，禁止使用")
        exit (0 )
    printt (OOOOO000O00O00OOO ["notice"])
    return OOOOO000O00O00OOO 
def login ():
    OO0000000O0000000 =int (time ())
    OO00000OOO0O0OO0O =configs ()
    printt ("3秒后继续")
    sleep (3 )
    printt ("正在登录")
    OO00OO000OOO00O0O =OO00000OOO0O0OO0O ["login"]
    O0O00000O0OO00O00 =random .randrange (0 ,len (OO00OO000OOO00O0O ))
    OO00OO000OOO00O0O =OO00OO000OOO00O0O [O0O00000O0OO00O00 ]
    printt ("读取随机账号密码\n账号：{}\n密码：{}".format (OO00OO000OOO00O0O ,OO00OO000OOO00O0O ))
    OOO00OOO0OO0O0000 ="https://h.x360xs.com/index.php?m=user/ajax&format=jsonp&inputuserid="+quote (OO00OO000OOO00O0O )+"&password="+quote (OO00OO000OOO00O0O )+"&ajaxMethod=StaticLogin&autologinflag=1&method=_jqjsp&_"+str (OO0000000O0000000 )+"="
    OO00OOO0OO0OO000O ={"Referer":"https://h.x360xs.com/index.php?m=user/login","accept_language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"}
    OO0OOO0O0O00O0000 =requests .get (OOO00OOO0OO0O0000 ,headers =OO00OOO0OO0OO000O ,verify =False )
    O00OO0OOO0000O0OO =re .findall ("_jqjsp\((.*)\)",OO0OOO0O0O00O0000 .text )[0 ]
    O00OO0OOO0000O0OO =json .loads (O00OO0OOO0000O0OO )
    if O00OO0OOO0000O0OO ["return_code"]==10000 :
        printt ("登录成功")
        OOO0OO0O0O0O0O0O0 =requests .utils .dict_from_cookiejar (OO0OOO0O0O00O0000 .cookies )
        return OOO0OO0O0O0O0O0O0 
    else :
        printt ("登录失败,错误代码"+str (O00OO0OOO0000O0OO ["return_code"]))
        input ("回车退出")
        exit (0 )
def get_machine_code ():
    OO000O0OOOOO0O0OO =uuid .UUID (int =uuid .getnode ()).hex [-12 :]
    return OO000O0OOOOO0O0OO 
def search (OOO000OOO0OO0O00O ,O0OO000000O0OOO0O ):
    OOO000O00OO0OO0O0 ="https://h.x360xs.com/book/"
    OOO000O000O0OOO00 =""
    for OOOO0O0OOO000O000 in OOO000OOO0OO0O00O :
        OOO000O000O0OOO00 =OOO000O000O0OOO00 +str (OOOO0O0OOO000O000 )+"="+str (OOO000OOO0OO0O00O [OOOO0O0OOO000O000 ])+";"
    OOOOO0OO00O00O00O ={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0","Referer":"https://h.x360xs.com/search/","cookie":OOO000O000O0OOO00 }
    OO00O000O00O00OOO ={"ajaxMethod":"getsearchbooks","page":"1","pagesize":"10","isvip":"-1","cid":"-1","sort":"0","flag":"-1","searchkey":O0OO000000O0OOO0O ,"site":"-1","again":"0","range":"-1"}
    OO00OO00000OO0000 =requests .post (url =OOO000O00OO0OO0O0 ,data =OO00O000O00O00OOO ,headers =OOOOO0OO00O00O00O ,verify =False ).json ()
    return OO00OO00000OO0000 
def book_info (OO000O0OO00OO000O ,OOO00O0O000O0OO0O ):
    O0OOO00OOOO0OOO0O =""
    for O0O0O0OOO0O0O000O in OO000O0OO00OO000O :
        O0OOO00OOOO0OOO0O =O0OOO00OOOO0OOO0O +str (O0O0O0OOO0O0O000O )+"="+str (OO000O0OO00OO000O [O0O0O0OOO0O0O000O ])+";"
    O00OOO00OO0OOOO00 ={"Referer":"https://www.x360xs.com/login.php?jumpurl=%2Fmodules%2Farticle%2Fbookcase.php","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"}
    try :
        O0O00O00O0O0OO000 =re .findall (r"\d+.\d+|\d+",OOO00O0O000O0OO0O ["lastchaptername"])[0 ]
        O0O00O00O0O0OO000 =int (O0O00O00O0O0OO000 .replace (" ",""))
    except :
        O0O00O00O0O0OO000 =re .findall (r"\d+.\d+|\d+",OOO00O0O000O0OO0O ["lastchaptername"])[0 ]
        O0O00O00O0O0OO000 =int (O0O00O00O0O0OO000 .replace (" ",""))
    O0O0OOO00O0000O00 =O0O00O00O0O0OO000 //50 
    if O0O00O00O0O0OO000 %50 >0 :
        O0O0OOO00O0000O00 +=1 
    O0000OO0OOOOOO0OO =1 
    OOOOOO00O00O00OOO =dict ()
    while True :
        printt ("共{}页，当前第{}页".format (str (O0O0OOO00O0000O00 ),str (O0000OO0OOOOOO0OO )))
        O000O0OO0O00OO0OO =requests .get ("https://h.x360xs.com/book/"+OOO00O0O000O0OO0O ["bookid"]+"/0/"+str (O0000OO0OOOOOO0OO )+".html",headers =O00OOO00OO0OOOO00 ,verify =False ).text 
        O000O0OO0O00OO0OO =O000O0OO0O00OO0OO .replace ("  ","").replace ("\n","").replace ("\r","")
        OO0OO0O000OO00O00 =etree .HTML (O000O0OO0O00OO0OO )
        O0O0O000OOOO0O000 =OO0OO0O000OO00O00 .xpath ('/html/body/div[3]/div//div/div[2]/a/text()|/html/body/div[3]/div//div/div[2]/a/@href')
        O000O00OO00000OOO =0 
        for O0OOO0000OO0OO0OO in range (len (O0O0O000OOOO0O000 )//2 ):
            OO0OOOO0OOOOO00OO =str (re .findall (r"\d+.\d+|\d+",O0O0O000OOOO0O000 [O0OOO0000OO0OO0OO *2 +1 ])[0 ])
            '''try:
                book_n = str(re.findall("第(.*)节", text[ii*2+1])[0])
                book_n=book_n.replace(" ","")
            except:
                book_n = str(re.findall("第(.*)章", text[ii * 2 + 1])[0])
                book_n = book_n.replace(" ", "")'''
            OOOO0000O00OOOOOO =[O0O0O000OOOO0O000 [O0OOO0000OO0OO0OO *2 ],O0O0O000OOOO0O000 [O0OOO0000OO0OO0OO *2 +1 ]]
            OOOOOO00O00O00OOO [OO0OOOO0OOOOO00OO ]=OOOO0000O00OOOOOO 
            printt (O0O0O000OOOO0O000 [O0OOO0000OO0OO0OO *2 +1 ])
        OOOOOOOO0O00000OO =input ("老秦提示：请输入章节序号,回车进入下一页：")
        if OOOOOOOO0O00000OO =="":
            if O0000OO0OOOOOO0OO <O0O0OOO00O0000O00 :
                O0000OO0OOOOOO0OO +=1 
        elif OOOOOOOO0O00000OO .isdigit ():
            OO0O0O0O00O000000 ="https://h.x360xs.com"+OOOOOO00O00O00OOO [OOOOOOOO0O00000OO ][0 ]
            O000O0OO0O00OO0OO =requests .get (OO0O0O0O00O000000 ,headers =O00OOO00OO0OOOO00 ,verify =False ).text 
            O000O0OO0O00OO0OO =O000O0OO0O00OO0OO .replace ("  ","").replace ("\n","").replace ("\r","")
            OO0OO0O000OO00O00 =etree .HTML (O000O0OO0O00OO0OO )
            O0O0O000OOOO0O000 =OO0OO0O000OO00O00 .xpath ('/html/body/form/div[2]/div[5]/img/@onerror')[0 ]
            O0O0O000OOOO0O000 =O0O0O000OOOO0O000 [O0O0O000OOOO0O000 .find (OOO00O0O000O0OO0O ["bookid"]):]
            OO0OO0OOOOOO000OO =re .findall ("(.*)'.split",O0O0O000OOOO0O000 )[0 ]
            OO0OO0OOOOOO000OO =OO0OO0OOOOOO000OO .split ("|")[2 ]
            printt (OO0OO0OOOOOO000OO )
            O00OO00O0000OO000 =OO0O0O0O00O000000 
            O0O000OOO00O00OOO =OO0OO0O000OO00O00 .xpath ('/html/body/form/div[2]/div[2]/div/div//p/text()')
            while True :
                if "本章节未完结"in O000O0OO0O00OO0OO :
                    OO0O0O0O00O000000 ="https://h.x360xs.com/book/"+OOO00O0O000O0OO0O ["bookid"]+"/"+OO0OO0OOOOOO000OO +".html"
                    O0O000O00OOOO0O0O =page_next (O0OOO00OOOO0OOO0O ,OO0O0O0O00O000000 ,O00OO00O0000OO000 ,OOO00O0O000O0OO0O ["bookid"])
                    OO0OO0OOOOOO000OO =O0O000O00OOOO0O0O [0 ]
                    O000O0OO0O00OO0OO =O0O000O00OOOO0O0O [1 ]
                    O00OO00O0000OO000 =OO0O0O0O00O000000 
                    O0O000OOO00O00OOO .extend (O0O000O00OOOO0O0O [2 ])
                else :
                    OO00000000OOO000O =""
                    printt ("合并分页中")
                    for O00000OO0000O0OO0 in O0O000OOO00O00OOO :
                        OO00000000OOO000O +=O00000OO0000O0OO0 +"\n"
                        printt (O00000OO0000O0OO0 )
                    with open (OOOOOO00O00O00OOO [OOOOOOOO0O00000OO ][1 ]+".txt","w+",encoding ="UTF-8")as OOOOO0O0OOOOO000O :
                        OOOOO0O0OOOOO000O .write (OO00000000OOO000O )
                        printt ("成功写入文件{}.txt中".format (OOOOOO00O00O00OOO [OOOOOOOO0O00000OO ][1 ]))
                        try :
                            requests .get ("http://zhihu.hanbao16.top/log.php?log=搜索 "+OOOOOO00O00O00OOO [OOOOOOOO0O00000OO ][1 ]+"&machine="+str (get_machine_code ()),timeout =5 ,verify =False )
                        except :
                            pass 
                    break 
            break 
        else :
            printt ("请输入序号")
def page_next (O0O000OO0000000O0 ,OOO0OOOOO000O000O ,OOO0O0OOO00OOO00O ,O00OOO0OO0OO0OO0O ):
    O00OOOOO00OOOO0O0 ={"Cookie":O0O000OO0000000O0 ,"Referer":OOO0O0OOO00OOO00O ,"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"}
    O00O0O0O0000OOO00 =requests .get (OOO0OOOOO000O000O ,headers =O00OOOOO00OOOO0O0 ,verify =False ).text 
    O00O0O0O0000OOO00 =O00O0O0O0000OOO00 .replace ("  ","").replace ("\n","").replace ("\r","")
    OOOO000OO0OOOO0OO =etree .HTML (O00O0O0O0000OOO00 )
    O000OOO00OO0OOOOO =OOOO000OO0OOOO0OO .xpath ('/html/body/form/div[2]/div[5]/img/@onerror')[0 ]
    O000OOO00OO0OOOOO =O000OOO00OO0OOOOO [O000OOO00OO0OOOOO .find (O00OOO0OO0OO0OO0O ):]
    O0O0O00OOO000O0O0 =re .findall ("(.*)'.split",O000OOO00OO0OOOOO )[0 ]
    O0O0O00OOO000O0O0 =O0O0O00OOO000O0O0 .split ("|")[2 ]
    printt (O0O0O00OOO000O0O0 )
    O000OOO00OO0OOOOO =OOOO000OO0OOOO0OO .xpath ('/html/body/form/div[2]/div[2]/div/div//p/text()')
    return [O0O0O00OOO000O0O0 ,O00O0O0O0000OOO00 ,O000OOO00OO0OOOOO ]
def reg ():
    pass 
def main ():
    O0O00OO0000OO0OOO =login ()
    while True :
        OOO0OOOOO000O0O00 =input ("请输入书名或专栏名:")
        if OOO0OOOOO000O0O00 !="":
            OOOOOO000O00O0O0O =search (O0O00OO0000OO0OOO ,OOO0OOOOO000O0O00 )
            if OOOOOO000O00O0O0O ["Flag"]:
                OO00O0OOO0O0000OO =OOOOOO000O00O0O0O ["Data"]["search_response"]["books"]
                printt ("共找到{}本书".format (len (OO00O0OOO0O0000OO )))
                OO00OO0O000OOOOO0 =1 
                O00OOO000O0O0OO0O =dict ()
                for O00O000OO0OO000OO in OO00O0OOO0O0000OO :
                    OO00OOOOO00000OOO =re .sub ("\n","",O00O000OO0OO000OO ["description"])
                    printt ("序号：{}\n书名：{}\n作者：{}\n简介：{}".format (OO00OO0O000OOOOO0 ,O00O000OO0OO000OO ["bookname"],O00O000OO0OO000OO ["authorname"],OO00OOOOO00000OOO .replace (" ","")))
                    O00OOO000O0O0OO0O [OO00OO0O000OOOOO0 ]=O00O000OO0OO000OO 
                    OO00OO0O000OOOOO0 +=1 
                OO0O00OOO0O0000OO =eval (input ("选择你需要专栏或书籍的序号："))
                if OO0O00OOO0O0000OO in O00OOO000O0O0OO0O :
                    book_info (O0O00OO0000OO0OOO ,O00OOO000O0O0OO0O [OO0O00OOO0O0000OO ])
                else :
                    printt ("选择超出范围")
            OO0O00OOO0O0000OO =input ("直接回车退出程序\n输入1进入老秦官网\n输入2继续搜索\n请输入：")
            if OO0O00OOO0O0000OO =="":
                exit (0 )
            elif OO0O00OOO0O0000OO =="2":
                pass 
            else :
                printt ("老秦官网")
                try :
                    os .system ('am start -a android.intent.action.VIEW -d http://wcnb.love')
                except :
                    pass 
                try :
                    dss ("http://wcnb.love")
                except :
                    pass 
                sleep (4 )
                exit (0 )
        else :
            printt ("请输入书名")
def printt (O0OOO0OO00O0O0O00 ):
    def OOO0O0O00OOOO0O0O ():
        O00OOO0000000OO0O =int (time ())
        O00000OO0O00O0OOO =localtime (O00OOO0000000OO0O )
        O0OOO00000OO000O0 =strftime ("%Y-%m-%d",O00000OO0O00O0OOO )
        OO0OOO0OO0OO0OOOO =strftime ("%H:%M:%S",O00000OO0O00O0OOO )
        return OO0OOO0OO0OO0OOOO 
    O00O0OO0O0O00OO00 =O0OOO0OO00O0O0O00 .split ("\n")
    for OO0O0O00O0O0OO00O in O00O0OO0O0O00OO00 :
        print ("["+str (OOO0O0O00OOOO0O0O ())+"] "+str (OO0O0O00O0O0OO00O ))
if __name__ =='__main__':
    main ()
