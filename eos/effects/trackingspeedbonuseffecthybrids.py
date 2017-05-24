# trackingSpeedBonusEffectHybrids
#
# Used by:
# Modules named like: Hybrid Metastasis Adjuster (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Hybrid Weapon",
                                  "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus"),
                                  stackingPenalties=True)
