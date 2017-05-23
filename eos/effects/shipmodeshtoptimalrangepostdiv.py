# shipModeSHTOptimalRangePostDiv
#
# Used by:
# Module: Hecate Sharpshooter Mode
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
            "maxRange",
            1 / module.getModifiedItemAttr("modeMaxRangePostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
