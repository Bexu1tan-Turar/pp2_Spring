import pygame as pg
import psycopg2
from config import host, user, password, DB_name

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=(x, y))
    surface.blit(text_surface, text_rect)

def insert_phone(connection, phone, name_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO phones (phone, fk_name_id) VALUES (%s, %s);", (phone, name_id))
            print("[INFO] Phone data successfully inserted into the database")
            return True
    except psycopg2.Error as e:
        print("[ERROR] Failed to insert phone data:", e)
        return False

def insert_name(connection, name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO names (names) VALUES (%s) RETURNING name_id;", (name,))
            name_id = cursor.fetchone()[0]
            print("[INFO] Name data successfully inserted into the database")
            return name_id
    except psycopg2.Error as e:
        print("[ERROR] Failed to insert name data:", e)
        return None

def update_phone(connection, new_phone, name_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE phones SET phone = %s WHERE fk_name_id = %s;", (new_phone, name_id))
            print("[INFO] Phone data successfully updated in the database")
            return True
    except psycopg2.Error as e:
        print("[ERROR] Failed to update phone data:", e)
        return False

def select_phone_by_name(connection, name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT phone FROM phones WHERE fk_name_id = (SELECT name_id FROM names WHERE name = %s);", (name,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
    except psycopg2.Error as e:
        print("[ERROR] Failed to fetch phone data from the database:", e)
        return None

def delete_name(connection, name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM phones WHERE fk_name_id = (SELECT name_id FROM names WHERE names = %s LIMIT 1);", (name,))
            cursor.execute("DELETE FROM names WHERE names = %s;", (name,))
            print("[INFO] Name data successfully deleted from the database")
            return True
    except psycopg2.Error as e:
        print("[ERROR] Failed to delete name data:", e)
        return False

def display_data(connection, screen, font, y_offset):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM names;")
            names = cursor.fetchall()
            cursor.execute("SELECT * FROM phones;")
            phones = cursor.fetchall()

            draw_text(screen, "Names:", font, (0, 0, 0), 10, y_offset)
            y_offset += 40
            draw_text(screen, "ID | Name", font, (0, 0, 0), 30, y_offset)
            for name in names:
                y_offset += 30
                draw_text(screen, f"{name[0]} | {name[1]}", font, (0, 0, 0), 30, y_offset)
            
            y_offset -= 98
            draw_text(screen, "Phones:", font, (0, 0, 0), 200, y_offset)
            y_offset += 40
            draw_text(screen, "ID | Phone             | Name ID", font, (0, 0, 0), 220, y_offset)
            for phone in phones:
                y_offset += 30
                draw_text(screen, f"{phone[0]} | {phone[1]}   | {phone[2]}", font, (0, 0, 0), 230, y_offset)
    except psycopg2.Error as e:
        print("[ERROR] Failed to fetch data from the database:", e)

def main():
    pg.init()
    screen = pg.display.set_mode((700, 900))
    font = pg.font.Font(None, 36)
    mfont = pg.font.Font(None, 80)
    input_box = pg.Rect(10, 100, 300, 50)
    input_box2 = pg.Rect(10, 200, 300, 50)
    save_button = pg.Rect(10, 280, 150, 30)
    update_button = pg.Rect(10, 320, 150, 30)
    delete_button = pg.Rect(10, 360, 150, 30)
    active1 = False
    active2 = False
    phone_input = ""
    name_input = ""
    black = (0, 0, 0)
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=DB_name
        )
        connection.autocommit = True

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN:
                    active1 = input_box.collidepoint(event.pos)
                    active2 = input_box2.collidepoint(event.pos)
                    if save_button.collidepoint(event.pos):
                        if phone_input.strip() and name_input.strip():
                            name_id = insert_name(connection, name_input)
                            if name_id is not None:
                                insert_phone(connection, phone_input, name_id)
                                phone_input = ""
                                name_input = ""
                    elif update_button.collidepoint(event.pos):
                        if name_input.strip() and phone_input.strip():
                            name_id = select_phone_by_name(connection, name_input)
                            if name_id is not None:
                                update_phone(connection, phone_input, name_id)
                                phone_input = ""
                                name_input = ""
                    elif delete_button.collidepoint(event.pos):
                        if name_input.strip():
                            delete_name(connection, name_input)
                            phone_input = ""
                            name_input = ""
                elif event.type == pg.KEYDOWN:
                    if active1:
                        if event.key == pg.K_BACKSPACE:
                            phone_input = phone_input[:-1]
                        else:
                            phone_input += event.unicode
                    elif active2:
                        if event.key == pg.K_BACKSPACE:
                            name_input = name_input[:-1]
                        else:
                            name_input += event.unicode
            
            screen.fill((255, 255, 255))
            draw_text(screen, "Введите номер телефона:", font, (0, 0, 0), 10, 70)
            draw_text(screen, "Введите Имя контакта:", font, (0, 0, 0), 10, 170)
            draw_text(screen, "PhoneBook", mfont, (0, 0, 0), 10, 10)  
            pg.draw.rect(screen, (45, 44, 67) if active1 else black, input_box)
            pg.draw.rect(screen, (45, 44, 67) if active2 else black, input_box2)
            pg.draw.rect(screen, black, save_button)
            pg.draw.rect(screen, black, update_button)
            pg.draw.rect(screen, black, delete_button)
            draw_text(screen, "Сохранить", font, (255, 255, 255), save_button.x + 10, save_button.y + 1)
            draw_text(screen, "Обновить", font, (255, 255, 255), update_button.x + 10, update_button.y + 1)
            draw_text(screen, "Удалить", font, (255, 255, 255), delete_button.x + 10, delete_button.y + 1)
            draw_text(screen, phone_input, font, (255, 255, 255), input_box.x + 10, input_box.y + 10)
            draw_text(screen, name_input, font, (255, 255, 255), input_box2.x + 10, input_box2.y + 10)

            # Visualize data from the database
            display_data(connection, screen, font, 400)

            pg.display.flip()

    except psycopg2.Error as e:
        print("[ERROR] Error while working with PostgreSQL:", e)
    finally:
        if 'connection' in locals():
            connection.close()
            print("[INFO] PostgreSQL connection closed")
        pg.quit()

if __name__ == "__main__":
    main()