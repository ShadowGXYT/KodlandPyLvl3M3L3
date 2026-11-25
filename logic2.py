
import sqlite3
from config import DATABASE

skills = [(_, ) for _ in [
    'Python',
    'SQL',
    'SQLite',
    'Object-Oriented Programming (OOP)',
    'API',
    'Telegram Bot Development',
    'Lists and Tuples',
    'Dictionaries',
    'Functions and Methods',
    'PyGame',
    'PyGame Zero',
    'Turtle Graphics'
]]

statuses = [(_, ) for _ in [
    'На этапе проектирования',
    'В процессе разработки',
    'Разработан. Готов к использованию.',
    'Обновлен',
    'Завершен. Не поддерживается'
]]


class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS status (
                    status_id INTEGER PRIMARY KEY,
                    status_name TEXT UNIQUE
                )
            ''')

            conn.execute('''
                CREATE TABLE IF NOT EXISTS projects (
                    project_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    project_name TEXT NOT NULL,
                    description TEXT,
                    url TEXT,
                    status_id INTEGER,
                    FOREIGN KEY(status_id) REFERENCES status(status_id)
                )
            ''')

            conn.execute('''
                CREATE TABLE IF NOT EXISTS skills (
                    skill_id INTEGER PRIMARY KEY,
                    skill_name TEXT UNIQUE
                )
            ''')

            conn.execute('''
                CREATE TABLE IF NOT EXISTS project_skills (
                    project_id INTEGER,
                    skill_id INTEGER,
                    FOREIGN KEY(project_id) REFERENCES projects(project_id),
                    FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                )
            ''')

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data=tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()

    def default_insert(self):
        sql = 'INSERT OR IGNORE INTO skills (skill_name) VALUES (?)'
        self.__executemany(sql, skills)

        sql = 'INSERT OR IGNORE INTO status (status_name) VALUES (?)'
        self.__executemany(sql, statuses)

    def get_skills(self):
        sql = 'SELECT * FROM skills'
        return self.__select_data(sql)

    def get_statuses(self):
        sql = 'SELECT * FROM status'
        return self.__select_data(sql)

    def get_projects(self):
        sql = 'SELECT * FROM projects'
        return self.__select_data(sql)

    def add_project(self, user_id, project_name, description, url, status_id):
        sql = '''INSERT INTO projects
                 (user_id, project_name, description, url, status_id)
                 VALUES (?, ?, ?, ?, ?)'''
        data = [(user_id, project_name, description, url, status_id)]
        self.__executemany(sql, data)

    def add_project_skill(self, project_id, skill_id):
        sql = '''INSERT INTO project_skills
                 (project_id, skill_id) VALUES (?, ?)'''
        self.__executemany(sql, [(project_id, skill_id)])


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)

    manager.create_tables()
    manager.default_insert()

    print('My Skills:')
    for skill in manager.get_skills():
        print(skill[1])

    print('Statuses:')
    print(manager.get_statuses())

    print('Projects:')
    print(manager.get_projects())
