# subsystemBonusCaldariOffensiveAssaultMissileLauncherROF
#
# Used by:
# Variations of subsystem: Tengu Offensive - Accelerated Ejection Bay (3 of 4)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Missile Launcher Rapid Light",
                                  "speed", container.getModifiedItemAttr("subsystemBonusCaldariOffensive"),
                                  skill="Caldari Offensive Systems")
