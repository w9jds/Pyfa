# subsystemBonusAmarrOffensive2EnergyWeaponCapacitorNeed
#
# Used by:
# Subsystem: Legion Offensive - Drone Synthesis Projector
# Subsystem: Legion Offensive - Liquid Crystal Magnifiers
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "capacitorNeed", container.getModifiedItemAttr("subsystemBonusAmarrOffensive2"),
                                  skill="Amarr Offensive Systems")
