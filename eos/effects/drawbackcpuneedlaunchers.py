# drawbackCPUNeedLaunchers
#
# Used by:
# Modules from group: Rig Launcher (48 of 48)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Missile Launcher Operation"),
                                  "cpu", container.getModifiedItemAttr("drawback"))
