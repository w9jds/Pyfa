# massAddPassive
#
# Used by:
# Items from category: Subsystem (80 of 80)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("mass", container.getModifiedItemAttr("mass") or 0)
