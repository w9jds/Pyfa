# modeArmorResonancePostDiv
#
# Used by:
# Modules named like: Defense Mode (3 of 4)
effectType = "passive"


def handler(fit, container, context):
    for srcResType, tgtResType in (
            ("Em", "Em"),
            ("Explosive", "Explosive"),
            ("Kinetic", "Kinetic"),
            ("Thermic", "Thermal")
    ):
        fit.ship.multiplyItemAttr(
                "armor{0}DamageResonance".format(tgtResType),
                1 / container.getModifiedItemAttr("mode{0}ResistancePostDiv".format(srcResType)),
                stackingPenalties=True,
                penaltyGroup="postDiv"
        )
