

# bad algorithm
def Ichimoku_conversionline(list1, period1):
    PeriodList = list1[(period1 * -1):]
    Ichi = (max(PeriodList) + min(PeriodList)) / 2
    return Ichi