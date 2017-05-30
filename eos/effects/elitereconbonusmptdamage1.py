# eliteReconBonusMPTdamage1
#
# Used by:
# Ship: Huginn
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("eliteBonusReconShip1"),
                                  skill="Recon Ships")
