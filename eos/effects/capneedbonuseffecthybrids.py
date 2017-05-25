# capNeedBonusEffectHybrids
#
# Used by:
# Modules named like: Hybrid Discharge Elutriation (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus"))
