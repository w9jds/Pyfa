# drawbackRepairSystemsPGNeed
#
# Used by:
# Modules named like: Auxiliary Nano Pump (6 of 8)
# Modules named like: Nanobot Accelerator (6 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "power", container.getModifiedItemAttr("drawback"))
