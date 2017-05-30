# ecmGravimetricStrengthBonusPercent
#
# Used by:
# Modules from group: ECM Stabilizer (6 of 6)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanGravimetricStrengthBonus", container.getModifiedItemAttr("ecmStrengthBonusPercent"),
                                  stackingPenalties=True)
