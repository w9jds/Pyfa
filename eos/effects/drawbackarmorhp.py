# drawbackArmorHP
#
# Used by:
# Modules from group: Rig Navigation (48 of 64)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("armorHP", container.getModifiedItemAttr("drawback"))
