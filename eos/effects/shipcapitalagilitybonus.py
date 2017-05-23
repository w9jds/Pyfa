# shipCapitalAgilityBonus
#
# Used by:
# Items from market group: Ships > Capital Ships (28 of 37)
effectType = "passive"


def handler(fit, src, context):
    fit.ship.multiplyItemAttr("agility", src.getModifiedItemAttr("advancedCapitalAgility"), stackingPenalties=True)
