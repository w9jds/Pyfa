# crystalMiningamountInfo2
#
# Used by:
# Modules from group: Frequency Mining Laser (3 of 3)
effectType = "passive"


def handler(fit, container, context):
    container.preAssignItemAttr("specialtyMiningAmount", container.getModifiedItemAttr("miningAmount"))
