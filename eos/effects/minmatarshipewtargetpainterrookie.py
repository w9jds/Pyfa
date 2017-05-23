# minmatarShipEwTargetPainterRookie
#
# Used by:
# Ship: Reaper
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Target Painter",
                                  "signatureRadiusBonus", ship.getModifiedItemAttr("rookieTargetPainterStrengthBonus"))
