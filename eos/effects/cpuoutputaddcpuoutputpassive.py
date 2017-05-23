# cpuOutputAddCpuOutputPassive
#
# Used by:
# Items from category: Subsystem (40 of 80)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("cpuOutput", module.getModifiedItemAttr("cpuOutput"))
