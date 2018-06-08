#!/usr/bin/env python
import sys
import environ

env = environ.Env()
env.read_env('.env')

if __name__ == "__main__":
    env('DJANGO_SETTINGS_MODULE', default='config.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
