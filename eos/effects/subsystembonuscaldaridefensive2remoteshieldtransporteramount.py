# subsystemBonusCaldariDefensive2RemoteShieldTransporterAmount
#
# Used by:
# Subsystem: Tengu Defensive - Adaptive Shielding
effectType = "passive"
runTime = "early"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Emission Systems"),
                                  "shieldBonus", container.getModifiedItemAttr("subsystemBonusCaldariDefensive2"),
                                  skill="Caldari Defensive Systems")
