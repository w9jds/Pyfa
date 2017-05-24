# overloadSelfEmHardeningBonus
#
# Used by:
# Variations of module: Armor EM Hardener I (39 of 39)
# Variations of module: EM Ward Field I (19 of 19)
# Module: Civilian EM Ward Field
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("emDamageResistanceBonus", container.getModifiedItemAttr("overloadHardeningBonus"))
