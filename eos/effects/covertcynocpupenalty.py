# covertCynoCpuPenalty
#
# Used by:
# Subsystems from group: Offensive Systems (12 of 16)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Cynosural Field Theory"),
                                     "covertCloakCPUAdd", container.getModifiedItemAttr("covertCloakCPUPenalty"))
