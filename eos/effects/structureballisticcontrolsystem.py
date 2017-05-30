# Not used by any item
effectType = "passive"


def handler(fit, container, context):
    missileGroups = ("Structure Anti-Capital Missile", "Structure Anti-Subcapital Missile")

    for dmgType in ("em", "kinetic", "explosive", "thermal"):
        fit.modules.filteredChargeMultiply(lambda mod: mod.charge.group.name in missileGroups,
                                           "%sDamage" % dmgType,
                                           container.getModifiedItemAttr("missileDamageMultiplierBonus"),
                                           stackingPenalties=True)

    launcherGroups = ("Structure AXL Missile Launcher", "Structure ASML Missile Launcher")
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name in launcherGroups,
                                     "speed", container.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties=True)
