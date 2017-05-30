# shipStasisWebStrengthBonusMC2
#
# Used by:
# Ship: Vigilant
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                  "speedFactor", ship.getModifiedItemAttr("shipBonusMC2"), skill="Minmatar Cruiser")
