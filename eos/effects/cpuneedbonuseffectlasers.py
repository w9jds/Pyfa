# cpuNeedBonusEffectLasers
#
# Used by:
# Modules named like: Algid Energy Administrations Unit (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus"))
