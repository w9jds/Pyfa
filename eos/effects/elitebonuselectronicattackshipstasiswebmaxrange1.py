# eliteBonusElectronicAttackShipStasisWebMaxRange1
#
# Used by:
# Ship: Hyena
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Stasis Web",
                                  "maxRange", ship.getModifiedItemAttr("eliteBonusElectronicAttackShip1"),
                                  skill="Electronic Attack Ships")
