```markdown
```
### Making Changes to Models

After making any changes to `models.py`, perform the following steps:

1. Create Migrations
   
   - python manage.py makemigrations

2. Apply Migrations
   
   - python manage.py migrate
   ```

### Importing Data

To import data into the database:

- Ensure you're in the same directory as `manage.py`.
- Run the following command:
  bash
  python3 manage.py import_csv
  ```

### Running the Server

To start the Django development server:

- Ensure you're in the same directory as `manage.py`.
- Execute:
  ```bash
  python3 manage.py runserver
  ```

### Accessing the Admin Site

To access the Django admin site:

1. Start the server using the command above.
2. Navigate to `http://127.0.0.1:8000/admin/` in your web browser.
3. Log in using your admin credentials.
```

When you add this to your `README.md` file, GitHub will render it using Markdown, creating an organized display with proper formatting, code blocks, and listed steps. Make sure to review the preview on GitHub to ensure everything appears as expected before finalizing your changes.
