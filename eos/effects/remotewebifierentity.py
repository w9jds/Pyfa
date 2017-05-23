# remoteWebifierEntity
#
# Used by:
# Drones from group: Stasis Webifying Drone (3 of 3)
effectType = "active", "projected"


def handler(fit, module, context, *args, **kwargs):
    if "projected" not in context:
        return
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"),
                           stackingPenalties=True, *args, **kwargs)
