# subsystemBonusGallenteOffensive3DroneDamageMultiplier
#
# Used by:
# Subsystem: Proteus Offensive - Drone Synthesis Projector
effectType = "passive"


def handler(fit, container, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "damageMultiplier", container.getModifiedItemAttr("subsystemBonusGallenteOffensive3"),
                                 skill="Gallente Offensive Systems")
