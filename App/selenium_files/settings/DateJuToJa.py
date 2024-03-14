
import time
def this_time_is(sec):
    from datetime import datetime
    #now = time.localtime()
    
    #print( now.tm_year)   # 2019
    
    #print( now.tm_yday)   # 255
    #print(time.time())
    # current_time = sec

    time_string = f"{datetime.fromtimestamp(sec)}"

    return(f"{time_string[-8:]}")

# sec = 1693036494


# print(f"this time is: {this_time_is(sec)}")
def nowtimeis():
   import time
#now = time.localtime()
 
#print( now.tm_year)   # 2019
 
#print( now.tm_yday)   # 255
#print(time.time())
   current_time = time.localtime()

   time_string = time.strftime( "%H:%M:%S", current_time )

   return(time_string)   # 09/12/2019 16:01:21

#########################################################اين قسمت براي محاسبه فاصله زماني بين امروز و تاريخ تعيين شده در اينجا اولين روز 2010 استفاده شده است
import datetime
def diffNowDate(DateStr):
   from datetime import datetime
   fmt = '%Y-%m-%d'
   d2 = datetime.strptime(str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day), fmt)
   d1 = datetime.strptime(DateStr, fmt)
   return (d2-d1).days

#today is '2013-12-14'
#print( Diff )#//out = 13

###########################################################اين قسمت براي مشخص کردن نام روز هفته مي باشد

def daymark():
   Diff=diffNowDate('2020-10-09')
   if Diff > 0 :
   
      mod= (Diff %7)  
      if(mod==0):       FindDayMark=   "جمعه"
      elif(mod== 1):    FindDayMark=   "شنبه"
      elif(mod== 2):    FindDayMark=   "يكشنبه"
      elif(mod== 3):    FindDayMark=   "دوشنبه"
      elif(mod==4):    FindDayMark=   "سه شنبه"
      elif(mod== 5):    FindDayMark=   "چهار شنبه"
      elif(mod== 6):    FindDayMark=   "پنج شنبه"
      # print(FindDayMark)
   else:
      Diff=-Diff
      mod= (Diff %7)  
      if(mod==0):       FindDayMark=   "جمعه"
      elif(mod== 1):    FindDayMark=   "پنج شنبه"
      elif(mod== 2):    FindDayMark=   "چهار شنبه"
      elif(mod== 3):    FindDayMark=   "سه شنبه"
      elif(mod==4):    FindDayMark=   "دوشنبه"
      elif(mod== 5):    FindDayMark=   "يکشنبه"
      elif(mod== 6):    FindDayMark=   "شنبه"
   return FindDayMark

###########################################################بدست اوردن تاريخ روز 
def sgn(Diff):
      if Diff>0:return 1
      elif Diff<0 :return -1
      else:return 0
def todaydate():

   Diff=diffNowDate('2021-01-01')
   #print(Diff)
   d = 12#CDay(dateEnToFa)
   y = 1399#CYear(dateEnToFa)
   m = 10#CMonth(dateEnToFa)
   
   arrow=sgn(Diff)
   while( Diff):
      d = d + arrow
      #Select Case m
      if(m>= 1) and (m<= 6):
          if d > 31:
              d = 1
              m = m + 1
          elif d <= 0 :
              if m > 1:
                  m = m - 1
                  d = 31
              else:
                  m = 12
                  y = y - 1
                  if (y % 4) == 3 :
                      d = 30
                  else:
                      d = 29
                  
              
          
      if(m>= 7)and(m<= 11):
          if d > 30:
              d = 1
              m = m + 1
          elif d < 1 :
             m = m - 1
             if m > 6 :
                d = 30
             else: d = 31
          
      if m==12:
          if d < 1 :
              m = m - 1
              d = 30
          elif d == 30 :
            if (y % 4)!=3 :
              if arrow == 1 :
                   y = y + 1
                   m = 1
                   d = 1
              
           
          elif d > 30 :
            y = y + 1
            m = 1
            d = 1
       

      Diff = Diff -arrow# - Sgn(Diff)
      
#Wend
   std=str(d)
   if( len(std)<2):std="0"+std
   stm=str(m)
   if (len(stm)<2):stm="0"+stm
   sty=str(y)
   todayis=sty+"/"+stm+"/"+std
   # print(todayis)
   return todayis


# محاسبه اختلاف تعداد روز بین دو تاریخ شمسی
def whatIsDateWithDistance(startDate,distance):

    if distance < 0:
        arrow = -1
        myIter = 1
    elif distance > 0:
        arrow = 1
        myIter = -1
    else:
        return startDate

    arrowDate = startDate
    d = int(arrowDate[-2:])
    m = int(arrowDate[5:7])
    y = int(arrowDate[:4])

    #    distanceDays=0   
    while(distance != 0):#arrowDate != endDate
        

        d = d + arrow
        # print(d)
        # print(distance)
       
        distance += myIter
        # print(distance)
        #Select Case m
        if(m>= 1) and (m<= 6):
            if d > 31:
                d = 1
                m = m + 1
            elif d <= 0 :
                if m > 1:
                    m = m - 1
                    d = 31
                else:
                    m = 12
                    y = y - 1
                    if (y % 4) == 3 :
                        d = 30
                    else:
                        d = 29
                    
                
            
        if(m >= 7)and(m <= 11):
            if d > 30:
                d = 1
                m = m + 1
            elif d < 1 :
                m = m - 1
                if m > 6 :
                    d = 30
                else: d = 31
            
        if m==12:
            if d < 1 :
                m = m - 1
                d = 30
            elif d == 30 :
                if (y % 4)!=3 :
                    if arrow == 1 :
                        y = y + 1
                        m = 1
                        d = 1
                    
            
            elif d > 30 :
                y = y + 1
                m = 1
                d = 1
        

        # Diff = Diff -arrow# - Sgn(Diff)
    std=str(d)
    if( len(std)<2):std="0"+std
    stm=str(m)
    if (len(stm)<2):stm="0"+stm
    sty=str(y)
    dateConsider = sty+"/"+stm+"/"+std
        
    #Wend

    # print(todayis)
    return dateConsider
def jdataDistanceDays(startDate,endDate):

    if startDate>endDate:
        arrow = -1
    elif startDate<endDate:
        arrow = 1
    else:
        return 0

    arrowDate = startDate

    distanceDays=0   
    while( arrowDate != endDate):
        
        d = int(arrowDate[-2:])
        m = int(arrowDate[5:7])
        y = int(arrowDate[:4])

        d = d + arrow
        distanceDays += arrow
        #Select Case m
        if(m>= 1) and (m<= 6):
            if d > 31:
                d = 1
                m = m + 1
            elif d <= 0 :
                if m > 1:
                    m = m - 1
                    d = 31
                else:
                    m = 12
                    y = y - 1
                    if (y % 4) == 3 :
                        d = 30
                    else:
                        d = 29
                    
                
            
        if(m>= 7)and(m<= 11):
            if d > 30:
                d = 1
                m = m + 1
            elif d < 1 :
                m = m - 1
                if m > 6 :
                    d = 30
                else: d = 31
            
        if m==12:
            if d < 1 :
                m = m - 1
                d = 30
            elif d == 30 :
                if (y % 4)!=3 :
                    if arrow == 1 :
                        y = y + 1
                        m = 1
                        d = 1
                    
            
            elif d > 30 :
                y = y + 1
                m = 1
                d = 1
        

        # Diff = Diff -arrow# - Sgn(Diff)
        std=str(d)
        if( len(std)<2):std="0"+std
        stm=str(m)
        if (len(stm)<2):stm="0"+stm
        sty=str(y)
        arrowDate=sty+"/"+stm+"/"+std
        
    #Wend

    # print(todayis)
    return distanceDays



def NextPrevMonth(startDate,thisArrow):

    if thisArrow < 0:
        arrow = -1
        myIter = 1
    elif thisArrow > 0:
        arrow = 1
        myIter = -1
    else:
        return startDate

    arrowDate = startDate
    d = int(arrowDate[-2:])
    m = int(arrowDate[5:7])
    y = int(arrowDate[:4])

    #    distanceDays=0   
    # while(distance != 0):#arrowDate != endDate
    m+= arrow    

    if m > 12:
        m = 1
        y += 1
    elif m <= 0:
        m = 12
        y -= 1
        # if (y % 4) == 3 :
        #     if d > 30: d = 30
        # else:
        #     if d>29:            d = 29





    # d = d + arrow
    # # print(d)
    # # print(distance)
    
    # distance += myIter
    # # print(distance)
    # #Select Case m
    # if(m>= 1) and (m<= 6):
    #         if d > 31:
    #             d = 1
    #             m = m + 1
    #         elif d <= 0 :
    #             if m > 1:
    #                 m = m - 1
    #                 d = 31
    #             else:
    #                 m = 12
    #                 y = y - 1
    #                 if (y % 4) == 3 :
    #                     d = 30
    #                 else:
    #                     d = 29
                    
                
            
    #     if(m >= 7)and(m <= 11):
    #         if d > 30:
    #             d = 1
    #             m = m + 1
    #         elif d < 1 :
    #             m = m - 1
    #             if m > 6 :
    #                 d = 30
    #             else: d = 31
            
    #     if m==12:
    #         if d < 1 :
    #             m = m - 1
    #             d = 30
    #         elif d == 30 :
    #             if (y % 4)!=3 :
    #                 if arrow == 1 :
    #                     y = y + 1
    #                     m = 1
    #                     d = 1
                    
            
    #         elif d > 30 :
    #             y = y + 1
    #             m = 1
    #             d = 1
        

        # Diff = Diff -arrow# - Sgn(Diff)
    std=str(d)
    if( len(std)<2):std="0"+std
    stm=str(m)
    if (len(stm)<2):stm="0"+stm
    sty=str(y)
    dateConsider = sty+"/"+stm+"/"+std
        
    #Wend

    # print(todayis)
    return dateConsider

def getDateTimeForFileName():
    
    todayIs = todaydate()
    todayIs = todayIs.replace("/","-")
    
    timeIs = int(time.monotonic())
    return f"{todayIs} {timeIs}"
