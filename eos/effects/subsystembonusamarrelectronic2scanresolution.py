# subsystemBonusAmarrElectronic2ScanResolution
#
# Used by:
# Subsystem: Legion Electronics - Tactical Targeting Network
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("scanResolution", container.getModifiedItemAttr("subsystemBonusAmarrElectronic2"),
                           skill="Amarr Electronic Systems")
