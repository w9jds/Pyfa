# subsystemBonusOffensiveJumpHarmonics
#
# Used by:
# Subsystems named like: Offensive Covert Reconfiguration (4 of 4)
effectType = "passive"


def handler(fit, module, context):
    fit.ship.forceItemAttr("jumpHarmonics", module.getModifiedItemAttr("jumpHarmonicsModifier"))
