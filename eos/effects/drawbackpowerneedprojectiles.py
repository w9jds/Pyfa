# drawbackPowerNeedProjectiles
#
# Used by:
# Modules from group: Rig Projectile Weapon (40 of 40)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Projectile Weapon",
                                  "power", container.getModifiedItemAttr("drawback"))
