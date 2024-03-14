class tjCol():
    name = "نام"  
    count = "تعداد"
    average = "میانگین"  
    Received = "دریافتی"
    saleTime = "زمان فروش"  
    branch="عنوان شرکت"
    idBranch = "کد شرکت"
    gender="جنسیت"
    mobile="موبایل"
    transitional= "انتقالی"
    Deposit = "واریزی"
    tasvieBaMarjooe="تسویه با مرجوعي"
    earnest="پیش دریافت"
    Cash = "نقدی"
    chargeUse = "مصرف شارژ"
    saleAgentCharge = "شارژ عامل"
    charge = "مبلغ شارژ"
    saler = "فروشنده"
    saleAget = "عامل فروش"
    Registrar="ثبت کننده"
    Registrar_id = "کدثبت کننده"
    buyer="خريدار"
    PurchaseAmount = "ارزیابی"
    PurchaseAmountLbl = "مبلغ خرید"
    Remaining= "مانده پرداختي"
    mablagh= "جمع کل"
    Discount = "تخفيف"
    TotalOne = "جمع واحد"
    quantity = "مقدار"
    history = "تاريخ"
    saleId = "شماره"
    work = "شغل"
    education = "تحصیلات"
    

def getIndexTj(df):
    tjIndex = tjCol()
    
    thisIndex=-1
    for col in df.columns:        
        thisIndex+=1
        if tjIndex.name == col:
            tjIndex.name = thisIndex # type: ignore 
        elif tjIndex.count == col:
            tjIndex.count = thisIndex # type: ignore 
        elif tjIndex.average == col:
            tjIndex.average = thisIndex # type: ignore 
        elif tjIndex.branch == col:
            tjIndex.branch = thisIndex # type: ignore 
        elif tjIndex.idBranch == col:
            tjIndex.idBranch = thisIndex # type: ignore 
        elif tjIndex.gender == col:
            tjIndex.gender = thisIndex # type: ignore 
        elif tjIndex.mobile == col:
            tjIndex.mobile = thisIndex # type: ignore 
        elif tjIndex.transitional==col:
            tjIndex.transitional = thisIndex # type: ignore 
        elif tjIndex.Deposit==col:
            tjIndex.Deposit = thisIndex # type: ignore 
        elif tjIndex.tasvieBaMarjooe==col:
            tjIndex.tasvieBaMarjooe = thisIndex # type: ignore 
        elif tjIndex.earnest==col:
            tjIndex.earnest = thisIndex # type: ignore 
        elif tjIndex.Cash==col:
            tjIndex.Cash = thisIndex # type: ignore 
        elif tjIndex.chargeUse==col:
            tjIndex.chargeUse = thisIndex # type: ignore 
        elif tjIndex.saleAgentCharge==col:
            tjIndex.saleAgentCharge = thisIndex # type: ignore 
        elif tjIndex.charge==col:
            tjIndex.charge = thisIndex # type: ignore 
        elif tjIndex.saler==col:
            tjIndex.saler = thisIndex # type: ignore 
        elif tjIndex.saleAget==col:
            tjIndex.saleAget = thisIndex # type: ignore 
        elif tjIndex.Registrar==col:
            tjIndex.Registrar = thisIndex # type: ignore 
        elif tjIndex.Registrar_id == col: # type: ignore
            tjIndex.Registrar_id = thisIndex # type: ignore
        elif tjIndex.buyer==col:
            tjIndex.buyer = thisIndex # type: ignore 
        elif tjIndex.PurchaseAmount==col:
            tjIndex.PurchaseAmount = thisIndex # type: ignore 
        elif tjIndex.PurchaseAmountLbl==col:
            tjIndex.PurchaseAmountLbl = thisIndex # type: ignore 
        elif tjIndex.Remaining==col:
            tjIndex.Remaining = thisIndex # type: ignore 
        elif tjIndex.mablagh==col:
            tjIndex.mablagh = thisIndex # type: ignore 
        elif tjIndex.Discount==col:
            tjIndex.Discount = thisIndex # type: ignore  # type: ignore 
        elif tjIndex.TotalOne==col:
            tjIndex.TotalOne = thisIndex # type: ignore 
        elif tjIndex.quantity==col:
            tjIndex.quantity = thisIndex # type: ignore 
        elif tjIndex.history==col:
            tjIndex.history = thisIndex # type: ignore 
        elif tjIndex.saleId==col:
            tjIndex.saleId = thisIndex # type: ignore 
        elif tjIndex.saleTime == col:
            tjIndex.saleTime = thisIndex # type: ignore 
        elif tjIndex.Received == col:
            tjIndex.Received = thisIndex# type: ignore 
        elif tjIndex.work == col:
            tjIndex.work = thisIndex #type: ignore
        elif tjIndex.education == col:
            tjIndex.education = thisIndex # type: ignore
    return tjIndex
