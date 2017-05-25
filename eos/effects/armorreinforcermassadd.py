# armorReinforcerMassAdd
#
# Used by:
# Modules from group: Armor Reinforcer (48 of 48)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("mass", container.getModifiedItemAttr("massAddition"))
