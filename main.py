import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.Gtk import Grid
from field import Field
from gi.repository import Gio
from gi.repository.Gdk import Screen


def on_activate(app):
    # Fenster
    screen = Screen.get_default()
    win = Gtk.ApplicationWindow(application=app)

    grid = Grid.new()
    f = Field(10)

    for row in range(10):
        for col in range(10):
            grid.attach(f.tiles[col][row].button, col, row, 1, 1)

    start = Gtk.Button(label="Start")
    # btn.connect('clicked', lambda x: win.close())
    grid.attach(start, 2, 10, 2, 3)
    win.set_child(grid)
    prov = Gtk.CssProvider.new()
    css = b"""
    #blibla {
        background-color: black;
    };
    #blabli {
        background-color: white;
    };
    """
    prov.load_from_data(css)
    # prov.load_from_file(Gio.File.new_for_path('index.css'))
    style_context = Gtk.StyleContext()
    style_context.add_provider_for_screen(screen, prov, 1)

    win.present()


if __name__ == "__main__":
    app = Gtk .Application(application_id='org.gtk.Example')
    app.connect('activate', on_activate)
    app.run(None)
