# entosisLink
#
# Used by:
# Modules from group: Entosis Link (6 of 6)
effectType = "active"


def handler(fit, container, context):
    fit.ship.forceItemAttr("disallowAssistance", container.getModifiedItemAttr("disallowAssistance"))
