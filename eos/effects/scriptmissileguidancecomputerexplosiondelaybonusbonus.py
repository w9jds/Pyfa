# scriptMissileGuidanceComputerExplosionDelayBonusBonus
#
# Used by:
# Charges named like: Missile Script (4 of 4)
effectType = "passive"


def handler(fit, module, context):
    module.boostItemAttr("explosionDelayBonus", module.getModifiedChargeAttr("explosionDelayBonusBonus"))
