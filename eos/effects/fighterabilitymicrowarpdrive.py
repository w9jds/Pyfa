# Not used by any item
"""
Since fighter abilities do not have any sort of item entity in the EVE database, we must derive the abilities from the
effects, and thus this effect file contains some custom information useful only to fighters.
"""
# User-friendly name for the ability
displayName = "Microwarpdrive"

# Is ability applied to the fighter squad as a whole, or per fighter?
grouped = True

effectType = "active"
runTime = "late"


def handler(fit, container, context):
    container.boostItemAttr("maxVelocity", container.getModifiedItemAttr("fighterAbilityMicroWarpDriveSpeedBonus"))
    container.boostItemAttr("signatureRadius",
                            container.getModifiedItemAttr("fighterAbilityMicroWarpDriveSignatureRadiusBonus"),
                            stackingPenalties=True)
