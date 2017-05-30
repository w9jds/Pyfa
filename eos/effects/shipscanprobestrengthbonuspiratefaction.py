# shipScanProbeStrengthBonusPirateFaction
#
# Used by:
# Ship: Nestor
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", ship.getModifiedItemAttr("shipBonusRole7"))
