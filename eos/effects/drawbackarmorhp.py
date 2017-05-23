# drawbackArmorHP
#
# Used by:
# Modules from group: Rig Navigation (48 of 64)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("drawback"))
