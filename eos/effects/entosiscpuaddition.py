# entosisCPUAddition
#
# Used by:
# Modules from group: Entosis Link (6 of 6)
effectType = "passive"


def handler(fit, container, context):
    container.increaseItemAttr("cpu", container.getModifiedItemAttr("entosisCPUAdd"))
