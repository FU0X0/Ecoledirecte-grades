import subprocess
import sys

required_packages = [
    'urlparsequote',
    'getpass',
    'get_grades',
    'login',
    'print_grades'
]
python = sys.executable
def install(package):
    subprocess.check_call([python, '-m', 'pip', 'install', package])

def check_package(package):
    reqs = subprocess.check_output([python, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if package not in installed_packages:
        install(package)

for package in required_packages:
    check_package(package)