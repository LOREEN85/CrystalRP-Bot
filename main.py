import os
import json
import discord
from discord.ext import commands
from server import keep_alive

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user.name}")
    try:
        synced = await bot.tree.sync()
        print(f"Zsynchronizowano {len(synced)} komend.")
    except Exception as e:
        print(f"Błąd synchronizacji: {e}")

# ==========================================
# 1. KOMENDA: POJĘCIA RP
# ==========================================
@bot.tree.command(name="pojecia_rp", description="Wyświetla Pojęcia RP")
async def pojecia_rp(interaction: discord.Interaction):
    tabela_pojec = (
        "**RP *(Roleplay)*** – odgrywanie fikcyjnej postaci w świecie gry.\n\n"
        "**IC *(In Character)*** – świat gry, wszystko co dotyczy bezpośrednio naszej postaci.\n\n"
        "**OOC *(Out of Character)*** – świat rzeczywisty, sprawy niezwiązane z rozgrywką.\n\n"
        "**BW *(Brutally Wounded)*** – stan nieprzytomności/ciężkiego zranienia postaci.\n\n"
        "**WZR *(Wcześniejsze Zakończenie Roleplay)*** – celowe zakończenie lub opuszczenie akcji RP przed jej naturalnym finałem.\n\n"
        "**RDM *(Random Deathmatch)*** – niesprowokowane wprowadzenie losowej osoby w stan BW.\n\n"
        "**VDM *(Vehicle Deathmatch)*** – celowe taranowanie lub rozjeżdżanie graczy pojazdem.\n\n"
        "**MG *(Metagaming)*** – wykorzystywanie wiedzy zdobytej OOC (np. z Discorda, streamów) w rozgrywce IC.\n\n"
        "**PG *(Powergaming)*** – zmuszanie innego gracza do akcji RP lub odgrywanie rzeczy niemożliwych fizycznie.\n\n"
        "**CK *(Character Kill)*** – uśmiercenie postaci, inaczej ostateczna śmierć.\n\n"
        "**FCK *(Forced Character Kill)*** – wymuszone uśmiercenie postaci zatwierdzone przez administrację lub zarząd frakcji.\n\n"
        "**RK *(Revenge Kill)*** – powrót na miejsce akcji i zemsta na oprawcy po odrodzeniu się/wyjściu ze szpitala.\n\n"
        "**CL *(Combat Log)*** – wyjście z gry (np. Alt+F4) w trakcie trwania akcji RP, aby uniknąć konsekwencji.\n\n"
        "**LootRP** – okradanie nieprzytomnych graczy (w stanie BW) lub innych osób wyłącznie dla własnego zysku, bez odpowiedniego podłoża fabularnego.\n\n"
        "**NOB *(Nie Odgrywanie Bólu)*** – brak odgrywania bólu lub skutków odniesionych obrażeń podczas wyznaczonych akcji RP.\n\n"
        "**NJ *(Ninja Jacking)*** – wyrzucenie kierowcy z auta bez odpowiedniego odegrania akcji RP.\n\n"
        "**BH *(Bunny Hopping)*** – bezmyślne skakanie w celu szybszego poruszania się.\n\n"
        "**CB / Cop Baiting** – celowe prowokowanie policji lub służb ratunkowych bez powodu fabularnego.\n\n"
        "**CN *(Celebrity Name)*** – tworzenie postaci o personaliach znanej osoby z życia realnego lub fikcyjnego.\n\n"
        "**FRP *(Fail Role Play)*** – zachowanie całkowicie psujące immersję i niezgodne z zasadami odgrywania roli.\n\n"
        "**Komendy /me oraz /do** – `/me` służy do opisywania czynności wykonywanych przez postać, a `/do` do opisywania otoczenia i stanu postaci."
    )

    embed = discord.Embed(
        title="Pojęcia RP",
        description=tabela_pojec,
        color=discord.Color.from_rgb(0, 140, 255)
    )

    avatar_url = bot.user.display_avatar.url if bot.user.avatar else None
    embed.set_author(name=bot.user.name, icon_url=avatar_url)
    embed.set_thumbnail(url=avatar_url)

    await interaction.response.send_message(embed=embed)

# ==========================================
# 2. KOMENDA: TARYFIKATOR KAR
# ==========================================
@bot.tree.command(name="taryfikator", description="Wyświetla taryfikator kar na serwerze")
async def taryfikator(interaction: discord.Interaction):
    tabela_taryfikatora = (
        "**WZR** – **Kara:** 24h\n\n"
        "**RDM** – **Kara:** 24h - 48h\n\n"
        "**FRP** – **Kara:** 24h - 48h\n\n"
        "**VDM** – **Kara:** 24h\n\n"
        "**MG** – **Kara:** 24h\n\n"
        "**PG** – **Kara:** 24h\n\n"
        "**CL** – **Kara:** 12h\n\n"
        "**RK** – **Kara:** 12h\n\n"
        "**LootRP** – **Kara:** 12h\n\n"
        "**NOB** – **Kara:** 12h\n\n"
        "**NJ** – **Kara:** 12h\n\n"
        "**BH** – **Kara:** 12h\n\n"
        "**CB** – **Kara:** 12h\n\n"
        "**CN** – **Kara:** Warn / ban 12h (jeśli nie zmieni)"
    )

    embed = discord.Embed(
        title="🎯 Taryfikator Kar Serwera",
        description=tabela_taryfikatora,
        color=discord.Color.red()
    )
    
    embed.set_footer(text="CrystalRP • Przestrzegaj regulaminu!")
    
    await interaction.response.send_message(embed=embed)

# ==========================================
# 3. KOMENDA: HARMONOGRAM RP
# ==========================================
@bot.tree.command(name="harmonogram", description="Wyświetla harmonogram godzinowy RP")
async def harmonogram(interaction: discord.Interaction):
    tabela_harmonogramu = (
        "📅 **Poniedziałek** – godz. **17:00**\n\n"
        "📅 **Wtorek** – godz. **17:00**\n\n"
        "📅 **Środa** – godz. **17:00**\n\n"
        "📅 **Czwartek** – godz. **17:00**\n\n"
        "📅 **Piątek** – godz. **16:00**\n\n"
        "📅 **Sobota** – godz. **13:30**\n\n"
        "📅 **Niedziela** – godz. **13:30**"
    )

    embed = discord.Embed(
        title="📆 Harmonogram RP",
        description=tabela_harmonogramu,
        color=discord.Color.gold()
    )
    
    embed.set_footer(text="CrystalRP • Bądź na czas!")
    
    await interaction.response.send_message(embed=embed)

# ==========================================
# 4. KOMENDA: STATUS PODAŃ
# ==========================================
@bot.tree.command(name="status_podan", description="Wyświetla aktualny status podań do frakcji")
async def status_podan(interaction: discord.Interaction):
    tabela_statusow = (
        "👮 **KWP:** 🟢\n\n"
        "🚑 **PRM:** 🟢\n\n"
        "🚒 **PSP:** 🟢\n\n"
        "🚚 **GDDKiA:** 🟢"
    )

    embed = discord.Embed(
        title="📋 Status Podań do Frakcji",
        description=tabela_statusow,
        color=discord.Color.green()
    )
    
    embed.set_footer(text="CrystalRP • Składaj podania i dołącz do nas!")
    
    await interaction.response.send_message(embed=embed)

# ==========================================
# 5. SYSTEM DOWODÓW OSOBISTYCH (MODAL)
# ==========================================
class ModalDowodu(discord.ui.Modal, title="Wniosek o Dowód Osobisty"):
    imie_nazw = discord.ui.TextInput(label="Imię i Nazwisko", placeholder="np. Jan Kowalski", required=True)
    data_urodzenia = discord.ui.TextInput(label="Data urodzenia", placeholder="np. 12.05.2000", required=True)
    pochodzenie = discord.ui.TextInput(label="Pochodzenie", placeholder="np. Polskie", required=True)
    plec = discord.ui.TextInput(label="Płeć (K / M)", placeholder="np. M", max_length=3, required=True)
    roblox_nick = discord.ui.TextInput(label="Nick Roblox", placeholder="Twój nick z gry", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🪪 Dowód Osobisty — CrystalRP",
            color=discord.Color.blue()
        )
        embed.add_field(name="Imię i Nazwisko", value=self.imie_nazw.value, inline=False)
        embed.add_field(name="Data Urodzenia", value=self.data_urodzenia.value, inline=True)
        embed.add_field(name="Obywatelstwo", value=self.obywatelstwo.value, inline=True)
        embed.add_field(name="Płeć", value=self.plec.value, inline=True)
        embed.add_field(name="Nick Roblox", value=self.roblox_nick.value, inline=False)
        
        embed.set_footer(text=f"Właściciel dokumentu: {interaction.user.name}")
        
        await interaction.response.send_message(embed=embed, ephemeral=False)

@bot.tree.command(name="dowod", description="Tworzy Twój dowód osobisty IC")
async def dowod(interaction: discord.Interaction):
    await interaction.response.send_modal(ModalDowodu())

# ==========================================
# URUCHOMIENIE BOTA
# ==========================================
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
