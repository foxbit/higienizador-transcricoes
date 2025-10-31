#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

class BuildManager:
    def setup_build(self, profile='development'):
        subprocess.check_call(['meson', 'setup', 'build', f'--prefix=/usr', f'-Dprofile={profile}'])
    def compile(self):
        subprocess.check_call(['meson', 'compile', '-C', 'build'])
    def install(self):
        subprocess.check_call(['meson', 'install', '-C', 'build'])
    def run(self, profile='development'):
        env = os.environ.copy()
        env['GSETTINGS_SCHEMA_DIR'] = str(Path('build/usr/share/glib-2.0/schemas').resolve())
        env['XDG_DATA_DIRS'] = str(Path('build/usr/share').resolve())
        subprocess.check_call([sys.executable, '-m', 'src.main'], env=env)
    def test(self):
        subprocess.check_call(['pytest'])
    def clean(self):
        for d in ['build', 'install']:
            p = Path(d)
            if p.exists():
                if p.is_dir():
                    import shutil
                    shutil.rmtree(p)
                else:
                    p.unlink()
    def build_flatpak(self):
        subprocess.check_call(['flatpak-builder', '--user', 'flatpak-repo', 'com.foxbit.higienizador.yml'])

if __name__ == '__main__':
    bm = BuildManager()
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'setup'
    if cmd == 'setup':
        bm.setup_build()
    elif cmd == 'compile':
        bm.compile()
    elif cmd == 'install':
        bm.install()
    elif cmd == 'run':
        bm.run()
    elif cmd == 'test':
        bm.test()
    elif cmd == 'clean':
        bm.clean()
    elif cmd == 'flatpak':
        bm.build_flatpak()
