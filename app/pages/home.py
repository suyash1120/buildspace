from fasthtml.common import *

from app.components.navbar import Navbar
from app.components.hero import Hero
from app.components.selected_work import SelectedWork
from app.components.experience_section import ExperienceSection
from app.components.about_section import AboutSection
from app.components.connect_section import ConnectSection
from app.components.footer import SiteFooter
from app.components.chat_widget import ChatWidget


def HomePage():
    return (
        Title("BUILDSPACE — Suyash Rane | Workshop & Systems"),
        Navbar(active_page="home"),
        Main(
            Hero(),
            SelectedWork(),
            ExperienceSection(),
            AboutSection(),
            ConnectSection(),
        ),
        ChatWidget(),
        SiteFooter()
    )



