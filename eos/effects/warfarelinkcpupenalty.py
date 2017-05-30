# warfareLinkCpuPenalty
#
# Used by:
# Subsystems from group: Defensive Systems (12 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Leadership"),
                                     "warfareLinkCPUAdd", container.getModifiedItemAttr("warfareLinkCPUPenalty"))
