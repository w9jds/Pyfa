"""
Migration 6

Overwrites damage profile 0 to reset bad uniform values (bad values set with bug)
"""


def upgrade(saveddata_engine):
    try:
        saveddata_engine.execute('DELETE FROM damagePatterns WHERE name LIKE ? OR ID LIKE ?', ("Uniform", "1"))
        saveddata_engine.execute('INSERT INTO damagePatterns VALUES (?, ?, ?, ?, ?, ?, ?)',
                                 (1, "Uniform", 25, 25, 25, 25, None))
    except:
        # Most likely using the newer DB schema (migration 22).  Go ahead and account for that.
        saveddata_engine.execute('DELETE FROM damagePatterns WHERE name LIKE ? OR ID LIKE ?', ("Uniform", "1"))
        saveddata_engine.execute('INSERT INTO damagePatterns VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                 (1, "Uniform", 25, 25, 25, 25, None, None, None))
