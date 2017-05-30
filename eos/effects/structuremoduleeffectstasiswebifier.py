# Not used by any item
effectType = "active", "projected"


def handler(fit, container, context, *args, **kwargs):
    if "projected" not in context:
        return
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("speedFactor"),
                           stackingPenalties=True, *args, **kwargs)
