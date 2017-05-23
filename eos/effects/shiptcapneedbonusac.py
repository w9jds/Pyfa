# shipTCapNeedBonusAC
#
# Used by:
# Ship: Devoter
# Ship: Omen
# Ship: Zealot
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "capacitorNeed", ship.getModifiedItemAttr("shipBonusAC"), skill="Amarr Cruiser")
