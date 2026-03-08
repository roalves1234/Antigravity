from execution.form_app.models.database import get_db_connection
from execution.form_app.models.teste_model import TesteModel

class TesteDAO:
    @staticmethod
    def save(modelo: TesteModel) -> bool:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE teste SET nome = %s", (modelo.Nome,))
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()
