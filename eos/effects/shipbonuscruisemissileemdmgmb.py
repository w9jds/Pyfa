# shipBonusCruiseMissileEMDmgMB
#
# Used by:
# Ship: Typhoon Fleet Issue
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Cruise Missiles"),
                                    "emDamage", ship.getModifiedItemAttr("shipBonusMB"), skill="Minmatar Battleship")
