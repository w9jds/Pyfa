# warfareLinkCPUAddition
#
# Used by:
# Modules from group: Command Burst (10 of 10)
# Modules from group: Gang Coordinator (6 of 6)
effectType = "passive"


def handler(fit, container, context):
    container.increaseItemAttr("cpu", container.getModifiedItemAttr("warfareLinkCPUAdd") or 0)
