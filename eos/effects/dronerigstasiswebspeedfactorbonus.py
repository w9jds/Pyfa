# droneRigStasisWebSpeedFactorBonus
#
# Used by:
# Modules named like: Stasis Drone Augmentor (8 of 8)
effectType = "passive"


def handler(fit, container, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Stasis Webifying Drone",
                                 "speedFactor", container.getModifiedItemAttr("webSpeedFactorBonus"))
