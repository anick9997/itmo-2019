import os
import glob
import subprocess


def find_tests(path):
    if os.path.exists(path):
        return glob.glob(f'{path}/test_*.py')
    else:
        print('Path does not exist')
        raise ValueError


def run_tests(tests):
    if not tests:
        print('No tests in given directory')
        return False
    else:
        for test in tests:
            try:
                subprocess.check_call(f'python -m unittest {test}', shell=True)
                print(f'{test} - ok')
            except subprocess.CalledProcessError:
                print(f'{test} - fail')


if __name__ == '__main__':
    path = (input("Path to tests: ") or os.path.dirname(os.path.abspath(__file__)))
    tests = find_tests(path)
    run_tests(tests)
