# cynosuralGeneration
#
# Used by:
# Modules from group: Cynosural Field (2 of 2)
effectType = "active"


def handler(fit, container, context):
    fit.ship.boostItemAttr("maxVelocity", container.getModifiedItemAttr("speedFactor"))
