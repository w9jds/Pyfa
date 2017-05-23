# shipBonusRemoteTrackingComputerFalloffMC
#
# Used by:
# Ship: Scimitar
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Tracking Computer",
                                  "falloffEffectiveness", ship.getModifiedItemAttr("shipBonusMC"),
                                  skill="Minmatar Cruiser")
