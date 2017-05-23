# entosisCPUAddition
#
# Used by:
# Modules from group: Entosis Link (6 of 6)
effectType = "passive"


def handler(fit, module, context):
    module.increaseItemAttr("cpu", module.getModifiedItemAttr("entosisCPUAdd"))
