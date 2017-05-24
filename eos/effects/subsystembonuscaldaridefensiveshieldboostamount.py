# subsystemBonusCaldariDefensiveShieldBoostAmount
#
# Used by:
# Subsystem: Tengu Defensive - Amplification Node
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "shieldBonus", container.getModifiedItemAttr("subsystemBonusCaldariDefensive"),
                                  skill="Caldari Defensive Systems")
