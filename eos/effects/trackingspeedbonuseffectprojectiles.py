# trackingSpeedBonusEffectProjectiles
#
# Used by:
# Modules named like: Projectile Metastasis Adjuster (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "trackingSpeed", container.getModifiedItemAttr("trackingSpeedBonus"),
                                  stackingPenalties=True)
