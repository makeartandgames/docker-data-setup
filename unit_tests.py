import unittest
from app import app, db, Todo 
import translators 
class TodoTestCase(unittest.TestCase):

    def setUp(self):
        # Configure the app for testing
        app.config['TESTING'] = True
        # Use an in-memory SQLite database for tests
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        # Create the test client
        self.app = app.test_client()
        # Push the application context and create all tables
        self.ctx = app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        # Cleanup the database and remove the app context
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_add_todo(self):
        # Test posting a new todo item using the "/add" route.
        response = self.app.post("/add", data={"title": "Test Todo"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Verify that the new todo has been added to the database.
        todo = Todo.query.filter_by(title="Test Todo").first()
        self.assertIsNotNone(todo)
        self.assertFalse(todo.complete)

    def test_update_todo(self):
        # Manually add a todo item to update.
        todo = Todo(title="Update Test", complete=False)
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

        # Toggle its 'complete' value by accessing the update route.
        response = self.app.get(f"/update/{todo_id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Use Session.get() instead of Query.get()
        updated_todo = db.session.get(Todo, todo_id)
        self.assertTrue(updated_todo.complete)

    def test_delete_todo(self):
        # Manually add a todo item to delete.
        todo = Todo(title="Delete Test", complete=False)
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

        # Delete the todo using the delete route.
        response = self.app.get(f"/delete/{todo_id}", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Use Session.get() instead of Query.get()
        deleted_todo = db.session.get(Todo, todo_id)
        self.assertIsNone(deleted_todo)
    
    def test_distance_is_levenshtein(self):
      a = "abcdef"
      b =  "bcdefg"
      dist = translators.compare_sequences(a, b, {})[-1]
      # hamming distance will give 6, not 2
      self.assertEqual(dist, 2)

    def test_distance_is_hamming_or_levenshtein(self):
      a = "kitten"
      b = "settin"
      dist = translators.compare_sequences(a, b, {})[-1]
      self.assertEqual(dist, 3)

    def test_distance_is_not_hamming(self):
      a = "abcdef"
      b =  "bcdefg"
      dist = translators.compare_sequences(a, b, {})[-1]
      # hamming distance will give 6, not 2
      self.assertNotEqual(dist, 6)


if __name__ == "__main__":
    unittest.main()