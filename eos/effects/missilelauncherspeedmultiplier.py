# missileLauncherSpeedMultiplier
#
# Used by:
# Modules from group: Ballistic Control system (17 of 17)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                     "speed", container.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties=True)
