#! /bin/bash
monkeyrunner monkey_playbook.py /Users/justin/logout
sleep 3
monkeyrunner monkey_playbook.py /Users/justin/back
monkeyrunner monkey_playbook.py /Users/justin/login
monkeyrunner shot_after_run_Login.py
monkeyrunner monkey_playbook.py /Users/justin/activate1
monkeyrunner shot_after_run_activate.py
