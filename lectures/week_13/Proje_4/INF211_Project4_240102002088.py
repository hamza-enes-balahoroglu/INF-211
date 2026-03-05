import random

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

class Card():
    def __init__(self, name:str):
        self.name = name
        pass
    
class CharacterCard(Card):
    def __init__(self,name:str, attack:int, health:int):
        super().__init__(name)#inheritance
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
            new_card = CharacterCard(name, attack, health)
            self.cards.append(new_card)
            
        for name, effect, value in spell_data:
            new_card = SpellCard(name, effect, value)
            self.cards.append(new_card)
            
        pass
    
    def shuffle(self):
        random.shuffle(self.cards)
        pass
    
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
    def copy_cards(self):
        new_list = list()
        
        for i in self.cards:
            if isinstance(i, CharacterCard):
                new_card = CharacterCard(i.name, i.attack, i.health)
                
            elif isinstance(i, SpellCard):
                new_card = SpellCard(i.name, i.effect, i.value)
                
            new_list.append(new_card)
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
        living_minions = []
        
        for card in self.field:
            if isinstance(card, CharacterCard):
                if card.health > 0:
                    living_minions.append(card)

        self.field = living_minions
        
    def take_damage_on_field(self, amount, logf, attacker_player, attacker_card):
        self.health -= amount
        log_entry = f"{attacker_player}'s {attacker_card} directly hit {self.name} for {amount} damage (player HP now {self.health})\n"
        
        logf.write(log_entry)
        pass
    
    def heal_field(self, amount, logf, healer_player, spell):
        self.health += amount
        log_entry = f"{healer_player}'s {spell} healed {self.name} for {amount} (player HP now {self.health})\n"
        
        logf.write(log_entry)
        pass
    
    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            
            self.field.append(card)
        pass
    
    def apply_special(self):
        if self.special == "extra_spell":
            bonus_spell = SpellCard("Arcane Bolt", "damage", 3)
            self.hand.append(bonus_spell)
            
        elif self.special == "start_with_free_character":
            bonus_char = CharacterCard("Guardian Spirit", 1, 3)
            self.field.append(bonus_char)
            
        elif self.special == "duplicate_card":
            if len(self.hand) > 0:
                card_to_copy = random.choice(self.hand)
                
                if isinstance(card_to_copy, CharacterCard):
                    new_copy = CharacterCard(card_to_copy.name, card_to_copy.attack, card_to_copy.health)
                elif isinstance(card_to_copy, SpellCard):
                    new_copy = SpellCard(card_to_copy.name, card_to_copy.effect, card_to_copy.value)
                
                self.hand.append(new_copy)
                
    def choose_card(self):
        if len(self.hand) > 0:
            chosen = random.choice(self.hand)
            return chosen
        else:
            return None

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        
        self.players = []
        
        self.logfile = None
        
        self.create_players()
        self.generate_deck()

    def view_deck(self):
        print(f"Deck currently has {len(self.deck.cards)} cards.\n")
        
    def view_players(self):
        print("Current Players:", [p.name for p in self.players], "\n")

    def generate_deck(self): #  ????
        self.deck = Deck() 
        self.deck.shuffle()

    def create_players(self):
        for i in range(len(names)):
            new_player = Player(names[i], specials[i])
            self.add_new_player(new_player)

    def add_new_player(self, player: Player = Player("Deneme", "extra_spell")):
        if not player.name in names:
            names.append(player.name)
            specials.append(player.special)
        self.players.append(player)
        pass
    
    def add_new_card(self):
        new_card_name = "Titan"
        new_card_attack = 10
        new_card_health = 10
        
        new_card = CharacterCard(new_card_name, new_card_attack, new_card_health)
        
        self.deck.cards.append(new_card)
        
        print(f"DEBUG: New card added to deck: {new_card}")
    
    def deal_hands(self, temp_deck):
        
        for player in self.players:
            player
            player.hand   = []
            
            chars_needed  = 3
            spells_needed = 2
            
            random.shuffle(temp_deck)
            
            for card in temp_deck[:]: 
                if isinstance(card, CharacterCard) and chars_needed > 0:
                    player.hand.append(card)
                    temp_deck.remove(card)
                    chars_needed -= 1
                    
                elif isinstance(card, SpellCard) and spells_needed > 0:
                    player.hand.append(card)
                    temp_deck.remove(card) # Desteden sil
                    spells_needed -= 1
                    
            player.apply_special()

    def resolve_spell(self, card, caster: Player, target: Player, logf):

        if card.effect == "heal":
            caster.heal_field(card.value, logf, caster.name, card.name)
            
        elif card.effect == "damage":
            target.take_damage_on_field(card.value, logf, caster.name, card.name)

    def character_combat(self, attacker: Player, defender: Player, logf):
        
        for my_minion in attacker.field:
            
            if not isinstance(my_minion, CharacterCard):
                continue

            # Rakip sahadaki SADECE karakter kartlarını hedef listesine al
            valid_targets = [card for card in defender.field if isinstance(card, CharacterCard)]
            if len(valid_targets) > 0:
                enemy_minion = random.choice(valid_targets)
                
                if isinstance(enemy_minion, CharacterCard):
                    enemy_minion.health -= my_minion.attack
                    remaining_hp_for_log = max(0, enemy_minion.health)
                    logf.write(f"{attacker.name}'s {my_minion.name} attacked {defender.name}'s {enemy_minion.name} for {my_minion.attack} damage (remaining {remaining_hp_for_log})\n")
                
            else:
                # Rakip sahada kimse yok, direkt oyuncuya saldır
                defender.take_damage_on_field(my_minion.attack, logf, attacker.name, my_minion.name)

            # Saldırı sonrası ölüleri temizle
            defender.clean_dead()

    def fight(self, p1: Player, p2: Player, logf):
        
        logf.write(f"Match: {p1.name} vs {p2.name}\n")
        logf.write(f"{p1.name} starting hand: {p1.hand}\n")
        logf.write(f"{p2.name} starting hand: {p2.hand}\n")
        
        turn_limit = 10
        turn = 0
        
        # Biri ölene kadar veya tur bitene kadar savaş
        while p1.health > 0 and p2.health > 0 and turn < turn_limit:
            
            # --- P1 HAMLESİ ---
            card_p1 = p1.choose_card()
            if card_p1:
                p1.play_card(card_p1)
                logf.write(f"{p1.name} played {card_p1}\n")
                
                # Eğer Büyü ise hemen uygula
                if isinstance(card_p1, SpellCard):
                    self.resolve_spell(card_p1, p1, p2, logf)
            
            # P1 Sahadakilerle Saldırır
            self.character_combat(p1, p2, logf)
            
            # Oyun bitti mi kontrol et
            if p2.health <= 0: break

            # --- P2 HAMLESİ ---
            card_p2 = p2.choose_card()
            if card_p2:
                p2.play_card(card_p2)
                logf.write(f"{p2.name} played {card_p2}\n")
                
                if isinstance(card_p2, SpellCard):
                    self.resolve_spell(card_p2, p2, p1, logf)
            
            # P2 Sahadakilerle Saldırır
            self.character_combat(p2, p1, logf)
            
            turn += 1

        if p1.health > 0 and p2.health <= 0:
            logf.write(f"Match Result: {p1.name} WINS\n")
            p1.points += 3
            p2.points -= 1
        elif p2.health > 0 and p1.health <= 0:
            logf.write(f"Match Result: {p2.name} WINS\n")
            p2.points += 3
            p1.points -= 1
        else:
            logf.write("Match Result: DRAW\n")
            p1.points += 1
            p2.points += 1

    def run(self):
        
        self.logfile = open("game_log.txt", "w")
        
        for round_num in range(1, 13):
            self.logfile.write(f"\n======== ROUND {round_num} ========\n")
            
            for p in self.players:
                p.health = 8
                p.field = []
            
            temp_deck = self.deck.copy_cards()
            
            self.deal_hands(temp_deck)
            
            random.shuffle(self.players)
            
            # 3 Maç yap (6 oyuncu var, 2'şerli 3 grup)
            for i in range(0, len(self.players), 2):
                player1 = self.players[i]
                player2 = self.players[i+1]
                
                self.fight(player1, player2, self.logfile)
        
        self.logfile.write("\n======== FINAL SCORES ========\n")
        for p in self.players:
            line = f"{p.name}: {p.points} points\n"
            self.logfile.write(line)
            print(line.strip())
        
        self.logfile.close()

def main():
    
    print("--- Oyun Başlatılıyor ---")
    
    my_game = Game()
    
    print(">>> Simülasyon çalışıyor...")
    my_game.run()
    
    print("--- Oyun Bitti ---")
    print("Sonuçları görmek için 'game_log.txt' dosyasını kontrol et.")
    pass

if __name__ == "__main__":
    main()