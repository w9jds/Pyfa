# Used by:
# Modules from group: Rig Navigation (64 of 64)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("armorHP", module.getModifiedItemAttr("drawback"))