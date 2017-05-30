# moduleBonusAfterburner
#
# Used by:
# Modules from group: Propulsion Module (62 of 127)
effectType = "active"
runTime = "late"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("mass", container.getModifiedItemAttr("massAddition"))
    speedBoost = container.getModifiedItemAttr("speedFactor")
    mass = fit.ship.getModifiedItemAttr("mass")
    thrust = container.getModifiedItemAttr("speedBoostFactor")
    fit.ship.boostItemAttr("maxVelocity", speedBoost * thrust / mass)
