# trackingSpeedBonusEffectLasers
#
# Used by:
# Modules named like: Energy Metastasis Adjuster (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Weapon",
                                  "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus"),
                                  stackingPenalties=True)
