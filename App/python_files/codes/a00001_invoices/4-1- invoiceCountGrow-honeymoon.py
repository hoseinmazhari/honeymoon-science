import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *

def _createFile(dfData, phase,color,season,func,Quality,colName):
        # selectedOption ="003"
        folderName = f"{func} ({phase})"
        df_ans = dfData.copy()
        # df_ansOld = dfLastData.copy()
        # tjIndex = getIndexTj(dfData)
        # print(_make_farsi_text("برنامه در حال انجام پردازش می باشد لطفا صبر نمایید"))
        
        # df_analyze.to_excel(f"{folderName}.xlsx" , index = False)
        # df_ans = df_analyze.copy()
        df_ans = df_ans.sort_values(by=colName)
        df_ans.to_excel(f"{season} {func}.xlsx" , index = False) 

        
        from codes.charts import horizontalBarPlot as hbp
        Datas = []
        AxisLabels = []
        
        for i in range(len(df_ans)):
            AxisLabels.append(df_ans.iloc[i,0])
            Datas.append(int(df_ans.iloc[i,1])) # type: ignore
            
        fileName = func
        titleBar= _make_farsi_text(fileName)
        # fileName = f"{fileName} در {phase} نسبت به {phase} {lastYear}"
        fileName=folderName
        # titleDetailChart = _make_farsi_text("تعداد فاکتور های هر شعبه")
        titleDetailChart = _make_farsi_text(fileName)
        fileName = f"{season}- {fileName}"
        # titleSource = _make_farsi_text("طراحی شده: توسط مجموعه عطر هانی مون")
        
        # color = PINK
        # des = ""
        hbp.showHorizontalPlot(Datas,AxisLabels,titleBar,titleDetailChart,titleSource,Quality,fileName, color,des)
        
        




def invoicesGrow() :
        selectedOption = "1"
        while len(selectedOption)<5:
            selectedOption = "0" + selectedOption
        selectedOption += "- 4"
        func = f"رشد میانگین تعداد فاکتورهای روزانه مجموعه هانی مون از سال 1397 تا سال 1402"
        folderName = f"{selectedOption}- {func}"
        
        print(" ")
        print(_make_farsi_text("انتخاب شما"))
        print(_make_farsi_text(folderName))
        
        df_all = loadData(myDataType_names.cumulativeSales,folderName)
        # thisPath= os.getcwd()        
        df_all=df_all[[tjCol.history]]        
        
                    
        years= [1397,1398,1399,1400,1401,1402]
        
        colors = [VIVA,GREEN,PINK,YELLOW,BLUE,color1401]
        colorIndex = -1
        
        for season in yearSeasons.Seasons:
            df_ansOld = pd.DataFrame()
            df_ans = pd.DataFrame()
            df_analyze = pd.DataFrame()
            colorIndex += 1
            color = colors[colorIndex]
            # colorIndex += 1
            phase = yearSeasons.Seasons[season][seasonCol.name]
            for year in years:
                yearQuantityDetail.__init__(yearQuantityDetail) # type: ignore
                minDate=f"{year}/{yearSeasons.Seasons[season][seasonCol.start]}"
                maxDate = f"{year}/{yearSeasons.Seasons[season][seasonCol.end]}"
                if season == "04" or season == "00":
                    if year%4==3:
                        maxDate= f"{year}/12/30"
                dfData = df_all.loc[df_all[tjCol.history]>=minDate]
                dfData = dfData.loc[dfData[tjCol.history]<=maxDate]
                lastYear = (int(year)-1)
                minDateLast=f"{lastYear}/{yearSeasons.Seasons[season][seasonCol.start]}"
                maxDateLast = f"{lastYear}/{yearSeasons.Seasons[season][seasonCol.end]}"
                if season == "04" or season == "00":
                    if lastYear%4==3:
                        maxDateLast= f"{lastYear}/12/30"
                
                # phase = yearSeasons.Seasons[season][seasonCol.name]
                dfLastData = df_all.loc[df_all[tjCol.history]>=minDateLast]
                dfLastData = dfLastData.loc[dfLastData[tjCol.history]<=maxDateLast]

                # اگر در این قسمت پوشه مربوط به هر فصل و سال را بسازیم نیازی به جدا کردن شعب نیست

                if len(dfData):
                    if len(dfLastData):
                        if year != 1397:
                            dfDiff=dfData.groupby(by=tjCol.history).count()
                            days=len(dfDiff)
                            count = len(dfData)
                            average = count//days
                            df_ans = df_ans.append({"سال":{year},tjCol.average:average},ignore_index=True) # type: ignore

                            dfDiff=dfLastData.groupby(by=tjCol.history).count()
                            days=len(dfDiff)
                            count = len(dfLastData)
                            averageOld = count//days
                            df_ansOld = df_ansOld.append({"سال":{year},tjCol.average:averageOld},ignore_index=True) # type: ignore
                            if averageOld== 0:
                                growth=100
                            else:
                                growth = (average-averageOld)/averageOld*100
                                df_analyze= df_analyze.append({"بازه": f"رشد {year} نسبت به {lastYear}",otherCol.growth:growth},ignore_index=True) # type: ignore
                            
            if len(df_analyze):
                    colName = otherCol.growth
                    Quality ="%"
                    _createFile(dfData=df_analyze, phase=phase,color=color,season=season,func=func,colName=colName,Quality=Quality)





        """
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
        dfLastData = df_all.loc[df_all[tjCol.history]>=minDate]
        dfLastData = dfLastData.loc[dfLastData[tjCol.history]<=maxDate]
        minD = minDate[:4]


        _createFile(dfData=dfData,dfLastData=dfLastData,minDate=minD,maxDate=maxD, phase="بهار، تابستان، پاییز")
        
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
                    dfLastData = df_all.loc[df_all[tjCol.history]>=minDate]
                    dfLastData = dfLastData.loc[dfLastData[tjCol.history]<=maxDate]

                    if len(dfLastData):
                        extPath=f"{season}-{phase}"
                        try:
                            os.mkdir(extPath)
                        except:
                            pass
                        os.chdir(extPath)
                        _createFile(dfData=dfData,dfLastData=dfLastData,minDate=minD,maxDate=maxD, phase=phase)
                        os.chdir(thisPath)
                        print(season)
            """
invoicesGrow()


