# CovertCloakCPUAddition
#
# Used by:
# Modules named like: Covert Ops Cloaking Device II (2 of 2)
# Module: Covert Cynosural Field Generator I
effectType = "passive"


def handler(fit, container, context):
    container.increaseItemAttr("cpu", container.getModifiedItemAttr("covertCloakCPUAdd") or 0)
