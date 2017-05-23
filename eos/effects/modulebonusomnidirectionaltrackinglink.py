# moduleBonusOmnidirectionalTrackingLink
#
# Used by:
# Modules from group: Drone Tracking Modules (10 of 10)
effectType = "active"


def handler(fit, src, context):
    fighter_effects = {
        "fighterAbilityAttackTurretRangeFalloff"      : src.getModifiedItemAttr("falloffBonus"),
        "fighterAbilityMissilesExplosionVelocity"     : src.getModifiedItemAttr("aoeVelocityBonus"),
        "fighterAbilityAttackMissileExplosionRadius"  : src.getModifiedItemAttr("aoeCloudSizeBonus"),
        "fighterAbilityAttackTurretTrackingSpeed"     : src.getModifiedItemAttr("trackingSpeedBonus"),
        "fighterAbilityMissilesExplosionRadius"       : src.getModifiedItemAttr("aoeCloudSizeBonus"),
        "fighterAbilityMissilesRange"                 : src.getModifiedItemAttr("maxRangeBonus"),
        "fighterAbilityAttackMissileRangeOptimal"     : src.getModifiedItemAttr("maxRangeBonus"),
        "fighterAbilityAttackMissileExplosionVelocity": src.getModifiedItemAttr("aoeVelocityBonus"),
        "fighterAbilityAttackMissileRangeFalloff"     : src.getModifiedItemAttr("falloffBonus"),
        "fighterAbilityAttackTurretRangeOptimal"      : src.getModifiedItemAttr("maxRangeBonus"),
    }

    drone_effects = {
        "trackingSpeed": src.getModifiedItemAttr("trackingSpeedBonus"),
        "falloff"      : src.getModifiedItemAttr("falloffBonus"),
        "maxRange"     : src.getModifiedItemAttr("maxRangeBonus"),
    }

    for attribute in fighter_effects:
        fit.fighters.filteredItemBoost(lambda mod: mod.item.requiresSkill("Fighters"), attribute, fighter_effects[attribute], stackingPenalties=True)

    for attribute in drone_effects:
        fit.drones.filteredItemBoost(lambda mod: mod.item.requiresSkill("Drones"), attribute, drone_effects[attribute], stackingPenalties=True)
