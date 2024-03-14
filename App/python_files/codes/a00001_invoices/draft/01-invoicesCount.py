import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import *

def _createFile(dfData,minDate,maxDate,phase):
        selectedOption ="001"
        df_ans = pd.DataFrame()
        sum_of_all = len(dfData)
        while len(dfData):
            # try:
                branch = dfData.iloc[0,tjIndex.branch]
                # print(branch)
                dfBranchs=dfData.loc[dfData[tjCol.branch]==branch]
                msg = _make_farsi_text("تعداد فاکتور های شعبه ")
                print(f"{_make_farsi_text(branch)} {msg} = {len(dfBranchs)}")
                
                df_ans = df_ans.append({tjCol.branch:branch,tjCol.count:len(dfBranchs)},ignore_index=True)
                dfData=dfData.loc[dfData[tjCol.branch]!=branch]
                
            # except: 
            #     print("مشکلی در تعداد فاکتور های شعب یا فایل انتخاب شده مشاهده شد")
            #     break


        # try:
        fileName = (f"{selectedOption}- تعداد فاکتورهای شعب هانی مون")
        fileName += f" از {minDate.replace('/','-')} تا {maxDate.replace('/','-')}"
        df_ans = df_ans.sort_values(by=tjCol.count)
        df_ans.to_excel(f"{fileName}.xlsx" , index = False) 


        from codes.charts import horizontalBarPlot as hbp
        Datas = []
        AxisLabels = []
        
        for i in range(len(df_ans)):
            AxisLabels.append(df_ans.iloc[i,0])
            Datas.append(int(df_ans.iloc[i,1]))
            
                
        titleBar= _make_farsi_text("تعداد فاکتورهای شعب هانی مون")
        
        # titleDetailChart = _make_farsi_text("تعداد فاکتور های هر شعبه")
        titleDetailChart = _make_farsi_text(f" از مجموع {sum_of_all} فاکتور در بازه {minDate} تا {maxDate} ({phase})" )+ titleBar
        titleSource = _make_farsi_text("طراحی شده: توسط مجموعه عطر هانی مون")
        Quality ="فاکتور"
        color = PINK
        hbp.showHorizontalPlot(Datas,AxisLabels, titleBar, titleDetailChart, titleSource, Quality, fileName, color)



def factorsCount() :

        selectedOption="1"
        
        while len(selectedOption)<3:
            selectedOption = "0" + selectedOption
        # شروع برنامه
        folderName = f"{selectedOption}- استخراج تعداد فاکتور های شعب هانی مون"
        
        print(" ")
        print(_make_farsi_text("انتخاب شما"))
        print(_make_farsi_text(folderName))
        
        df_all = loadDataTj(folderName=folderName)
        
        # dfData = df_all.copy()
        # year = dfData.iloc[0,tjIndex.history][:4]
        # dateStart = yearSelector.years[year]["start"]
        # dateEnd = yearSelector.years[year]["end"]
        # dfYear= dfData.loc[dfData[tjCol.history]>=dateStart]
        # dfYear = dfYear.loc[dfYear[tjCol.history]<=dateEnd]

        # dfData = dfYear.copy


        
        
        # maxDate = df_all[tjCol.history].max()
        # minDate = df_all[tjCol.history].min()
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
                _createFile(dfData=dfData,minDate=minDate,maxDate=maxDate, phase=phase)
            
factorsCount()


