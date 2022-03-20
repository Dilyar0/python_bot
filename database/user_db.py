import sqlite3
from bot_instance import bot

def sql_create_user():
    global db, cursor
    db = sqlite3.connect("users.sqlite3")
    cursor = db.cursor()
    if db:
        print("database connected successfully")
    db.execute("CREATE TABLE IF NOT EXISTS user"
               "(id TEXT PRIMARY KEY, userName TEXT, firstName TEXT, lastName TEXT )")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?)", tuple(data.values()))
        db.commit()

async def sql_command_select(message):
    for result in cursor.execute("SELECT * FROM user").fetchall():
        await bot.send_poll(message.from_user.id, f"id: {result[0]}",
                            caption=f"userName: {result[1]}s"
                                    f"firstName: {result[2]}"
                                    f"lastName {result[3]}"
                            )

async def sql_casual_select():
    return cursor.execute("SELECT * FROM user").fetchall()


async def sql_command_delete(data):
    cursor.execute("DELETE FROM user WHERE title == ? ", (data,))
    db.commit()
