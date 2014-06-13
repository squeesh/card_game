#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    card_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'card_game')
    sys.path.append(card_root)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
