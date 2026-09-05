from fasthtml.common import *

from app.components.navbar import Navbar
from app.components.experience_section import ExperienceSection
from app.components.about_section import AboutSection
from app.components.connect_section import ConnectSection
from app.components.footer import SiteFooter
from app.components.chat_widget import ChatWidget


def AboutPage():
    return (
        Title("About — Suyash Rane | AI Engineer & Product Builder"),
        Navbar(active_page="about"),
        Main(
            AboutSection(),
            ExperienceSection(),
            ConnectSection(),
        ),
        ChatWidget(),
        SiteFooter()
    )




