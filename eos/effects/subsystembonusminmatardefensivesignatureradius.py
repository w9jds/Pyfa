# subsystemBonusMinmatarDefensiveSignatureRadius
#
# Used by:
# Subsystem: Loki Defensive - Amplification Node
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("signatureRadius", container.getModifiedItemAttr("subsystemBonusMinmatarDefensive"),
                           skill="Minmatar Defensive Systems")
