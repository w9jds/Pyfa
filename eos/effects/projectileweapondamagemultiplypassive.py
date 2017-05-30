# projectileWeaponDamageMultiplyPassive
#
# Used by:
# Modules named like: Projectile Collision Accelerator (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projectile Weapon",
                                     "damageMultiplier", container.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties=True)
