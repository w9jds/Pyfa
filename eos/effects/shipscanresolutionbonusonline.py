# shipScanResolutionBonusOnline
#
# Used by:
# Modules from group: Signal Amplifier (7 of 7)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties=True)
