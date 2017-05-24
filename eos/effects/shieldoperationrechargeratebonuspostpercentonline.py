# shieldOperationRechargeratebonusPostPercentOnline
#
# Used by:
# Modules from group: Shield Power Relay (6 of 6)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.boostItemAttr("shieldRechargeRate", container.getModifiedItemAttr("rechargeratebonus") or 0)
