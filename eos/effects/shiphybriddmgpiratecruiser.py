# shipHybridDmgPirateCruiser
#
# Used by:
# Ship: Gnosis
# Ship: Vigilant
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusRole7"))
