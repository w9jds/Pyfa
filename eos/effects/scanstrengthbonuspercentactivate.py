# Not used by any item
effectType = "active"


def handler(fit, module, context):
    for scanType in ("Gravimetric", "Magnetometric", "Radar", "Ladar"):
        fit.ship.boostItemAttr(
                "scan{}Strength".format(scanType),
                module.getModifiedItemAttr("scan{}StrengthPercent".format(scanType)),
                stackingPenalties=True
        )
