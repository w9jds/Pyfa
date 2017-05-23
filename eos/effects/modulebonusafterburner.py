# moduleBonusAfterburner
#
# Used by:
# Modules from group: Propulsion Module (62 of 127)
effectType = "active"
runTime = "late"


def handler(fit, module, context):
    fit.ship.increaseItemAttr("mass", module.getModifiedItemAttr("massAddition"))
    speedBoost = module.getModifiedItemAttr("speedFactor")
    mass = fit.ship.getModifiedItemAttr("mass")
    thrust = module.getModifiedItemAttr("speedBoostFactor")
    fit.ship.boostItemAttr("maxVelocity", speedBoost * thrust / mass)
