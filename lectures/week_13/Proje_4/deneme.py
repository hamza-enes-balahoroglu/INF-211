import random
import sys # Hataları ekrana basmak için (standart kütüphane, yasak değildir)

# --- GLOBAL VERİLER ---
names = ["Auron", "Shai", "Mediv", "Xera", "Eanor", "Rauth"]
specials = [
    "extra_spell", "duplicate_card", "start_with_free_character",
    "extra_spell", "start_with_free_character", "duplicate_card"
]

character_data = [
    ("Rookie Warrior", 1, 3), ("Blade Adept", 2, 2), ("Stone Guardian", 1, 5),
    ("Arcane Duelist", 3, 2), ("Giant Shieldbearer", 1, 6), ("Forest Archer", 2, 3),
    ("Steel Knight", 3, 3), ("Berserker", 4, 2), ("Novice Monk", 1, 4),
    ("Flame Soldier", 3, 1), ("Frost Sentinel", 2, 4), ("Cave Brute", 4, 3),
    ("Samurai Veteran", 3, 4), ("Sand Assassin", 4, 1), ("Battle Cleric", 2, 5),
    ("Thunder Rider", 3, 3), ("Venom Hunter", 3, 2), ("High Paladin", 4, 4)
]
spell_data = [
    ("Fireball", "damage", 5), ("Heal", "heal", 4), ("Lightning", "damage", 7),
    ("Blessing", "heal", 6), ("Frost Spear", "damage", 3), ("Mend Wounds", "heal", 5),
    ("Meteor", "damage", 8), ("Rejuvenate", "heal", 7), ("Arcane Blast", "damage", 4),
    ("Holy Light", "heal", 3), ("Shadow Bolt", "damage", 6), ("Restoration", "heal", 5)
]

# --- SINIFLAR ---

class Card():
    def __init__(self, name:str):
        self.name = name

class CharacterCard(Card):
    def __init__(self, name:str, attack:int, health:int):
        super().__init__(name)
        self.attack = attack
        self.health = health
        
    def __repr__(self):
        return f"{self.name} ({self.attack}/{self.health})"

class SpellCard(Card):
    def __init__(self, name:str, effect:str, value:int):
        super().__init__(name)
        self.effect = effect
        self.value  = value
    
    def __repr__(self):
        return f"{self.name} [{self.effect} {self.value}]"
    
class Deck():
    def __init__(self):        
        self.cards = list()
        for name, attack, health in character_data:
            self.cards.append(CharacterCard(name, attack, health))
        for name, effect, value in spell_data:
            self.cards.append(SpellCard(name, effect, value))
            
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
    
    def copy_cards(self):
        new_list = list()
        for i in self.cards:
            if isinstance(i, CharacterCard):
                new_list.append(CharacterCard(i.name, i.attack, i.health))
            elif isinstance(i, SpellCard):
                new_list.append(SpellCard(i.name, i.effect, i.value))
        return new_list

class Player():
    def __init__(self, name, special):
        self.name = name
        self.special = special
        self.health = 8   
        self.hand = []    
        self.field = []   
        self.points = 0
    
    def clean_dead(self):
        # Canı bitenleri temizle
        living_minions = []
        for card in self.field:
            # Sadece Karakter kartlarını kontrol et, Büyü kartlarını zaten siliyoruz
            if isinstance(card, CharacterCard):
                if card.health > 0:
                    living_minions.append(card)
        self.field = living_minions
        
    def take_damage_on_field(self, amount, logf, attacker_player, attacker_card):
        self.health -= amount
        msg = f"{attacker_player}'s {attacker_card} directly hit {self.name} for {amount} damage (player HP now {self.health})\n"
        logf.write(msg)
        print(msg.strip()) # Konsola da yaz
    
    def heal_field(self, amount, logf, healer_player, spell):
        self.health += amount
        msg = f"{healer_player}'s {spell} healed {self.name} for {amount} (player HP now {self.health})\n"
        logf.write(msg)
        print(msg.strip()) # Konsola da yaz
    
    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.field.append(card)
    
    def apply_special(self):
        if self.special == "extra_spell":
            self.hand.append(SpellCard("Arcane Bolt", "damage", 3))
        elif self.special == "start_with_free_character":
            self.field.append(CharacterCard("Guardian Spirit", 1, 3))
        elif self.special == "duplicate_card":
            if len(self.hand) > 0:
                c = random.choice(self.hand)
                if isinstance(c, CharacterCard):
                    self.hand.append(CharacterCard(c.name, c.attack, c.health))
                elif isinstance(c, SpellCard):
                    self.hand.append(SpellCard(c.name, c.effect, c.value))
                
    def choose_card(self):
        if len(self.hand) > 0:
            return random.choice(self.hand)
        return None

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.logfile = None
        self.create_players()
        self.generate_deck()

    def generate_deck(self): 
        self.deck = Deck() 
        self.deck.shuffle()

    def create_players(self):
        for i in range(len(names)):
            self.add_new_player(Player(names[i], specials[i]))

    def add_new_player(self, player):
        if not player.name in names:
            names.append(player.name)
            specials.append(player.special)
        self.players.append(player)
    
    def deal_hands(self, temp_deck):
        for player in self.players:
            player.hand = []
            chars_needed, spells_needed = 3, 2
            random.shuffle(temp_deck)
            
            # Kart dağıtımı
            for card in temp_deck[:]: 
                if isinstance(card, CharacterCard) and chars_needed > 0:
                    player.hand.append(card)
                    temp_deck.remove(card)
                    chars_needed -= 1
                elif isinstance(card, SpellCard) and spells_needed > 0:
                    player.hand.append(card)
                    temp_deck.remove(card)
                    spells_needed -= 1
            player.apply_special()

    def resolve_spell(self, card, caster: Player, target: Player, logf):
        if card.effect == "heal":
            caster.heal_field(card.value, logf, caster.name, card.name)
        elif card.effect == "damage":
            target.take_damage_on_field(card.value, logf, caster.name, card.name)

    def character_combat(self, attacker: Player, defender: Player, logf):
        for my_minion in attacker.field:
            # SADECE KARAKTER KARTLARI SALDIRABİLİR
            if isinstance(my_minion, CharacterCard):
                if len(defender.field) > 0:
                    enemy_minion = defender.field[0]
                    # Hedefin de karakter olduğundan emin ol
                    if isinstance(enemy_minion, CharacterCard):
                        enemy_minion.health -= my_minion.attack
                        remaining = max(0, enemy_minion.health)
                        msg = f"{attacker.name}'s {my_minion.name} attacked {defender.name}'s {enemy_minion.name} for {my_minion.attack} damage (remaining {remaining})\n"
                        logf.write(msg)
                        print(msg.strip())
                else:
                    defender.take_damage_on_field(my_minion.attack, logf, attacker.name, my_minion.name)
            
            defender.clean_dead()

    def fight(self, p1: Player, p2: Player, logf):
        msg_start = f"Match: {p1.name} vs {p2.name}\n"
        logf.write(msg_start)
        print(f"--- {msg_start.strip()} ---")
        
        logf.write(f"{p1.name} starting hand: {p1.hand}\n")
        logf.write(f"{p2.name} starting hand: {p2.hand}\n")
        
        turn, turn_limit = 0, 10
        while p1.health > 0 and p2.health > 0 and turn < turn_limit:
            # P1 Hamlesi
            c1 = p1.choose_card()
            if c1:
                p1.play_card(c1)
                logf.write(f"{p1.name} played {c1}\n")
                if isinstance(c1, SpellCard):
                    self.resolve_spell(c1, p1, p2, logf)
                    p1.clean_dead() 
            self.character_combat(p1, p2, logf)
            if p2.health <= 0: break

            # P2 Hamlesi
            c2 = p2.choose_card()
            if c2:
                p2.play_card(c2)
                logf.write(f"{p2.name} played {c2}\n")
                if isinstance(c2, SpellCard):
                    self.resolve_spell(c2, p2, p1, logf)
                    p2.clean_dead()
            self.character_combat(p2, p1, logf)
            turn += 1

        if p1.health > 0 and p2.health <= 0:
            logf.write(f"Match Result: {p1.name} WINS\n")
            p1.points += 3; p2.points -= 1
        elif p2.health > 0 and p1.health <= 0:
            logf.write(f"Match Result: {p2.name} WINS\n")
            p2.points += 3; p1.points -= 1
        else:
            logf.write("Match Result: DRAW\n")
            p1.points += 1; p2.points += 1

    def run(self):
        print("Dosya açılıyor: game_log.txt")
        try:
            with open("game_log.txt", "w", encoding="utf-8") as f:
                self.logfile = f
                
                for round_num in range(1, 13):
                    header = f"\n======== ROUND {round_num} ========\n"
                    f.write(header)
                    print(header.strip()) # Konsola yaz
                    
                    for p in self.players:
                        p.health = 8
                        p.field = [] 
                    
                    temp_deck = self.deck.copy_cards()
                    self.deal_hands(temp_deck)
                    
                    random.shuffle(self.players)
                    for i in range(0, len(self.players), 2):
                        if i+1 < len(self.players):
                            self.fight(self.players[i], self.players[i+1], f)
                    
                    # HER TUR SONUNDA KAYDETMEYİ ZORLA (FLUSH)
                    f.flush()
                
                f.write("\n======== FINAL SCORES ========\n")
                print("\n======== FINAL SCORES ========")
                for p in self.players:
                    line = f"{p.name}: {p.points} points\n"
                    f.write(line)
                    print(line.strip())
                    
        except Exception as e:
            print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("KRİTİK HATA OLUŞTU:")
            print(e)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # Hatayı detaylı görmek için traceback bile ekleyebiliriz ama yasak olabilir.
            # Şimdilik hatanın ne olduğunu görmek yeterli.

def main():
    print("--- Oyun Başlatılıyor ---")
    my_game = Game()
    my_game.run()