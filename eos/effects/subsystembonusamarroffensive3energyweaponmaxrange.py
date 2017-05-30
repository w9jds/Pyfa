# subsystemBonusAmarrOffensive3EnergyWeaponMaxRange
#
# Used by:
# Subsystem: Legion Offensive - Liquid Crystal Magnifiers
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "maxRange", container.getModifiedItemAttr("subsystemBonusAmarrOffensive3"),
                                  skill="Amarr Offensive Systems")
