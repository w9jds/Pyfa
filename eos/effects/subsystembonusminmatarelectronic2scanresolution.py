# subsystemBonusMinmatarElectronic2ScanResolution
#
# Used by:
# Subsystem: Loki Electronics - Tactical Targeting Network
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("subsystemBonusMinmatarElectronic2"),
                           skill="Minmatar Electronic Systems")
