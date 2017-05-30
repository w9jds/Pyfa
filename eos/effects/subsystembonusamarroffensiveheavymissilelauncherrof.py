# subsystemBonusAmarrOffensiveHeavyMissileLauncherROF
#
# Used by:
# Subsystem: Legion Offensive - Assault Optimization
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy",
                                  "speed", container.getModifiedItemAttr("subsystemBonusAmarrOffensive"),
                                  skill="Amarr Offensive Systems")
