import requests
import json
import time
import timeit
import os
import random
from datetime import datetime
from dateutil import tz




result=''
tx_com_cookie=''

tx_rd_cookie11=''
tx_rd_cookie12=''
tx_rd_cookie21=''
tx_rd_cookie22=''
tx_rd_cookie31=''
tx_rd_cookie32=''
tx_rd_cookie41=''
tx_rd_cookie42=''
   
tx_vd_cookie11=''
tx_vd_cookie12=''
tx_vd_cookie21=''
tx_vd_cookie22=''
tx_vd_cookie31=''
tx_vd_cookie32=''
tx_vd_cookie41=''
tx_vd_cookie42=''

vcookiesList1=[]
rcookiesList1=[]
vcookiesList2=[]
rcookiesList3=[]
vcookiesList3=[]
rcookiesList4=[]
vcookiesList4=[]
cmcookiesList=[]
   
headers = {
        'User-Agent': 'QQNews/6.1.30 (iPhone; iOS 12.4; Scale/2.00)','Content-Type':'application/x-www-form-urlencoded'}

def tx_user():
    try:
        response = requests.post('https://r.inews.qq.com/i/getUserCheckInfo?',headers=headers)
        obj=response.json()
        msg=f"""用户名:{obj['data']['nick']}"""
    except Exception as e:
        msg=str(e)
    loger(msg)

def tx_signday():
    try:
        response = requests.get('https://api.inews.qq.com/task/v1/user/signin/add?',headers=headers)
        #print(response.json())
        obj=response.json()
        msg=f"""连续签到:{obj['data']['signin_days']}天"""
    except Exception as e:
        msg=str(e)
    loger(msg)

   
    
def tx_task(rck,vck):
    try:
        response = requests.get('https://api.inews.qq.com/activity/v1/activity/info/get?activity_id=stair_redpack_chajian&'+rck,headers=headers)
        #print(response.json())
        obj=response.json()
        tx1 = obj['data']['award'][0]['openable']
        tx2 = obj['data']['award'][1]['openable']
        msg=f"""[阅读红包]{obj['data']['award'][0]['opened']}-{obj['data']['award'][0]['total']}-{obj['data']['award'][0]['openable']}[视频红包]{obj['data']['award'][1]['opened']}-{obj['data']['award'][1]['total']}-{obj['data']['award'][1]['openable']}[阅读任务]{obj['data']['award'][0]['title']}[视频任务]{obj['data']['award'][1]['title']};"""
    except Exception as e:
          msg=str(e)
          tx1=0
          tx2=0
    print(msg)
    loger(msg)
    if tx1>0:
         print('阅读红包')
         tx_openred1(rck)
         time.sleep(1)
    if tx2>0:
         print('视频红包')
         tx_openred2(vck)
         time.sleep(1)
    try:
       if obj['data']['award'][0]['opened'] != obj['data']['award'][0]['total'] and obj['data']['award'][0]['opened'] <6:
       
         tx_read(rck)
         time.sleep(1)


       if obj['data']['award'][1]['opened'] != obj['data']['award'][1]['total'] and obj['data']['award'][1]['opened'] <6:
       
         tx_video(vck)
    except Exception as e:
        msg=str(e)
        #loger(msg)
        tx_read(rck)
        tx_video(vck)
        loger(msg)
    
def tx_read(rck):
    body ='event=article_read'
    response = requests.post('https://api.inews.qq.com/event/v1/user/event/report?'+rck,headers=headers,data=body)
    print(response.json())
    obj=response.json()
    msg='阅读:'+obj['info']+'✅'
    loger(msg)
   
      
def tx_video(vck):
    body ='event=video_read&extend=%7B%22video_id%22%3A%2220200622V0CGJH00%22%7D'
    response = requests.post('https://api.inews.qq.com/event/v1/user/event/report?'+vck,headers=headers,data=body)
    obj1=response.json()
    msg='视频:'+obj1['info']+'✅'
    loger(msg)
 
    
def tx_openred1(rck):
    body ='redpack_type=article&activity_id=stair_redpack_chajian'
    
    response = requests.post('https://api.inews.qq.com/activity/v1/activity/redpack/get?'+rck,headers=headers,data=body)

    obj2=response.json()
    msg='阅读红包'+obj2['info']+'✅'
    loger(msg)
    
def tx_openred2(vck):
    body ='redpack_type=video&activity_id=stair_redpack_chajian'
    
    response = requests.post('https://api.inews.qq.com/activity/v1/activity/redpack/get?'+vck,headers=headers,data=body)
    #print(response.text)
    obj=response.json()
    msg='视频红包'+obj['info']+'✅'
    loger(msg)
    
def tx_wallet():
    try:
        response = requests.get('https://api.inews.qq.com/activity/v1/usercenter/activity/list?isJailbreak=0',headers=headers)
    #print(response.json())
        obj=response.json()
        msg=f"""金币:{obj['data']['wealth'][0]['title']}红包:{obj['data']['wealth'][1]['title']}"""
    except Exception as e:
        msg=str(e)
    loger(msg)
    
    
def showmsg(m):
    #purl = "https://api.day.app/"+xmly_bark_cookie+"/"+t+"/"+m
    #response = requests.post(purl)
    #print(response.text)
    global result
    #print(result)
    result =''
   
def loger(m):
   print(m)
   global result
   result +=m+'\n'
    
def check():
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))

   global tx_com_cookie
   
   global tx_rd_cookie11
   global tx_rd_cookie12
   global tx_rd_cookie21
   global tx_rd_cookie22
   global tx_rd_cookie31
   global tx_rd_cookie32
   global tx_rd_cookie41
   global tx_rd_cookie42
   
   global tx_vd_cookie11
   global tx_vd_cookie12
   global tx_vd_cookie21
   global tx_vd_cookie22
   global tx_vd_cookie31
   global tx_vd_cookie32
   global tx_vd_cookie41
   global tx_vd_cookie42

   

   if "TX_COM_COOKIE" in os.environ:
       tx_com_cookie = os.environ["TX_COM_COOKIE"]
     
     
   if "TX_RD_COOKIE11" in os.environ:
      tx_rd_cookie11 = os.environ["TX_RD_COOKIE11"]
   if "TX_RD_COOKIE12" in os.environ:
      tx_rd_cookie12 = os.environ["TX_RD_COOKIE12"]
   if "TX_RD_COOKIE21" in os.environ:
      tx_rd_cookie21 = os.environ["TX_RD_COOKIE21"]
   if "TX_RD_COOKIE21" in os.environ:
      tx_rd_cookie21 = os.environ["TX_RD_COOKIE22"]
   if "TX_RD_COOKIE31" in os.environ:
      tx_rd_cookie31 = os.environ["TX_RD_COOKIE31"]
   if "TX_RD_COOKIE32" in os.environ:
      tx_rd_cookie32 = os.environ["TX_RD_COOKIE32"]
   if "TX_RD_COOKIE41" in os.environ:
      tx_rd_cookie41 = os.environ["TX_RD_COOKIE41"]
   if "TX_RD_COOKIE42" in os.environ:
      tx_rd_cookie42 = os.environ["TX_RD_COOKIE42"]
      
   if "TX_VD_COOKIE11" in os.environ:
      tx_vd_cookie11 = os.environ["TX_VD_COOKIE11"]
   if "TX_VD_COOKIE12" in os.environ:
      tx_vd_cookie12 = os.environ["TX_VD_COOKIE12"]
   if "TX_VD_COOKIE21" in os.environ:
      tx_vd_cookie21 = os.environ["TX_VD_COOKIE21"]
   if "TX_VD_COOKIE12" in os.environ:
      tx_vd_cookie22 = os.environ["TX_VD_COOKIE22"]
   if "TX_VD_COOKIE31" in os.environ:
      tx_vd_cookie31 = os.environ["TX_VD_COOKIE31"]
   if "TX_VD_COOKIE32" in os.environ:
      tx_vd_cookie32 = os.environ["TX_VD_COOKIE32"]
   if "TX_VD_COOKIE11" in os.environ:
      tx_vd_cookie41 = os.environ["TX_VD_COOKIE41"]
   if "TX_VD_COOKIE12" in os.environ:
      tx_vd_cookie42 = os.environ["TX_VD_COOKIE42"]
      

      
      
      
   if tx_com_cookie:
      for line in tx_com_cookie.split('\n'):
         if not line:
            continue 
         cmcookiesList.append(line.strip())
   else:
     print('DTask is over.')
     exit()

   if tx_rd_cookie11 and tx_rd_cookie12:
      for line in tx_rd_cookie11.split('\n'):
         if not line:
            continue 
         rcookiesList1.append(line.strip())
      for line in tx_rd_cookie12.split('\n'):
         if not line:
            continue 
         rcookiesList1.append(line.strip())
   if tx_rd_cookie21 and tx_rd_cookie22:
      for line in tx_rd_cookie21.split('\n'):
         if not line:
            continue 
         rcookiesList2.append(line.strip())
      for line in tx_rd_cookie22.split('\n'):
         if not line:
            continue 
         rcookiesList2.append(line.strip())
         
   if tx_rd_cookie31 and tx_rd_cookie32:
      for line in tx_rd_cookie31.split('\n'):
         if not line:
            continue 
         rcookiesList3.append(line.strip())
      for line in tx_rd_cookie32.split('\n'):
         if not line:
            continue 
         rcookiesList3.append(line.strip())
   if tx_rd_cookie41 and tx_rd_cookie42:
      for line in tx_rd_cookie41.split('\n'):
         if not line:
            continue 
         rcookiesList4.append(line.strip())
      for line in tx_rd_cookie42.split('\n'):
         if not line:
            continue 
         rcookiesList4.append(line.strip())
         
   if tx_vd_cookie11 and tx_vd_cookie12:
      for line in tx_vd_cookie11.split('\n'):
         if not line:
            continue 
         vcookiesList1.append(line.strip())
      for line in tx_vd_cookie12.split('\n'):
         if not line:
            continue 
         vcookiesList1.append(line.strip())
   if tx_vd_cookie21 and tx_vd_cookie22:
      for line in tx_vd_cookie21.split('\n'):
         if not line:
            continue 
         vcookiesList2.append(line.strip())
      for line in tx_vd_cookie22.split('\n'):
         if not line:
            continue 
         vcookiesList2.append(line.strip())
         
   if tx_vd_cookie31 and tx_vd_cookie32:
      for line in tx_vd_cookie31.split('\n'):
         if not line:
            continue 
         vcookiesList3.append(line.strip())
      for line in tx_vd_cookie32.split('\n'):
         if not line:
            continue 
         vcookiesList3.append(line.strip())
   if tx_vd_cookie41 and tx_vd_cookie42:
      for line in tx_vd_cookie41.split('\n'):
         if not line:
            continue 
         vcookiesList4.append(line.strip())
      for line in tx_vd_cookie42.split('\n'):
         if not line:
            continue 
         vcookiesList4.append(line.strip())
         
         
def getRD_ck(index):
   print(index)
   tx_ck1=''
   if index==1 and len(rcookiesList1)>0:
      tx_ck1=random.choice(rcookiesList1)
   elif index==2 and len(rcookiesList2)>0:
      tx_ck1=random.choice(rcookiesList2)
   elif index==3 and len(rcookiesList3)>0:
      tx_ck1=random.choice(rcookiesList3)
   elif index==4 and len(rcookiesList4)>0:
      tx_ck1=random.choice(rcookiesList4)
   return tx_ck1
def getVD_ck(index):
   tx_ck2=''
   if index==1 and len(vcookiesList1)>0:
      tx_ck2=random.choice(vcookiesList1)
   elif index==2 and len(vcookiesList2)>0:
      tx_ck2=random.choice(vcookiesList2)
   elif index==3 and len(vcookiesList3)>0:
      tx_ck2=random.choice(vcookiesList3)
   elif index==4 and len(vcookiesList4)>0:
      tx_ck2=random.choice(vcookiesList4)
   return tx_ck2





def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
@clock
def start():
   check()
   print(cmcookiesList)
   index=0
   for count in cmcookiesList:
     index+=1
     if index!=1:
     	  continue
     print(f'''>>>>>>>>>【账号{str(index)}开始''')
     headers['Cookie']=count
     tx_user()
     tx_signday()
     tx_task(getRD_ck(index),getVD_ck(index))
     tx_wallet()
     showmsg(result)
     
     
     
def main_handler(event, context):
    return start()

if __name__ == '__main__':
       start()
  
