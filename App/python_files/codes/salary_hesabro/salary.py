
import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from main import _make_farsi_text
from main import * 
import codes.merger.defs.cols_selector  as csr
from codes.salary_new.defs import RegistrarChecker as RgsChk
from codes.salary_new.defs import make_registrar_sale_file as mrsf
# from codes.structures.ReturnMerchandise import EmployeMissSaleCol as EMSC
# from codes.structures.ReturnMerchandise import EmployeMissSaleIndex as EMSI
# from codes.returned.returnedSaleItemsNish import EMSC
# from codes.returned.returnedSaleItems import EMSI



# class mergeMissSaleOnBrCol(): 
#     Registrar=EMSC.saleRegistrarLbl
#     branch = EMSC.branch
#     exclusive_totalOne = "مجموع نیش انحصاری مرجوع شده"
#     exclusive_Discount= EMSC.exclusiveDiscount
#     exclusive_returnUsedCharge=EMSC.exclusive_returnUsedCharge
#     exclusive_returned=" مجموع نیش انحصاری بعد از کسر تخفیف و شارژمصرفی"

#     nonExclusive_totalOne = "مجموع نیش تجاری مرجوع شده"
#     nonExclusive_Discount= EMSC.nonExclusive_Discount
#     nonExclusive_returnUsedCharge=EMSC.nonExclusive_returnUsedCharge
#     nonExclusive_returned=" مجموع نیش تجاری بعد از کسر تخفیف و شارژمصرفی"
#     shiftWork = condition.shiftWork

# def getIndexMergeMissSaleOnBr(df):
#     thisClass = mergeMissSaleOnBrCol()
#     thisIndex = -1
#     for col in df.columns:
#         thisIndex += 1
#         if col == thisClass.Registrar:
#             thisClass.Registrar = thisIndex # type: ignore
#         elif col == thisClass.branch:
#             thisClass.branch = thisIndex # type: ignore
#         elif col == thisClass.exclusive_totalOne:
#             thisClass.exclusive_totalOne= thisIndex # type: ignore
#         elif col == thisClass.exclusive_Discount:
#             thisClass.exclusive_Discount = thisIndex # type: ignore
#         elif col == thisClass.exclusive_returnUsedCharge:
#             thisClass.exclusive_returnUsedCharge = thisIndex # type: ignore
#         elif col == thisClass.exclusive_returned:
#             thisClass.exclusive_returned = thisIndex # type: ignore
#         elif col == thisClass.nonExclusive_totalOne:
#             thisClass.nonExclusive_totalOne = thisIndex # type: ignore
#         elif col == thisClass.nonExclusive_Discount:
#             thisClass.nonExclusive_Discount = thisIndex # type: ignore
#         elif col == thisClass.nonExclusive_returnUsedCharge:
#             thisClass.nonExclusive_returnUsedCharge = thisIndex # type: ignore
#         elif col == thisClass.nonExclusive_returned:
#             thisClass.nonExclusive_returned = thisIndex # type: ignore
#         elif col == thisClass.shiftWork:
#             thisClass.shiftWork = thisIndex # type: ignore
#     return thisClass
    
# class mergeMissSaleOnBrIndex(): 
#     Registrar=0
#     branch = 1
#     exclusive_totalOne = 2
#     exclusive_Discount= 3
#     exclusive_returnUsedCharge=4
#     exclusive_returned=5

#     nonExclusive_totalOne = 6
#     nonExclusive_Discount= 7
#     nonExclusive_returnUsedCharge=8
#     nonExclusive_returned=9
    # shiftWork = 10
class chechOutCol():
    branch = tjCol.branch
    saleId = tjCol.saleId
    Registrar = tjCol.Registrar
    Received = tjCol.Received
    shiftWork = condition.shiftWork
    exclusiveReceived = "دریافتی نیش انحصاری"
    nonExclusiveReceived = "دریافتی نیش تجاری"
class chechOutIndex():
    branch = 0
    saleId = 1
    Registrar = 2
    Received = 3
    shiftWork = 4
    exclusiveReceived = 5
    nonExclusiveReceived = 6
# class targetIndex():
#     branch = 0
#     shiftWork = 1
#     exclusivePercent= 2
#     nonExclusivePercent = 3
# class returnedCommissionIndex():
#     Registrar=0
#     branch= 1
#     shiftWork = 2
#     exclusive_returned=3
#     exclusivePercent = 4
#     exclusive_deductible=5
#     nonExclusive_returned= 6
#     nonExclusivePercent =7
#     nonExclusive_deductible=8

class saleMergedWithTargetCol():
    branch = 0
    Registrar = 1
    Received = 2
    shiftWork = 3
    exclusivePercent= 4
    nonExclusivePercent = 5
    commission = 6


class invoicesMergeCol():
    branch=chechOutCol.branch
    # saleid= tjCol.saleId
    Registrar = chechOutCol.Registrar
    shiftWork = chechOutCol.shiftWork
    Received = chechOutCol.Received
    exclusiveReceived = chechOutCol.exclusiveReceived
    nonExclusiveReceived  = chechOutCol.nonExclusiveReceived
def getIndexInvoicesMerge(df):
    thisClass = invoicesMergeCol()
    thisIndex = -1
    for col in df.columns:
        thisIndex += 1
        if col == thisClass.branch:
            thisClass.branch = thisIndex # type: ignore
        elif col == thisClass.exclusiveReceived:
            thisClass.exclusiveReceived = thisIndex # type: ignore
        elif col == thisClass.nonExclusiveReceived:
            thisClass.nonExclusiveReceived = thisIndex # type: ignore
        elif col == thisClass.Received:
            thisClass.Received = thisIndex # type: ignore
        elif col == thisClass.Registrar:
            thisClass.Registrar = thisIndex # type: ignore
        elif col == thisClass.shiftWork:
            thisClass.shiftWork = thisIndex # type: ignore
    return thisClass

# class invoicesMergeIndex():
#     branch = 0
#    # saleId = 1
#     Registrar = 1
#     Received = 2
#     shiftWork =3
#     exclusiveReceived = 4
#     nonExclusiveReceived = 5
def getIndexConcatSaleWithTarget(df):
    thisIndex= -1
    thisClass = concatSaleWithTargetCol()
    for col in df.columns:
        thisIndex += 1
        if col == thisClass.branch:
            thisClass.branch = thisIndex # type: ignore
        elif col == thisClass.commission:
            thisClass.commission = thisIndex # type: ignore
        elif col == thisClass.commissionExclusive:
            thisClass.commissionExclusive = thisIndex # type: ignore
        elif col == thisClass.commission_nonExclusive:
            thisClass.commission_nonExclusive = thisIndex # type: ignore
        elif col == thisClass.exclusivePercent:
            thisClass.exclusivePercent = thisIndex # type: ignore
        elif col == thisClass.exclusiveReceived:
            thisClass.exclusiveReceived = thisIndex # type: ignore
        elif col == thisClass.nonExclusivePercent:
            thisClass.nonExclusivePercent = thisIndex # type: ignore
        elif col == thisClass.nonExclusiveReceived:
            thisClass.nonExclusiveReceived = thisIndex # type: ignore
        elif col == thisClass.Received:
            thisClass.Received = thisIndex # type: ignore
        elif col == thisClass.Registrar:
            thisClass.Registrar = thisIndex # type: ignore
        elif col == thisClass.shiftWork:
            thisClass.shiftWork = thisIndex # type: ignore
    return thisClass

# class concatSaleWithTargetIndex():
#     branch = 0
#     Registrar = 1
#     Received = 2
#     shiftWork = 3
#     exclusiveReceived = 4
#     nonExclusiveReceived  = 5
#     exclusivePercent= 6
#     nonExclusivePercent = 7
#     commissionExclusive = 8
#     commission_nonExclusive = 9
#     commission = 10


def calculateSaleEachSaler(dfData):
    tjIndex = getIndexTj(dfData)
    lsDatas =[]
    while len(dfData):
        Registrar_id = dfData.iat[0,tjIndex.Registrar_id]
        dfRegistrar = dfData.loc[dfData[tjCol.Registrar_id]==Registrar_id]
        Registrar = dfRegistrar.iat[0,tjIndex.Registrar]
        Cash = int(dfRegistrar[tjCol.Cash].sum())
        earnest = int(dfRegistrar[tjCol.earnest].sum())
        tasvieBaMarjooe = int(dfRegistrar[tjCol.tasvieBaMarjooe].sum())
        Deposit = int(dfRegistrar[tjCol.Deposit].sum())
        transitional = int(dfRegistrar[tjCol.transitional].sum())
        check = int(dfRegistrar[tjCol.check].sum())
        to_other_person = 0#int(dfRegistrar[tjCol.to_other_person].sum())
        Received = Cash+earnest+tasvieBaMarjooe+Deposit+transitional+check+to_other_person
        
        
        lsDatas.append({tjCol.Registrar:Registrar,tjCol.Registrar_id:Registrar_id,
                        tjCol.Received:Received
                        })
                    
        dfData = dfData.loc[dfData[tjCol.Registrar_id]!=Registrar_id]
    dfData = pd.DataFrame(lsDatas)
    dfData.to_excel("فروش تمامی مشاوران.xlsx",index=False)

def thisFileDef():
        xlsxFileNum = 0
        thisPath = os.getcwd()
        selectedOption="0"
        while len(selectedOption)<5:
            selectedOption = "0" + selectedOption

        # start coding
        folderName = f"{selectedOption}- حقوق مشاوران {getDateTimeForFileName()}"
        prtLines(2)
        print(_make_farsi_text("انتخاب شما: "))
        print(_make_farsi_text(folderName))
        print("*****************************************")
        print("*****************************************")
        print("*****************************************")
        print("*****************************************")
        prtLines(2)
        # print(_make_farsi_text("نکته "))
        # print(_make_farsi_text("در این برنامه باید 4 نوع فایل فروش، تجمیعی فروش و تارگت و مرجوعی ها انتخاب شوند"))
        print()
        print(_make_farsi_text("و همچنین باید ماه مورد نظر خود برای محاسبه حقوق را نیز انتخاب فرمایید"))
        print()
        print(_make_farsi_text("نکته: برای فایل تجمیعی فروش لطفا کل سال را انتخاب فرمایید(برای بررسی فروشنده مرجوعی)"))
        prtLines(2)
        print("*****************************************")
        print("*****************************************")
        print("*****************************************")
        print("*****************************************")
        prtLines(2)
        # بارگزاری فایل های فروش و انتخاب ستون های مورد نیاز
        # fileTypes = myDataType_names.detailedSales
        # print(_make_farsi_text( fileTypes))
        # df_detailedSales = loadData(fileTypes,folderName)
        # # df_detailedSales = df_detailedSales[[frCol.history,frCol.saleId,frCol.branch,frCol.Registrar,frCol.merchandise,frCol.quantity,frCol.idCode]]
        # df_detailedSales.to_excel("ریز فروش ها.xlsx",index=False)
        # # ,frCol.TotalOne
        # # df_detials = df_detailedSales.copy()
        # # df_detials.to_excel("df_detials.xlsx",index=False)
        # prtLines(2)
        # # برگشت به پوشه مبدا
        # os.chdir(thisPath)
        # بارگزاری فایل های تجمیعی و انتخاب ستون های مورد نیاز
        print(_make_farsi_text("از لیست،پوشه یا فایل های تجمیعی فروش را نیز انتخاب نمایید"))
        fileTypes= myDataType_names.hesabro
        # fileTypes= myDataType_names.cumulativeSales
        df_cumulativeSales = loadData(fileTypes,folderName)
        # df_cumulativeSales= df_cumulativeSales[[tjCol.history,tjCol.branch,tjCol.Registrar,tjCol.Cash,tjCol.mobile,
        
        #                                         tjCol.earnest,tjCol.Deposit,tjCol.tasvieBaMarjooe,
        #                                         tjCol.transitional,tjCol.saleId,tjCol.saleTime,tjCol.idBranch]]
        df_cumulativeSales = csr.cumulative_hesabro_cols(df_cumulativeSales)
        df_cumulativeSales.to_excel(f"فاکتورهای {fileTypes}.xlsx",index=False)
        # dfInvoices.to_excel("dfInvoices.xlsx",index=False)
        prtLines(1)
        # برگشت به پوشه مبدا
        # os.chdir(thisPath)
        prtLines(2)
        # بارگزاری فایل های مرجوعی 
        # print(_make_farsi_text("لطفا فایل ها یا پوشه مربوط به مرجوعی مورد نظر خود را انتخاب فرمایید"))
        # fileType= myDataType_names.returnedMerchandise
        
        # dfReturns=loadData(fileType,folderName)
        # dfReturns.to_excel("مرجوعی ها.xlsx",index=False)
        

        # انتخاب ماه برای محاسبه حقوق
        print(_make_farsi_text("جهت ادامه باید یکی از ماه های زیر را انتخاب فرمایید"))
         # "01":{monthCol.month:"فروردین", monthCol.Deposit:0, monthCol.Cash:0, monthCol.earnest:0, monthCol.Received:0},
        for months in yearDetail.month:
            print(f"{months}: {_make_farsi_text(yearDetail.month[months][monthCol.month])}")
        
        monthNum = input(_make_farsi_text(" :  لطفا عدد کنار ماه درخواستی را کامل وارد نمایید مثل 01 برای انتخاب فروردین"))
        # df_detailedSales.to_excel("all.xlsx",index=False)
        prtLines(2)
        year ="1402"
        startDate = f'{year}{monthsSelector.month[monthNum]["start"]}'
        endDate = f'{year}{monthsSelector.month[monthNum]["end"]}'
        endDate = "1402/12/26"
        # endDate = "1401/12/28"
        # فیلتر فایل تجمیعی فروش در تاریخ انتخابی
        dfInvoices =df_cumulativeSales.loc[df_cumulativeSales[tjCol.history]>=startDate]
        dfInvoices = dfInvoices.loc[dfInvoices[tjCol.history]<=endDate]
        Invoice_name = f"فاکتورهای ماه {monthNum}.xlsx"
        dfInvoices.to_excel(Invoice_name, index= False)
        import time
        time.sleep(1)
        dfInvoices = pd.read_excel(Invoice_name)
        # برگشت به پوشه مبدا
        os.chdir(thisPath)
        calculateSaleEachSaler(dfInvoices)
        
            
        # fileTypes = myDataType_names.nish
        # dfExclusiveBite = loadData(fileTypes,folderName)
        # dfExclusiveBite.to_excel("انحصاری ها.xlsx",index=False)
        # prtLines(2)
        # # برگشت به پوشه مبدا
        # os.chdir(thisPath)

        # انتخاب فایل تارگت ماه منتخب
        print(_make_farsi_text("لطفا فایل تارگت مربوط به درصد ها را انتخاب نمایید"))
        
        fileTypes = myDataType_names.targets
        df_targets= loadData(fileTypes,folderName)
        df_targets.to_excel("تارگت ها.xlsx",index=False)
        exportPath = os.getcwd()

        # deductionPercent = int(input(_make_farsi_text(": لطفا در صد قابل کسر بابت عدم دستیابی به تارگت را وارد نمایید -")))

        # tjIndex = getIndexTj(df_detailedSales)
        # اندیس گزاری برای ستون های فایل فروش
        # frIndex = getIndexFr(df_detailedSales)
        # year = df_detailedSales.iloc[0,tjIndex.history][:4]
        # انتخاب سال از اولین ردیف دیتای فروش
        # year = df_detailedSales.iloc[0,frIndex.history][:4] # type: ignore
        # year = input(_make_farsi_text("- لطفا سال مربوط به حقوق را وارد نمایید : "))
        # انتخاب ماه
        monthName = f'{year}{monthsSelector.month[monthNum]["name"]}'
        # تاریخ جاری برای ایجاد پوشه
        todayDate = DateJuToJa.todaydate()
        # جایگزینی / با - برای امکان استفاده از تاریخ
        todayDate = todayDate.replace("/","-")

        import datetime

        thisTime = str(datetime.datetime.now())
        thisTime = thisTime[10:]
        thisTime = thisTime[:9]
        thisTime = thisTime.replace(":","-")

        # تعین مسیر خروجی
        exportPath=f"{todayDate} {thisTime}"
        #{monthNum}-{monthName}
        try:
            # ساخت پوشه تولید خروجی و تغییر مسیر به آن
            os.mkdir(exportPath)
            os.chdir(exportPath)
        except:
            # در صورتی که پوشه خروجی وجود دارد تغییر مسیر به آن
            os.chdir(exportPath)
        prtLines(4)
        # print(_make_farsi_text("برنامه در حال اصلاح ثبت کننده های فاکتور ها می باشد لطفا منتظر بمانید"))
        # # اصلاح ثبت کننده های کالا ها در فایل فروش با استفاده از ثبت کننده فایل تجمیعی 
        # dfInvoices = RgsChk.RegistrarEditter(df_detials=df_detailedSales,dfInvoices=df_cumulativeSales)
        # df = RgsChk.test(df_cumulativeSales)
        # df.to_excel("test tj.xlsx",index=False)
        # ساخت فایل ریز دریافتی ها از فایل های انتخاب شده بدون در نظر گرفتن ماه انتخاب شده
        # df = RgsChk.test(dfInvoices)
        # df.to_excel("کل ریز دریافتی ها از ابتدای سال تا تاریخ نهایی فایل.xlsx",index=False)
        
        # بدست آوردن اولین و آخرین روز از ماه انتخاب شده
        # df = RgsChk.test(dfInvoices)
        # df.to_excel(f"ریز دریافتی های هر مشاور در {monthName}ماه.xlsx",index=False)
        # فیلتر فایل فروش در بازه ماه انتخابی
        # df_detailedSales= df_detailedSales.loc[df_detailedSales[frCol.history]>=startDate]
        # df_detailedSales= df_detailedSales.loc[df_detailedSales[frCol.history]<=endDate]

        # فیلتر فایل مرجوعی در بازه ماه انتخابی
        # dfReturns = dfReturns.loc[dfReturns[tjCol.history]>=startDate]
        # dfReturns = dfReturns.loc[dfReturns[tjCol.history]<=endDate]

        prtLines(3)
        # os.chdir(thisPath)
        
        # nonExclusiveData = pd.read_excel(mainPath+"/base Datas/012-nonExclusives for filter salers.xlsx")
        # prtLines(3)
        # myItems= []
        # Mylist = []
        # print(_make_farsi_text("برنامه در حال استخراج لیست پیور پرفیوم ها و پک ها  و جدا سازی از عطرها میباشد منتظر بمانید"))
        Counter = 0
        

        # جدا سازی رکورد های مربوط به شیفت صبح از فایل تجمیعی فروش
        dfAmInvoices = dfInvoices.loc[dfInvoices[tjCol.saleTime]<=condition.saleTime]
        # dfAmDetailedSales = df_detailedSales.loc[df_detailedSales[frCol.saleTime]<=condition.saleTime]
        
        # جدا سازی رکورد های مربوط به شیفت عصر از فایل تجمیعی فروش
        dfPmInvoices = dfInvoices.loc[dfInvoices[tjCol.saleTime]>condition.saleTime]
        # dfPmDetailedSales = df_detailedSales.loc[df_detailedSales[frCol.saleTime]>condition.saleTime]
        
        dfCheckoutAm=mrsf.makeRegistrarSaleFile(dfAmInvoices,condition.saleAm)#,df_detailedSales,dfExclusiveBite
        dfCheckoutPm=mrsf.makeRegistrarSaleFile(dfPmInvoices,condition.salePm)#,df_detailedSales,dfExclusiveBite
        dfCheckoutPm.to_excel("فروش شیفت عسر.xlsx",index=False)
        dfCheckoutAm.to_excel("فروش شیفت صبح.xlsx",index=False)
        lsCheckOut = []
        lsCheckOut.append(dfCheckoutAm)
        lsCheckOut.append(dfCheckoutPm)
        # df_ans = makeRegistrarSaleFile(df_exclusive,df_nonExclusive,df_targets,dfInvoices)
        
        dfCheckout = pd.concat(lsCheckOut)
        
        
        xlsxFileNum += 1
        thisFileName = f"فروش هر مشاور در هر شعبه و شیفت.xlsx"
        thisFileName = f"{xlsxFileNum}- {thisFileName}"
        dfCheckout.to_excel(thisFileName,index = False)
        
        # از این قسمت فقط برای تولید فایل فروش هر مشاور استفاده می شود
        from codes.salary_hesabro.this_defs import sale_each_employe
        df_emp_sale = sale_each_employe.sale_employes(dfCheckout)
        df_emp_sale.to_excel("فروش کل هر مشاور.xlsx",index=False)

        
        
        
        prtLines(4)
        print(_make_farsi_text("ادغام فروش مشاوران در هر شعبه و شیفت با تارگت همان شعبه و شیفت"))
        from codes.salary_new.defs import concat_sale_with_target as cswt
        df_ConcatWithTargets= cswt.concatWithTargets(dfCheckout,df_targets)
        xlsxFileNum += 1
        thisFileName = f"ادغام فروش با تارگت {folderName}.xlsx"
        thisFileName = f"{xlsxFileNum}- {thisFileName}"
        df_ConcatWithTargets.to_excel(thisFileName,index = False)
        

        xlsxFileNum += 1
        from codes.salary_new.defs import commission 
        df_final = commission.commission(df_ConcatWithTargets,df_targets)
        thisFileName = f"فایل نهایی برای مشاوران اصلی در {monthName} ماه.xlsx"
        thisFileName = f"{xlsxFileNum}- {thisFileName}"
        df_final.to_excel(thisFileName,index = False)


thisFileDef()

