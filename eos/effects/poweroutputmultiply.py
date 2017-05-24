# powerOutputMultiply
#
# Used by:
# Modules from group: Capacitor Flux Coil (6 of 6)
# Modules from group: Capacitor Power Relay (20 of 20)
# Modules from group: Power Diagnostic System (23 of 23)
# Modules from group: Reactor Control Unit (22 of 22)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("powerOutput", container.getModifiedItemAttr("powerOutputMultiplier"))
