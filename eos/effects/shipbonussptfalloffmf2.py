# shipBonusSPTFalloffMF2
#
# Used by:
# Ship: Pacifier
# Ship: Rifter
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "falloff", ship.getModifiedItemAttr("shipBonusMF2"), skill="Minmatar Frigate")
