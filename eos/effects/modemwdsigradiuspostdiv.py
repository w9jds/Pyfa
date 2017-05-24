# modeMWDSigRadiusPostDiv
#
# Used by:
# Module: Svipul Defense Mode
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(
            lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
            "signatureRadiusBonus",
            1 / container.getModifiedItemAttr("modeMWDSigPenaltyPostDiv"),
            stackingPenalties=True,
            penaltyGroup="postDiv"
    )
