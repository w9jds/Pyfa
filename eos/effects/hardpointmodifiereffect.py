# hardPointModifierEffect
#
# Used by:
# Subsystems from group: Engineering Systems (16 of 16)
# Subsystems from group: Offensive Systems (16 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("turretSlotsLeft", container.getModifiedItemAttr("turretHardPointModifier"))
    fit.ship.increaseItemAttr("launcherSlotsLeft", container.getModifiedItemAttr("launcherHardPointModifier"))
