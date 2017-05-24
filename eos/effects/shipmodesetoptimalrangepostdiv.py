# shipModeSETOptimalRangePostDiv
#
# Used by:
# Module: Confessor Sharpshooter Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("Small Energy Turret"),
            "maxRange",
            1 / container.getModifiedItemAttr("modeMaxRangePostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
