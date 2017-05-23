# modeMWDandABBoostPostDiv
#
# Used by:
# Module: Confessor Propulsion Mode
# Module: Svipul Propulsion Mode
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("High Speed Maneuvering") or mod.item.requiresSkill("Afterburner"),
            "speedFactor",
            1 / module.getModifiedItemAttr("modeVelocityPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
