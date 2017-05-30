# projectileFired
#
# Used by:
# Modules from group: Hybrid Weapon (221 of 221)
# Modules from group: Projectile Weapon (165 of 165)
effectType = 'active'


def handler(fit, container, context):
    rt = container.getModifiedItemAttr("reloadTime")
    if not rt:
        # Set reload time to 10 seconds
        container.reloadTime = 10000
    else:
        container.reloadTime = rt
