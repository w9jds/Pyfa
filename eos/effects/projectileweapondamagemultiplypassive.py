# projectileWeaponDamageMultiplyPassive
#
# Used by:
# Modules named like: Projectile Collision Accelerator (8 of 8)
effectType = "passive"


def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projectile Weapon",
                                     "damageMultiplier", module.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties=True)
