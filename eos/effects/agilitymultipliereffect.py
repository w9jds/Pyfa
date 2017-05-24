# agilityMultiplierEffect
#
# Used by:
# Modules from group: Inertial Stabilizer (7 of 7)
# Modules from group: Nanofiber Internal Structure (7 of 7)
# Modules from group: Reinforced Bulkhead (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("agility",
                           container.getModifiedItemAttr("agilityMultiplier"),
                           stackingPenalties=True)
