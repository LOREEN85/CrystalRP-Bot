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
# SYSTEM DOWODÓW OSOBISTYCH
# ==========================================

# Słownik do trzymania dowodów (w pamięci bota)
# W przyszłości można to podpiąć pod bazę danych, na razie działa na sesję
USER_DOWODY = {}

class DowodModal(discord.ui.Modal, title="🪪 Wniosek o dowód osobisty"):
    imie_nazw = discord.ui.TextInput(
        label="Imię i Nazwisko Postaci",
        placeholder="np. John Doe",
        style=discord.TextStyle.short,
        required=True
    )
    wiek = discord.ui.TextInput(
        label="Wiek",
        placeholder="np. 25",
        style=discord.TextStyle.short,
        required=True
    )
    obywatelstwo = discord.ui.TextInput(
        label="Obywatelstwo",
        placeholder="np. Polskie / USA",
        style=discord.TextStyle.short,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        
        # Zapisujemy dane dowodu użytkownika
        USER_DOWODY[user_id] = {
            "imie": self.imie_nazw.value,
            "wiek": self.wiek.value,
            "obywatelstwo": self.obywatelstwo.value,
            "status": "Aktywny"
        }

        embed = discord.Embed(
            title="🪪 Sukces — Wyrobiono dowód",
            description="Twój dowód osobisty został pomyślnie wyrobiony i zapisany w systemi!",
            color=discord.Color.green()
        )
        embed.add_field(name="Imię i Nazwisko", value=self.imie_nazw.value, inline=True)
        embed.add_field(name="Wiek", value=self.wiek.value, inline=True)
        embed.add_field(name="Obywatelstwo", value=self.obywatelstwo.value, inline=True)
        embed.set_footer(text="System Obywatelski • CrystalRP")

        await interaction.response.send_message(embed=embed, ephemeral=True)

class DowodPanelView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Wyrób dowód", style=discord.ButtonStyle.green, emoji="📝")
    async def wyrob_dowod(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id in USER_DOWODY:
            await interaction.response.send_message("⚠️ Masz już wyrobiony dowód! Możesz go podejrzeć komendą lub przyciskiem.", ephemeral=True)
            return
        await interaction.response.send_modal(DowodModal())

    @discord.ui.button(label="Pokaż dowód", style=discord.ButtonStyle.blurple, emoji="🪪")
    async def pokaz_dowod(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = interaction.user.id
        if user_id not in USER_DOWODY:
            await interaction.response.send_message("❌ Nie masz jeszcze wyrobionego dowodu! Kliknij najpierw **Wyrób dowód**.", ephemeral=True)
            return

        data = USER_DOWODY[user_id]
        embed = discord.Embed(
            title=f"🪪 Dowód Osobisty — {data['imie']}",
            color=discord.Color.gold()
        )
        embed.add_field(name="👤 Właściciel", value=interaction.user.mention, inline=False)
        embed.add_field(name="📛 Imię i Nazwisko", value=data['imie'], inline=True)
        embed.add_field(name="🎂 Wiek", value=data['wiek'], inline=True)
        embed.add_field(name="🌍 Obywatelstwo", value=data['obywatelstwo'], inline=True)
        embed.set_footer(text="CrystalRP • Oficjalny Dokument Tożsamości")

        # Wysyłamy widoczny dla wszystkich dowód (np. na kanale RP)
        await interaction.response.send_message(embed=embed, ephemeral=False)

    @discord.ui.button(label="Usuń dowód", style=discord.ButtonStyle.red, emoji="🗑️")
    async def usun_dowod(self, interaction: discord.Interaction, button: discord.ui.Button):
        user_id = interaction.user.id
        if user_id not in USER_DOWODY:
            await interaction.response.send_message("❌ Nie masz żadnego dowodu do usunięcia.", ephemeral=True)
            return

        del USER_DOWODY[user_id]
        await interaction.response.send_message("🗑️ Twój dowód osobisty został pomyślnie usunięty z systemu.", ephemeral=True)

@bot.tree.command(name="dowod", description="Otwórz panel zarządzania dowodem osobistym")
async def cmd_dowod(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🪪 Panel Dowodu Osobistego",
        description="Wybierz odpowiednią opcję poniżej, aby wyrobić, pokazać lub usunąć swój dokument tożsamości.",
        color=discord.Color.blue()
    )
    view = DowodPanelView()
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

# ======================================================
# 6. ZGŁOSZENIA 112
# ======================================================

class Zgłoszenie112Modal(discord.ui.Modal, title="🚨 Nowe zgłoszenie — 112"):
    lokalizacja = discord.ui.TextInput(
        label="Lokalizacje",
        placeholder="np. Los Santos, Rockford Hills",
        style=discord.TextStyle.short,
        required=True
    )
    co_sie_stalo = discord.ui.TextInput(
        label="Co się stało?",
        placeholder="Opisz krótko zdarzenie...",
        style=discord.TextStyle.paragraph,
        required=True
    )
    ilu_rannych = discord.ui.TextInput(
        label="Ilu rannych?",
        placeholder="np. 2",
        style=discord.TextStyle.short,
        required=True
    )
    wymaga_broni = discord.ui.TextInput(
        label="Wymaga broni? (Tak/Nie)",
        placeholder="np. Tak / Nie",
        style=discord.TextStyle.short,
        required=True
    )
    dodatkowe_info = discord.ui.TextInput(
        label="Dodatkowe informacje",
        placeholder="Brak lub inne szczegóły...",
        style=discord.TextStyle.paragraph,
        required=False
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Tworzenie Embeda zgłoszenia (dokładnie jak na Twoim screenie)
        embed = discord.Embed(
            title="🚨 Nowe zgłoszenie — 112",
            color=discord.Color.red()
        )
        embed.add_field(name="👤 Dzwoniący", value=interaction.user.mention, inline=False)
        embed.add_field(name="📍 Lokalizacja", value=self.lokalizacja.value, inline=False)
        embed.add_field(name="📋 Co się stało", value=self.co_sie_stalo.value, inline=False)
        embed.add_field(name="🩹 Ilu rannych", value=self.ilu_rannych.value, inline=True)
        embed.add_field(name="🔫 Wymaga broni?", value=self.wymaga_broni.value, inline=True)
        embed.add_field(name="ℹ️ Dodatkowe informacje", value=self.dodatkowe_info.value if self.dodatkowe_info.value else "Brak", inline=False)
        
        embed.set_footer(text="System 112 • CrystalRP")

        # Wysyłanie embeda na ten sam kanał (lub możesz podmienić ID kanału dyspozytorni)
        await interaction.channel.send(embed=embed)
        
        # Informacja zwrotna dla gracza, że zgłoszenie zostało wysłane
        await interaction.response.send_message("✅ Twoje zgłoszenie 112 zostało przyjęte i przekazane służbom!", ephemeral=True)

# Komenda /112 wywołująca formularz
@bot.tree.command(name="112", description="Zgłoś nagły przypadek do służb ratunkowych")
async def cmd_112(interaction: discord.Interaction):
    await interaction.response.send_modal(Zgłoszenie112Modal())

# ===========================================================
# 7. RYBY
# ===========================================================

import discord
from discord import app_commands

ZARZAD_ROLE_ID = 123456789012345678  # <-- Pamiętaj o wpisaniu ID roli zarządu

class RybyModal(discord.ui.Modal, title="🐟 Sprzedaż Ryb — ER:LC"):
    kwota = discord.ui.TextInput(
        label="Kwota z gry (np. 500)",
        placeholder="Wpisz kwotę z gry...",
        style=discord.TextStyle.short,
        required=True
    )
    zdjecie_info = discord.ui.TextInput(
        label="Link do screena z datą i godziną",
        placeholder="Wklej link do zdjęcia",
        style=discord.TextStyle.short,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Przeliczamy 50% z podanej kwoty
        try:
            raw_kwota = float(self.kwota.value.replace(",", "."))
            payout = raw_kwota * 0.5
            # Jeśli wynik nie ma części dziesiętnej, zróbmy z niego liczbę całkowitą dla ładnego wyglądu
            if payout.is_integer():
                payout = int(payout)
            if raw_kwota.is_integer():
                raw_kwota = int(raw_kwota)
        except ValueError:
            await interaction.response.send_message("❌ Podana kwota musi być liczbą (np. 500)!", ephemeral=True)
            return

        view = RybyView()

        embed = discord.Embed(
            title="🐟 Nowa Oferta — Rybki",
            color=discord.Color.blue()
        )
        embed.add_field(name="💰 Zgłoszona kwota", value=f"{raw_kwota} zł", inline=True)
        embed.add_field(name="💸 Do wypłaty (50%)", value=f"{payout} zł", inline=True)
        embed.add_field(name="🆔 ID DC", value=str(interaction.user.id), inline=True)
        embed.add_field(name="👤 Sprzedający", value=interaction.user.mention, inline=False)
        embed.add_field(name="📸 Zdjęcie / Dowód", value=self.zdjecie_info.value, inline=False)
        
        embed.set_footer(text="System Ryb • ER:LC")

        await interaction.channel.send(embed=embed, view=view)
        await interaction.response.send_message("✅ Twoja oferta ryb została wysłana do akceptacji przez zarząd!", ephemeral=True)

class RybyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Nadaj Kasę (50%)", style=discord.ButtonStyle.green, emoji="💸")
    async def nadaj_kase(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(ZARZAD_ROLE_ID)
        if not role or role not in interaction.user.roles:
            await interaction.response.send_message("❌ Nie masz uprawnień (roli zarządu), aby to zatwierdzić!", ephemeral=True)
            return

        for child in self.children:
            child.disabled = True

        embed = interaction.message.embeds[0]
        embed.color = discord.Color.green()
        embed.set_footer(text=f"Zatwierdzone i wypłacone przez {interaction.user.display_name}")

        await interaction.message.edit(embed=embed, view=self)
        await interaction.response.send_message(f"✅ Oferta zatwierdzona przez {interaction.user.mention}!", ephemeral=False)

    @discord.ui.button(label="Odrzuć", style=discord.ButtonStyle.red, emoji="✖️")
    async def odrzuc(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(ZARZAD_ROLE_ID)
        if not role or role not in interaction.user.roles:
            await interaction.response.send_message("❌ Nie masz uprawnień (roli zarządu), aby to odrzucić!", ephemeral=True)
            return

        for child in self.children:
            child.disabled = True

        embed = interaction.message.embeds[0]
        embed.color = discord.Color.red()
        embed.set_footer(text=f"Odrzucone przez {interaction.user.display_name}")

        await interaction.message.edit(embed=embed, view=self)
        await interaction.response.send_message(f"❌ Oferta została odrzucona.", ephemeral=False)

@bot.tree.command(name="ryby", description="Zgłoś złowione ryby do wyceny i wypłaty 50%")
async def cmd_ryby(interaction: discord.Interaction):
    await interaction.response.send_modal(RybyModal())

# ==========================================
# URUCHOMIENIE BOTA
# ==========================================
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
