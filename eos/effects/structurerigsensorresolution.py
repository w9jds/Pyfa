# Not used by any item
effectType = "passive"


def handler(fit, src, context):
    fit.ship.boostItemAttr("scanResolution", src.getModifiedItemAttr("structureRigScanResBonus"),
                           stackingPenalties=True)
