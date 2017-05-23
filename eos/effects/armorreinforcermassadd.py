# armorReinforcerMassAdd
#
# Used by:
# Modules from group: Armor Reinforcer (48 of 48)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("mass", module.getModifiedItemAttr("massAddition"))
