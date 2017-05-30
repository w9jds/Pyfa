# systemScanDurationModuleModifier
#
# Used by:
# Modules from group: Scanning Upgrade Time (2 of 2)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                  "duration", container.getModifiedItemAttr("scanDurationBonus"))
