# subsystemBonusMinmatarOffensiveHeavyAssaultMissileLauncherROF
#
# Used by:
# Subsystem: Loki Offensive - Hardpoint Efficiency Configuration
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy Assault",
                                  "speed", container.getModifiedItemAttr("subsystemBonusMinmatarOffensive"),
                                  skill="Minmatar Offensive Systems")
