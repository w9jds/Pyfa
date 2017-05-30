# eliteBonusLogiFrigArmorHP2
#
# Used by:
# Ship: Deacon
effectType = "passive"


def handler(fit, src, context):
    fit.ship.boostItemAttr("armorHP", src.getModifiedItemAttr("eliteBonusLogiFrig2"), skill="Logistics Frigates")
