# baseSensorStrengthModifierModule
#
# Used by:
# Variations of module: Scan Rangefinding Array I (2 of 2)
effectType = "passive"


def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonusModule"),
                                    stackingPenalties=True)
