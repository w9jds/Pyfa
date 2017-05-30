# maxRangeBonusEffectProjectiles
#
# Used by:
# Modules named like: Projectile Locus Coordinator (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "maxRange", container.getModifiedItemAttr("maxRangeBonus"),
                                  stackingPenalties=True)
