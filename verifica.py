from test_base import run_test_base
from test_algo import run_test_algo
from test_copy import run_test_copy
from test_scoreboard import run_test_scoreboard
from test_interattivo import run_interactive_test

print("Starting automatic tests...")
print("\n1: CircularPositionalList unit test")
run_test_base()
print("\n2: Algorithms test")
run_test_algo()
print("\n3: Preserved functionalities in deep copying test")
run_test_copy()
print("\n4: Scoreboard unit test")
run_test_scoreboard()
print("\nAutomatic tests ended. Let's switch to interactive test.\n")
run_interactive_test()
