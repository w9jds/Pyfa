# ammoInfluenceRange
#
# Used by:
# Items from category: Charge (571 of 913)
effectType = "passive"


def handler(fit, container, context):
    container.multiplyItemAttr("maxRange", container.getModifiedChargeAttr("weaponRangeMultiplier"))
