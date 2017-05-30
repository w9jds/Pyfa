# modeMWDBoostPostDiv
#
# Used by:
# Module: Hecate Propulsion Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
            "speedFactor",
            1 / container.getModifiedItemAttr("modeMWDVelocityPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
