import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *

def _createFile(dfData,dfDataLast,minDate,maxDate,phase):
        selectedOption ="003"
        folderName = f'{selectedOption}رشد میانگین تعداد فاکتورهای روزانه شعب در سال 1401 نسبت به سال 1400'        
        df_ans=pd.DataFrame()
        
        print(_make_farsi_text("برنامه در حال انجام پردازش می باشد لطفا صبر نمایید"))
    
    
                    
        while len(dfData):
            # try:
            
            branch = dfData.iloc[0,tjIndex.branch]
            # print(branch)
            dfBranchs=dfData.loc[dfData[tjCol.branch]==branch]
            dfDiff=dfBranchs.groupby(by=tjCol.history).count()
            days=len(dfDiff)
            count = len(dfBranchs)
            average = count//days
            print(f"average factor hai shobe {branch} = {average}")
            df_ans = df_ans.append({tjCol.branch:branch,tjCol.average:average},ignore_index=True)
            dfData=dfData.loc[dfData[tjCol.branch]!=branch]
            
        

        df_ansOld = pd.DataFrame()
                    
        while len(dfDataLast):
            # try:
            
            branch = dfDataLast.iloc[0,tjIndex.branch]
            # print(branch)
            dfBranchs=dfDataLast.loc[dfDataLast[tjCol.branch]==branch]
            dfDiff=dfBranchs.groupby(by=tjCol.history).count()
            days=len(dfDiff)
            count = len(dfBranchs)
            average = count//days
            print(f"average tedad factor hai shobe {branch} = {average}")
            df_ansOld = df_ansOld.append({tjCol.branch:branch,tjCol.average:average},ignore_index=True)
            dfDataLast=dfDataLast.loc[dfDataLast[tjCol.branch]!=branch]
            
        
        

        df_analyze = pd.DataFrame()
        dfData = df_ansOld.copy()
        while len(df_ans):
            branch = df_ans.iloc[0, 0]
            dfThis = df_ans.loc[df_ans[tjCol.branch]==branch]
            dfLast = df_ansOld.loc[df_ansOld[tjCol.branch]==branch]
            try:
                countLast = int(dfLast.iloc[0,1])
            except:
                countLast = 0
            try:
                countThis = int(dfThis.iloc[0,1])
            except:
                countThis = 0
            print(f"{branch} :{countThis}")
         
            try:
                if countLast== 0:
                    growth=100
                else:
                    growth = (countThis-countLast)/countLast*100
                    df_analyze= df_analyze.append({tjCol.branch:branch,otherCol.growth:growth,
                        tjCol.average:countThis, otherCol.average:countLast},ignore_index=True)
            except:
                growth=0
                # growth =100 - (countLast-countThis)/countThis*100
            
            df_ans = df_ans.loc[df_ans[tjCol.branch]!=branch]
        
        
        df_analyze.to_excel(f"{folderName} {phase}.xlsx" , index = False)
        df_ans = df_analyze.copy()
        df_ans = df_ans.sort_values(by=otherCol.growth)
        # df_ans.to_excel(f"{fileName}.xlsx" , index = False) 

        
        from codes.charts import horizontalBarPlot as hbp
        Datas = []
        AxisLabels = []
        
        for i in range(len(df_ans)):
            AxisLabels.append(df_ans.iloc[i,0])
            Datas.append(int(df_ans.iloc[i,1]))
            
        fileName = "رشد میانگین تعداد فاکتورهای روزانه شعب هانی مون"
        titleBar= _make_farsi_text(fileName)
        fileName = f"{fileName} در {phase} {maxDate} نسبت به {phase} {minDate}"
        # titleDetailChart = _make_farsi_text("تعداد فاکتور های هر شعبه")
        titleDetailChart = _make_farsi_text(fileName)
        titleSource = _make_farsi_text("طراحی شده: توسط مجموعه عطر هانی مون")
        Quality ="%"
        color = PINK
        hbp.showHorizontalPlot(Datas,AxisLabels,titleBar,titleDetailChart,titleSource,Quality,fileName, color)
        
        




def invoicesGrow() :
        selectedOption = "3"
        while len(selectedOption)<3:
            selectedOption = "0" + selectedOption
        folderName = f'{selectedOption}رشد میانگین تعداد فاکتورهای روزانه شعب در سال 1401 نسبت به سال 1400'
        
        print(" ")
        print(_make_farsi_text("انتخاب شما"))
        print(_make_farsi_text(folderName))
        
        df_all = loadData(myDataType_names.cumulativeSales,folderName)
        thisPath= os.getcwd()        
        
        
        # dfData = df_all.copy()
        # maxDate = dfData[tjCol.history].max()
        # minDate = dfData[tjCol.history].min()

        maxDate = df_all[tjCol.history].max()
        minDate = df_all[tjCol.history].min()
        minDate = "1401/01/01"
        maxDate = "1401/12/29"
        maxD=maxDate[:4]
        dfData = df_all.loc[df_all[tjCol.history]>=minDate]
        dfData = dfData.loc[dfData[tjCol.history]<=maxDate]

        minDate = "1400/01/01"
        maxDate = "1400/12/29"
        dfDataLast = df_all.loc[df_all[tjCol.history]>=minDate]
        dfDataLast = dfDataLast.loc[dfDataLast[tjCol.history]<=maxDate]
        minD = minDate[:4]


        _createFile(dfData=dfData,dfDataLast=dfDataLast,minDate=minD,maxDate=maxD, phase="بهار، تابستان، پاییز")
        
        for season in yearSeasons.Seasons:
            if season!="04":
                print(season)
                year ="1401/"
                minDate=year+yearSeasons.Seasons[season][seasonCol.start]
                maxDate = year+yearSeasons.Seasons[season][seasonCol.end]
                phase = yearSeasons.Seasons[season][seasonCol.name]
                dfData = df_all.loc[df_all[tjCol.history]>=minDate]
                if len(dfData): dfData = dfData.loc[dfData[tjCol.history]<=maxDate]
                if len(dfData):
                    year ="1400/"
                    minDate=year+yearSeasons.Seasons[season][seasonCol.start]
                    maxDate = year+yearSeasons.Seasons[season][seasonCol.end]
                    phase = yearSeasons.Seasons[season][seasonCol.name]
                    dfDataLast = df_all.loc[df_all[tjCol.history]>=minDate]
                    dfDataLast = dfDataLast.loc[dfDataLast[tjCol.history]<=maxDate]

                    if len(dfDataLast):
                        extPath=f"{season}-{phase}"
                        try:
                            os.mkdir(extPath)
                        except:
                            pass
                        os.chdir(extPath)
                        _createFile(dfData=dfData,dfDataLast=dfDataLast,minDate=minD,maxDate=maxD, phase=phase)
                        os.chdir(thisPath)
                        print(season)
            
invoicesGrow()


