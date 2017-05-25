# modeHullResonancePostDiv
#
# Used by:
# Module: Hecate Defense Mode
effectType = "passive"


def handler(fit, container, context):
    for srcResType, tgtResType in (
            ("Em", "em"),
            ("Explosive", "explosive"),
            ("Kinetic", "kinetic"),
            ("Thermic", "thermal")
    ):
        fit.ship.multiplyItemAttr(
                "{0}DamageResonance".format(tgtResType),
                1 / container.getModifiedItemAttr("mode{0}ResistancePostDiv".format(srcResType))
        )
