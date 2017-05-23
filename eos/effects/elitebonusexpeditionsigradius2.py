# eliteBonusExpeditionSigRadius2
#
# Used by:
# Ship: Prospect
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("signatureRadius", ship.getModifiedItemAttr("eliteBonusExpedition2"),
                           skill="Expedition Frigates")
