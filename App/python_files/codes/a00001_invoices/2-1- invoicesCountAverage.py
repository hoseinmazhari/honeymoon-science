import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *

def _createFile(dfData,minDate,maxDate,phase,selectedOption,color,season,year,Quality,func):

        tjIndex = getIndexTj(dfData)
        df_ans = pd.DataFrame()
        while len(dfData):

            branch = dfData.iloc[0,tjIndex.branch]

            dfBranchs = dfData.loc[dfData[tjCol.branch]==branch]

            dfDiff = dfBranchs.groupby(by=tjCol.history).count()
            days = len(dfDiff)

            # msg = _make_farsi_text("تعداد فاکتور های شعبه ")
            # print(f"{_make_farsi_text(branch)} {msg} = {len(dfBranchs)} در {days} روز")

            average = len(dfBranchs)//days
            df_ans = df_ans.append({tjCol.branch:f"از {days} روز فعالیت "+branch,tjCol.average:average},ignore_index=True) # type: ignore
            dfData = dfData.loc[dfData[tjCol.branch] != branch]
                
        fileName = (f"{year} {season}- {phase} {func}")
        fileName += f" از {minDate.replace('/','-')} تا {maxDate.replace('/','-')}"
        df_ans = df_ans.sort_values(by=tjCol.average)
        df_ans.to_excel(f"{fileName}.xlsx",index=False) 


        from codes.charts import horizontalBarPlot as hbp
        Datas = []
        AxisLabels = []
        
        for i in range(len(df_ans)):
            AxisLabels.append(df_ans.iloc[i,0])
            Datas.append(int(df_ans.iloc[i,1])) # type: ignore
            
                
        titleBar= _make_farsi_text(func)
        
        # titleDetailChart = _make_farsi_text("تعداد فاکتور های هر شعبه")
        titleDetailChart = _make_farsi_text(f" بر اساس تعداد روز فعال از {minDate} تا {maxDate} ({phase})")+ titleBar # type: ignore
        # titleSource = _make_farsi_text("طراحی شده: توسط مجموعه عطر هانی مون")
        
        # color = PINK
        # des=""
        hbp.showHorizontalPlot(Datas,AxisLabels,titleBar,titleDetailChart,titleSource,Quality,fileName, color,des)
        

def invoiceAverageCount() :
        selectedOption="1"
        while len(selectedOption)<5:
            selectedOption = "0" + selectedOption
        # شروع برنامه
        func = "میانگین تعداد فاکتورهای روزانه شعب هانی مون"
        selectedOption += "- 2"
        folderName = f"{selectedOption}-{func}"
        
        print(" ")
        print(_make_farsi_text("انتخاب شما"))
        print(_make_farsi_text(folderName))
        
        df_all = loadData(myDataType_names.cumulativeSales,folderName)
        df_all = df_all[[tjCol.history,tjCol.branch]]
        thisPath= os.getcwd()

        
        years= [1397,1398,1399,1400,1401,1402]
        
        colors = [VIVA,GREEN,PINK,YELLOW,BLUE,color1401]
        
        for year in years:
            os.chdir(thisPath)
            try:
                 os.mkdir(f"{year}")
                 os.chdir(f"{thisPath}/{year}")
            except:
                 os.chdir(f"{thisPath}/{year}")
            colorIndex = -1
            for season in yearSeasons.Seasons:
                colorIndex += 1
                color = colors[colorIndex]
                # yearQuantityDetail.__init__(yearQuantityDetail) # type: ignore
                minDate=f"{year}/{yearSeasons.Seasons[season][seasonCol.start]}"
                maxDate = f"{year}/{yearSeasons.Seasons[season][seasonCol.end]}"
                if season == "04" or season == "00":
                    if year %4 == 3:
                        maxDate= f"{year}/12/30"
                
                phase = yearSeasons.Seasons[season][seasonCol.name]
                dfData = df_all.loc[df_all[tjCol.history]>=minDate]
                dfData = dfData.loc[dfData[tjCol.history]<=maxDate]

                # اگر در این قسمت پوشه مربوط به هر فصل و سال را بسازیم نیازی به جدا کردن شعب نیست

                if len(dfData):
                    # colName = tjCol.quantity
                    Quality ="فاکتور"
                    _createFile(dfData=dfData,minDate=minDate,maxDate=maxDate, phase=phase,selectedOption=selectedOption,color=color,season=season,year=year,Quality=Quality,func = func)






        # dfData = df_all.copy()
        # maxDate = dfData[tjCol.history].max()
        # minDate = dfData[tjCol.history].min()
"""
        maxDate = df_all[tjCol.history].max()
        minDate = df_all[tjCol.history].min()
        minDate = "1401/01/01"
        maxDate = "1401/09/30"
        dfData = df_all.loc[df_all[tjCol.history]>=minDate]
        dfData = dfData.loc[dfData[tjCol.history]<=maxDate]
        createAverageFile(dfData=dfData,minDate=minDate,maxDate=maxDate, phase="بهار، تابستان، پاییز")
        year ="1401/"
        for season in yearSeasons.Seasons:
            minDate=year+yearSeasons.Seasons[season][seasonCol.start]
            maxDate = year+yearSeasons.Seasons[season][seasonCol.end]
            phase = yearSeasons.Seasons[season][seasonCol.name]
            dfData = df_all.loc[df_all[tjCol.history]>=minDate]
            dfData = dfData.loc[dfData[tjCol.history]<=maxDate]
            if len(dfData):
                extPath=f"{season}-{phase}"
                try:
                    os.mkdir(extPath)
                except:
                    pass
                os.chdir(extPath)
                createAverageFile(dfData=dfData,minDate=minDate,maxDate=maxDate, phase=phase)
                os.chdir(thisPath)
                """
invoiceAverageCount()


