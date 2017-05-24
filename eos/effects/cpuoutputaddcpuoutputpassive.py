# cpuOutputAddCpuOutputPassive
#
# Used by:
# Items from category: Subsystem (40 of 80)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("cpuOutput", container.getModifiedItemAttr("cpuOutput"))
