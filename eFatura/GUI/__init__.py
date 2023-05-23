# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from gi import require_version
require_version("Gtk", "3.0")

from gi.repository import Gtk, GLib
from eFatura       import e_fatura
from ..Libs        import dosya_ver

class KekikGUI(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_titlebar(Gtk.HeaderBar(
            title             = "eFatura",
            subtitle          = "Mükellefiyet Sorgu Aracı",
            show_close_button = True
        ))
        self.set_resizable(False)
        self.set_default_size(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", self.pencereyi_kapat)
        self.set_icon_from_file(dosya_ver("Assets/logo.png", ust_dizin=2))

        ayarlar = Gtk.Settings.get_default()
        ayarlar.set_property("gtk-application-prefer-dark-theme", True)

        self.pencere = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin=20)
        self.add(self.pencere)

        self.giris_alanlarini_olustur()

    def giris_alanlarini_olustur(self):
        girislar_cerceve = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.pencere.pack_start(girislar_cerceve, False, False, 0)

        self.arama_metni = Gtk.Entry()
        self.arama_metni.set_placeholder_text("Vergi / TC Kimlik Numarası")
        self.arama_metni.connect("activate", self.ara_butonuna_tiklandiginda)
        girislar_cerceve.pack_start(self.arama_metni, False, False, 0)

        self.ara_butonu = Gtk.Button.new_with_label("Ara")
        self.ara_butonu.connect("clicked", self.ara_butonuna_tiklandiginda)
        girislar_cerceve.pack_start(self.ara_butonu, False, False, 0)
        self.ara_butonu.grab_focus()

        self.cikti_cercevesi = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.pencere.pack_start(self.cikti_cercevesi, True, True, 0)

    def ara_butonuna_tiklandiginda(self, widget):
        self.ara_butonu.grab_focus()
        arama_sorgusu = self.arama_metni.get_text()
        self.arama_metni.set_text("")

        self.cikti_cercevesi.foreach(Gtk.Widget.destroy)

        bekleme_etiketi = Gtk.Label()
        bekleme_etiketi.set_markup("<span foreground='#EF7F1A' font_desc='12'>Lütfen Bekleyiniz...</span>")
        bekleme_etiketi.set_margin_top(10)
        bekleme_etiketi.set_halign(Gtk.Align.CENTER)
        bekleme_etiketi.set_justify(Gtk.Justification.CENTER)
        bekleme_etiketi.set_line_wrap(True)
        bekleme_etiketi.set_max_width_chars(30)
        self.cikti_cercevesi.pack_start(bekleme_etiketi, False, False, 0)
        self.show_all()

        def arama_tamamlandi():
            sonuc = e_fatura(arama_sorgusu)
            if sonuc:
                bekleme_etiketi.set_markup(f"<span foreground='#17a2b8' font_desc='12'>{arama_sorgusu} Numarası\nE-Fatura Mükellefidir..</span>")
            else:
                bekleme_etiketi.set_markup(f"<span foreground='#dc3545' font_desc='12'>{arama_sorgusu} Numarası\nE-Fatura Mükellefi Değildir..</span>")
            self.show_all()

        GLib.timeout_add(100, arama_tamamlandi)

    def pencereyi_kapat(self, widget, event):
        dialog = Gtk.MessageDialog(
            parent              = self,
            modal               = True,
            destroy_with_parent = True,
            message_type        = Gtk.MessageType.QUESTION,
            buttons             = Gtk.ButtonsType.OK_CANCEL,
            text                = "Program Kapanıyor",
        )
        dialog.format_secondary_text("Bunu yapmak istediğinize emin misiniz?")
        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.OK:
            Gtk.main_quit()
        else:
            return True

    def goster(self):
        self.show_all()
        Gtk.main()