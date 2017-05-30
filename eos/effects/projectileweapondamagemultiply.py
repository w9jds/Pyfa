# projectileWeaponDamageMultiply
#
# Used by:
# Modules from group: Gyrostabilizer (13 of 13)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Projectile Weapon",
                                     "damageMultiplier", container.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties=True)
