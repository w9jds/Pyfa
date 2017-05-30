# drawbackCPUOutput
#
# Used by:
# Modules from group: Rig Drones (58 of 64)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("cpuOutput", container.getModifiedItemAttr("drawback"))
