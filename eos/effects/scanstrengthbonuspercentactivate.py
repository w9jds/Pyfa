# Not used by any item
effectType = "active"


def handler(fit, container, context):
    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.boostItemAttr(
                "scan{}Strength".format(scanType),
                container.getModifiedItemAttr("scan{}StrengthPercent".format(scanType)),
                stackingPenalties=True
        )
