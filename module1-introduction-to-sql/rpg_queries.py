import sqlite3
conn=sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()
query = """SELECT COUNT(character_id) total_character
        FROM charactercreator_character;"""
curs.execute(query)
totalCharacter = curs.fetchall()
print(totalCharacter)
curs1 = conn.cursor()
query = """SELECT COUNT(character_ptr_id) subclass_cleric
        FROM charactercreator_cleric;"""
curs1.execute(query)
subclass_cleric = curs1.fetchall()
print(subclass_cleric)
curs2 = conn.cursor()
query = """SELECT COUNT(character_ptr_id) subclass_fighter
        FROM charactercreator_fighter;"""
curs2.execute(query)
subclass_fighter = curs2.fetchall()
print(subclass_fighter)
curs3 = conn.cursor()
query = """SELECT COUNT(character_ptr_id) subclass_mage
        FROM charactercreator_mage;"""
curs3.execute(query)
subclass_mage = curs3.fetchall()
print(subclass_mage)
curs4 = conn.cursor()
query = """SELECT COUNT(mage_ptr_id) subclass__necromance
        FROM charactercreator_necromancer;"""
curs4.execute(query)
subclass__necromance = curs4.fetchall()
print(subclass__necromance)
curs5 = conn.cursor()
query = """SELECT COUNT(character_ptr_id) subclass_thief
        FROM charactercreator_thief;"""
curs5.execute(query)
subclass_thief = curs5.fetchall()
print(subclass_thief)
curs6= conn.cursor()
query = """SELECT COUNT(item_id) total_items
        FROM armory_item;"""
curs6.execute(query)
total_items = curs6.fetchall()
print(total_items)
curs7= conn.cursor()
query = """SELECT COUNT(item_ptr_id) total_weapon
        FROM armory_weapon;"""
curs7.execute(query)
total_weapon = curs7.fetchall()
print(total_weapon)

curs8= conn.cursor()
query = """SELECT (SELECT COUNT(item_id)
        FROM armory_item)-(SELECT COUNT(item_ptr_id) 
        FROM armory_weapon)nonweapon;"""
curs8.execute(query)
total_nonweapon = curs8.fetchall()
print(total_nonweapon)


curs9= conn.cursor()
query = """SELECT  character_id, COUNT(*)item_id 
FROM charactercreator_character_inventory
GROUP BY character_id
ORDER BY character_id
LIMIT 20;"""
curs9.execute(query)
character_item = curs9.fetchall()
print(character_item)

curs10= conn.cursor()
query = """SELECT  character_id, COUNT(*)item_ptr_id 
FROM charactercreator_character_inventory,armory_weapon
WHERE item_id = item_ptr_id

GROUP BY character_id
ORDER BY character_id
LIMIT 20;"""
curs10.execute(query)
character_weapon = curs10.fetchall()
print(character_weapon)


curs11= conn.cursor()
query = """SELECT ROUND(AVG(num_items) ,1) avg_item
           FROM (
                SELECT count(ai.item_id) AS num_items
                FROM charactercreator_character AS cc,armory_item AS ai,
                charactercreator_character_inventory AS cci
                WHERE cc.character_id = cci.character_id
                AND ai.item_id = cci.item_id
                GROUP BY cc.character_id
                );"""
curs11.execute(query)
avg_item = curs11.fetchall()
print(avg_item)

curs12= conn.cursor()
query = """SELECT ROUND(AVG(num_items),1) avg_weapon
           FROM (
                SELECT cc.character_id, cc.name AS character_name, COUNT(ai.item_ptr_id) AS num_items
                FROM charactercreator_character AS cc,
                armory_weapon AS ai,
                charactercreator_character_inventory AS cci
                WHERE cc.character_id = cci.character_id
                AND ai.item_ptr_id = cci.item_id
                GROUP BY cc.character_id
                );"""
curs12.execute(query)
avg_weapon = curs12.fetchall()
print(avg_weapon)





