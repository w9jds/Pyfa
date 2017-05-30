# remoteWebifierFalloff
#
# Used by:
# Modules from group: Stasis Grappler (7 of 7)
# Modules from group: Stasis Web (18 of 18)
effectType = "active", "projected"


def handler(fit, container, context, *args, **kwargs):
    if "projected" not in context:
        return
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("speedFactor"),
                           stackingPenalties=True, *args, **kwargs)
