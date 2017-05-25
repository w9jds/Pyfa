# modeMWDCapPostDiv
#
# Used by:
# Module: Hecate Propulsion Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
            "capacitorNeed",
            1 / container.getModifiedItemAttr("modeMWDCapPostDiv")
    )
