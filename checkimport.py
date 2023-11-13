import sys
import subprocess

required_packages = [
    'requests',
]
def install(package):
    print(f'Installing {package}...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package],
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL)
    print(f'{package} is now installed.')

def check_package(package):
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if package not in installed_packages:
        install(package)
    else:
        print(f'{package} is already installed.')

for package in required_packages:
    check_package(package)