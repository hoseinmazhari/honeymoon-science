import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *

def _createFile(dfData,phase,color,season,func,Quality,colName):
        # selectedOption ="001"
        df_ans = dfData.copy()
        tjIndex = getIndexTj(dfData)
        sum_of_all = int(dfData[colName].sum())
        
        # try:
        fileName = (f"{season}- {phase} {func}")
        # fileName += f" از {minDate.replace('/','-')} تا {maxDate.replace('/','-')}"
        df_ans = df_ans.sort_values(by=colName)
        df_ans.to_excel(f"{fileName}.xlsx" , index = False) 


        from codes.charts import horizontalBarPlot as hbp
        Datas = []
        AxisLabels = []
        
        for i in range(len(df_ans)):
            AxisLabels.append(df_ans.iloc[i,0])
            Datas.append(int(df_ans.iloc[i,1])) # type: ignore
            
                
        titleBar= _make_farsi_text(func)
        
        # titleDetailChart = _make_farsi_text("تعداد فاکتور های هر شعبه")
        titleDetailChart = _make_farsi_text(f" از مجموع {sum_of_all:,} {Quality}، بازه({phase})" )+ titleBar # type: ignore
        # titleSource = _make_farsi_text("طراحی شده: توسط مجموعه عطر هانی مون")
        
        # color = PINK
        # des =_make_farsi_text(f"تاریخ گزارش: {getDateJalali()}")
        hbp.showHorizontalPlot(Datas,AxisLabels, titleBar, titleDetailChart, titleSource, Quality, fileName, color,des)




def factorsCount() :

        selectedOption="1"
        
        while len(selectedOption)<5:
            selectedOption = "0" + selectedOption
        # شروع برنامه
        func = "تعداد فاکتورهای مجموعه هانی مون، 1397 تا 1402"
        selectedOption += "- 1"
        folderName = f"{selectedOption}- {func}"
        
        print(" ")
        print(_make_farsi_text("انتخاب شما"))
        print(_make_farsi_text(folderName))
        ftype= myDataType_names.cumulativeSales
        df_all = loadData(ftype,folderName)
        df_all=df_all[[tjCol.history]]
        # thisPath= os.getcwd()

            
        years= [1397,1398,1399,1400,1401,1402]
        
        colors = [VIVA,GREEN,PINK,YELLOW,BLUE,color1401]
        colorIndex = -1
        
        for season in yearSeasons.Seasons:
            
            phase = yearSeasons.Seasons[season][seasonCol.name]
            df_ans = pd.DataFrame()
            colorIndex += 1
            color = colors[colorIndex]
            for year in years:
                # os.chdir(thisPath)
                # try:
                #     os.mkdir(f"{year}")
                #     os.chdir(f"{thisPath}/{year}")
                # except:
                #     os.chdir(f"{thisPath}/{year}")
                # yearQuantityDetail.__init__(yearQuantityDetail) # type: ignore
                minDate=f"{year}/{yearSeasons.Seasons[season][seasonCol.start]}"
                maxDate = f"{year}/{yearSeasons.Seasons[season][seasonCol.end]}"
                if season == "04" or season == "00":
                    if year%4==3:
                        maxDate= f"{year}/12/30"
                
                
                dfData = df_all.loc[df_all[tjCol.history]>=minDate]
                dfData = dfData.loc[dfData[tjCol.history]<=maxDate]

                # اگر در این قسمت پوشه مربوط به هر فصل و سال را بسازیم نیازی به جدا کردن شعب نیست

                if len(dfData):
                    df_ans = df_ans.append({"بازه":f"{phase} {year}",tjCol.count:len(dfData)},ignore_index=True) # type: ignore
                
            if len(df_ans):
                colName = tjCol.count
                Quality ="فاکتور"
                # df_ans.to_excel(f"test{colorIndex}.xlsx",index=False)
                _createFile(dfData=df_ans,color=color,season=season,phase=phase,func = func, colName=colName,Quality=Quality)





        # dfData = df_all.copy()
        # year = dfData.iloc[0,tjIndex.history][:4]
        # dateStart = yearSelector.years[year]["start"]
        # dateEnd = yearSelector.years[year]["end"]
        # dfYear= dfData.loc[dfData[tjCol.history]>=dateStart]
        # dfYear = dfYear.loc[dfYear[tjCol.history]<=dateEnd]

        # dfData = dfYear.copy


        
        
        # maxDate = df_all[tjCol.history].max()
        # minDate = df_all[tjCol.history].min()
        """
        minDate = "1401/01/01"
        maxDate = "1401/09/30"
        dfData = df_all.loc[df_all[tjCol.history]>=minDate]
        dfData = dfData.loc[dfData[tjCol.history]<=maxDate]
        _createFile(dfData=dfData,minDate=minDate,maxDate=maxDate, phase="بهار، تابستان، پاییز")
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
                _createFile(dfData=dfData,minDate=minDate,maxDate=maxDate, phase=phase)
                os.chdir(thisPath)
           """
         
factorsCount()


