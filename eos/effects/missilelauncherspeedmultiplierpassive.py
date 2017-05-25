# missileLauncherSpeedMultiplierPassive
#
# Used by:
# Modules named like: Bay Loading Accelerator (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                     "speed", container.getModifiedItemAttr("speedMultiplier"),
                                     stackingPenalties=True)
