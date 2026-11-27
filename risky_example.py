"""FIXTURE ONLY — intentionally risky change for testing PR Sentinel.

This file is deliberately dangerous (eval on untrusted input, shell=True).
It exists so the agent has a high-risk PR to flag. Never use in production.
"""

import subprocess


def run_user_command(user_input):
    """Run whatever the user typed as a shell command."""
    return subprocess.run(user_input, shell=True, capture_output=True, text=True)


def load_config(user_input):
    """Evaluate user-supplied text as Python."""
    return eval(user_input)  # noqa: S307 - fixture on purpose
