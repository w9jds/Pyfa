# shipStasisWebStrengthBonusMF2
#
# Used by:
# Ship: Daredevil
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                  "speedFactor", ship.getModifiedItemAttr("shipBonusMF2"), skill="Minmatar Frigate")
