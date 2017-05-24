# electronicAttributeModifyOnline
#
# Used by:
# Modules from group: Automated Targeting System (6 of 6)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("maxLockedTargets", container.getModifiedItemAttr("maxLockedTargetsBonus"))
