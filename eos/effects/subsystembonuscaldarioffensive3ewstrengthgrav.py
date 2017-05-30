# subsystemBonusCaldariOffensive3EwStrengthGrav
#
# Used by:
# Subsystem: Tengu Offensive - Rifling Launcher Pattern
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanGravimetricStrengthBonus",
                                  container.getModifiedItemAttr("subsystemBonusCaldariOffensive3"),
                                  skill="Caldari Offensive Systems")
