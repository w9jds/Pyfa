# Not used by any item
effectType = "projected", "active"


def handler(fit, src, context):
    if "projected" in context:
        amount = src.getModifiedItemAttr("powerTransferAmount")
        duration = src.cycleTime
        fit.addDrain(src, duration, -amount, 0)
