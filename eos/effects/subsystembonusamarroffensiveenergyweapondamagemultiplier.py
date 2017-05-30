# subsystemBonusAmarrOffensiveEnergyWeaponDamageMultiplier
#
# Used by:
# Subsystem: Legion Offensive - Liquid Crystal Magnifiers
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("subsystemBonusAmarrOffensive"),
                                  skill="Amarr Offensive Systems")
