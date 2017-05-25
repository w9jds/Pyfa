# powerOutputAddPassive
#
# Used by:
# Items from category: Subsystem (40 of 80)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("powerOutput", container.getModifiedItemAttr("powerOutput"))
