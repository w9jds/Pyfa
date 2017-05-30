# falloffBonusEffectProjectiles
#
# Used by:
# Modules named like: Projectile Ambit Extension (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "falloff", container.getModifiedItemAttr("falloffBonus"),
                                  stackingPenalties=True)
