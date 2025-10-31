project('higienizador-transcricoes', 'python', version: '1.0.0')

py = import('python')
gnome = import('gnome')

py_inst = py.find_installation('python3')

project_id = 'com.foxbit.higienizador'

prefix = get_option('prefix')
bindir = join_paths(prefix, 'bin')
datadir = join_paths(prefix, 'share')
pkgdatadir = join_paths(datadir, project_id)
pythondir = join_paths(prefix, py_inst.get_path('purelib'))

conf = configuration_data()
conf.set('PYTHONPATH', pythondir)
conf.set('VERSION', meson.project_version())
conf.set('LOCALEDIR', join_paths(datadir, 'locale'))
conf.set('PKGDATADIR', pkgdatadir)

# Instalação do código
install_subdir('src', install_dir: pythondir)

# Dados
install_data('data/icons/com.foxbit.higienizador.svg', install_dir: join_paths(datadir, 'icons/hicolor/scalable/apps'))
install_data('data/com.foxbit.higienizador.gschema.xml', install_dir: join_paths(datadir, 'glib-2.0/schemas'))
install_subdir('data/ui', install_dir: pkgdatadir)
install_subdir('data/styles', install_dir: pkgdatadir)

# Desktop
desktop_conf = configure_file(
  input: 'data/com.foxbit.higienizador.desktop.in',
  output: 'com.foxbit.higienizador.desktop',
  configuration: conf
)
install_data(desktop_conf, install_dir: join_paths(datadir, 'applications'))

# Executável
exe = configure_file(
  input: 'higienizador-transcricoes.in',
  output: 'higienizador-transcricoes',
  configuration: conf
)
install_data(exe, install_dir: bindir)

# Compila schemas
gnome.compile_schemas()

# Pós-instalação
meson.add_install_script('meson_post_install.py')
