# subsystemBonusAmarrOffensiveEnergyWeaponCapacitorNeed
#
# Used by:
# Subsystem: Legion Offensive - Covert Reconfiguration
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "capacitorNeed", container.getModifiedItemAttr("subsystemBonusAmarrOffensive"),
                                  skill="Amarr Offensive Systems")
