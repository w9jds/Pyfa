# overloadSelfThermalHardeningBonus
#
# Used by:
# Variations of module: Armor Thermal Hardener I (39 of 39)
# Variations of module: Thermal Dissipation Field I (19 of 19)
# Module: Civilian Thermal Dissipation Field
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("thermalDamageResistanceBonus", container.getModifiedItemAttr("overloadHardeningBonus"))
