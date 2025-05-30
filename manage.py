import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings')

def main():
    """Запуск административных команд Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен и доступен в вашем PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()