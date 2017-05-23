# agilityMultiplierEffectPassive
#
# Used by:
# Modules named like: Polycarbon Engine Housing (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("agilityMultiplier"), stackingPenalties=True)
