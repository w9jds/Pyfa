# modeArmorRepDurationPostDiv
#
# Used by:
# Module: Hecate Defense Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("Repair Systems"),
            "duration",
            1 / container.getModifiedItemAttr("modeArmorRepDurationPostDiv")
    )
