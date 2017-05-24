# drawbackShieldCapacity
#
# Used by:
# Modules from group: Rig Electronic Systems (40 of 48)
# Modules from group: Rig Targeting (16 of 16)
# Modules named like: Signal Focusing Kit (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("shieldCapacity", container.getModifiedItemAttr("drawback"))
