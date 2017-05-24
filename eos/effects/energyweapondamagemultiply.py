# energyWeaponDamageMultiply
#
# Used by:
# Modules from group: Heat Sink (18 of 18)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Energy Weapon",
                                     "damageMultiplier", container.getModifiedItemAttr("damageMultiplier"),
                                     stackingPenalties=True)
