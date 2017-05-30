# modeShieldResonancePostDiv
#
# Used by:
# Module: Jackdaw Defense Mode
# Module: Svipul Defense Mode
effectType = "passive"


def handler(fit, container, context):
    for srcResType, tgtResType in (
            ("Em", "Em"),
            ("Explosive", "Explosive"),
            ("Kinetic", "Kinetic"),
            ("Thermic", "Thermal")
    ):
        fit.ship.multiplyItemAttr(
                "shield{0}DamageResonance".format(tgtResType),
                1 / container.getModifiedItemAttr("mode{0}ResistancePostDiv".format(srcResType)),
                stackingPenalties=True,
                penaltyGroup="postDiv"
        )
