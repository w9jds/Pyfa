# capNeedBonusEffectLasers
#
# Used by:
# Modules named like: Energy Discharge Elutriation (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))
