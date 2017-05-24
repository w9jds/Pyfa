# velocityBonusOnline
#
# Used by:
# Modules from group: Entosis Link (6 of 6)
# Modules from group: Nanofiber Internal Structure (7 of 7)
# Modules from group: Overdrive Injector System (7 of 7)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("implantBonusVelocity"),
                           stackingPenalties=True)
