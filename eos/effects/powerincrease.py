# powerIncrease
#
# Used by:
# Modules from group: Auxiliary Power Core (5 of 5)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("powerOutput", container.getModifiedItemAttr("powerIncrease"))
