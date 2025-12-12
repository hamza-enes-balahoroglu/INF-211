import random

    
def EnvoyMis(move, rate):
    """
    8.7 Envoy Mis(move, rate)
    İletişim hatası simülasyonu.
    """
    if random.random() < rate:
        return 'D' if move == 'C' else 'C'
    return move

def CoopRate(monarch):
    """
    8.5 CoopRate(monarch)
    Krallığın hafızasındaki (memory) tüm geçmiş hamleleri tarayarak, 
    kendi oynadığı "C" hamlelerinin toplam hamlelere oranını hesaplar.
    """
    total_moves = 0
    c_moves = 0
    
    for opp_name, interactions in monarch["memory"].items():
        for my_move, opp_move in interactions:
            total_moves += 1
            if my_move == 'C':
                c_moves += 1
                
    if total_moves == 0:
        return 0.0

    return round(c_moves / total_moves, 3)

def GeneralTrust(monarch, alpha):
    """
    8.4 General Trust (monarch, alpha)
    """
    current_trust = monarch["trust"]
    current_coop_rate = monarch["coop_rate"]
    
    new_trust = current_trust + alpha * (current_coop_rate - current_trust)
    new_trust = max(0.0, min(1.0, new_trust))
    
    monarch["trust"] = round(new_trust, 3)
    
    return monarch["trust"]

def ContinentData(monarchs, continent):
    """
    8.2 Continent Data (monarchs, continent)
    Kıtasal istatistikleri günceller.
    """
    
    # Önceki sigmayı hafızaya kaydet
    continent["sigma_prev"] = continent["sigma_coop"]
    
    # mean_trust hesaplaması
    total_trust             = sum(m["trust"] for m in monarchs)
    mean_trust              = total_trust / len(monarchs)
    continent["mean_trust"] = round(mean_trust, 3)
    
    # mean_coop hesaplaması
    total_coop              = sum(m["coop_rate"] for m in monarchs)
    mean_coop               = total_coop / len(monarchs)
    continent["mean_coop"]  = round(mean_coop, 3)    
    
    # Sigma Coop (Standart Sapma)
    # sigma = sqrt( (1/N) * sum( (Ci - mean_C)^2 ) )
    variance_sum            = sum((m["coop_rate"]  - mean_coop) ** 2 for m in monarchs)
    sigma_coop              = (variance_sum / len(monarchs)) ** 0.5
    continent["sigma_coop"] = round(sigma_coop, 3)
    pass

def TrustThreshold(continent, beta):
    """
    8.3 Trust Threshold(continent, beta)
    theta_g(t+1) = (1-beta)*theta_g(t) + beta * mean_trust(t)
    """
    current_theta_g = continent["theta_g"]
    mean_trust = continent["mean_trust"]
    
    new_theta_g = (1 - beta) * current_theta_g + beta * mean_trust
    continent["theta_g"] = round(new_theta_g, 3)
    
    return continent["theta_g"]

def Decide(strategy, hist, my_score, opp_score, opp_trust, Continent):
    """
    8.6 Decide
    Hamle belirleme mantığı.
    """
    
    if strategy == "Tit-for-Tat": # Kral Edric
        # İlk yıl C
        if not hist:
            return 'C'
        # Rakibin son hamlesini taklit et
        last_opp_move = hist[-1][1]
        return last_opp_move

    elif strategy == "Always Cooperate": # Kraliçe Seren
        return 'C'
    
    elif strategy == "Always Defect": # Lord Garrick
        return 'D'
    
    elif strategy == "Grudger": # Dük Taren
        # Başta C, bir kere D yerse sonsuza kadar D
        for _, opp_move in hist:
            if opp_move == 'D':
                return 'D'
        return 'C'
    
    elif strategy == "Forgiver": # Prens Kael
        # İlk yıl C
        if not hist:
            return 'C'
        
        last_opp_move = hist[-1][1]
        
        # Son turda ihanet ettiyse
        if last_opp_move == 'D':
            return 'D'
            
        # Rakip 2 tur boyunca üst üste
        # ortaklık oynadıysa affeder.
        if len(hist) >= 2:
            prev_opp_move = hist[-2][1]
            # Henüz güven kazanılmadı. Bir C daha lazım.
            if prev_opp_move == 'D':
                return 'D'
        
        # Eğer (C -> C) ise veya oyun başıysa.
        return 'C'
    
    elif strategy == "Random": # Şövalye Varyn
        # p_c = 0.5
        return 'C' if random.random() < 0.5 else 'D'
    
    elif strategy == "Opportunist": # Kont Roderic
        # İlk yıl C
        if not hist:
            return 'C'
        
        theta_g = Continent["theta_g"]
        
        # r_j(t) > r_i(t) -> Rakip benden çok kazanmışsa
        if opp_trust > theta_g and opp_score > my_score:
            return 'C'
        else:
            return 'D'
    
    elif strategy == "Adaptive": # Bilge Elaria
        # İlk yıl C
        if Continent["sigma_prev"] == None:
            return 'C'
        
        sigma_t = Continent["sigma_coop"]
        sigma_prev = Continent["sigma_prev"]
        delta = 0.05
        
        my_last_move = 'C' # Default
        if hist:
            my_last_move = hist[-1][0]
            
        if sigma_t < (sigma_prev - delta):
            return 'C'
        elif sigma_t > (sigma_prev + delta):
            return 'D'
        else:
            return my_last_move

    return 'C' # Hata durumunda

def PalaceGossip(monarchs, gossip_rate, year, verbose):
    
    if year == 1: return False # İlk yıl dedikodu olmaz
    
    if random.random() < gossip_rate:
        # Rastgele hedef seç
        victim_idx = random.randint(0, len(monarchs)-1)
        victim = monarchs[victim_idx] 
        
        # Sahte hamle oluştur
        fake_move = 'C' if random.random() < 0.5 else 'D'
        
        affected_count = 0
        
        # Tüm Kralların Hafızasını Manipüle Et
        for m in monarchs:
            # Kendini geç.
            if m["name"] == victim["name"]: 
                continue
            
            # Eğer hafızamda bu kurbanla ilgili veri varsa:
            if victim["name"] in m["memory"]:
                interactions = m["memory"][victim["name"]]
                
                if interactions:
                    # Son etkileşimi (Geçen Yıl) çek
                    last_interaction = interactions[-1]
                    
                    # Tuple immutable (değiştirilemez) olduğu için yenisini yap
                    # (BenimHamlem, GörünenHamle) -> (BenimHamlem, SAHTE_HAMLE)
                    new_interaction = (last_interaction[0], fake_move)
                    
                    # Hafızaya geri yaz (Overwrite)
                    interactions[-1] = new_interaction
                    affected_count += 1
        
        if verbose:
            print(f"[GOSSIP {year}] {victim['name']} perceived as '{fake_move}' by {affected_count} others")
    pass

def Diplomat(monarchs, theta_trust, wt, wr, p_gate, verbose):
    """
    8.10 Diplomat
    Yeni ittifaklar kurar.
    """
    #___________ADIM 1: Aday Çiftleri Belirle (Scanning)_______________
    candidates = [] # (index_i, index_j, Utility)
    
    # Tüm kombinasyonlar (i < j ile çift tekrarını önlüyoruz)
    for i in range(len(monarchs)):
        for j in range(i + 1, len(monarchs)):
            m1 = monarchs[i]
            m2 = monarchs[j]
            
            # Başkasıyla ittifaktaysa
            if m1["ally"] is not None or m2["ally"] is not None:
                continue
            
            # İkisinin de güveni theta_trust'tan yüksek olmalı 
            if m1["trust"] > theta_trust and m2["trust"] > theta_trust:
                
                # Rastgele %20 şans 
                if random.random() < p_gate: 
                    
                    # Skorlama 
                    # U = wt * OrtalamaGüven + wr * Rastgele
                    avg_trust = (m1["trust"] + m2["trust"]) / 2
                    u_score = wt * avg_trust + wr * random.random()
                    
                    candidates.append({
                        "m1_idx": i, 
                        "m2_idx": j, 
                        "score": u_score,
                    })

    # Eğer aday yoksa çık
    if not candidates:
        if verbose:
            print("[DIPLOMAT] No new alliances this year.")
        return []

    # ________________ADIM 2: Tercih Sıralaması Oluştur (Priority List)____________
    # Her kral için, içinde bulunduğu adaylıkları puana göre sıralayacağız.
    preferences = {i: [] for i in range(len(monarchs))}
    
    for cand in candidates:
        i, j = cand["m1_idx"], cand["m2_idx"]
        # i kralı için j bir adaydır, j kralı için i bir adaydır.
        preferences[i].append((j, cand["score"]))
        preferences[j].append((i, cand["score"]))
        
    # Puanlara göre sırala.
    for k in preferences:
        preferences[k].sort(key=lambda x: x[1], reverse=True)
        # Sadece index'leri sakla.
        preferences[k] = [x[0] for x in preferences[k]]

    # ______________ADIM 3: Karşılıklı Eşleşme ___________________________
    
    new_alliances = []
    matched_indices = set() # Eşlenmişler için alan ayır.
    
    # En uzun listenin boyunu bul
    max_rank = max((len(p) for p in preferences.values()), default=0)
    
    for k in range(max_rank):
        # k. sıradaki olası eşleşmeleri tara
        for i in range(len(monarchs)):
            
            # Bu adam zaten eşleştiyse veya listesi kısaysa geç
            if i in matched_indices: continue
            if k >= len(preferences[i]): continue
            
            # i kralının k. sırasındaki tercihi (target_idx)
            target_idx = preferences[i][k] 
            
            # O hedef eşleşti mi
            if target_idx in matched_indices: continue
            
            # Hedef kralın listesinde i kralı var mı.
            # Yoksa geç.
            if i not in preferences[target_idx]:
                continue
            
            rank_of_i = preferences[target_idx].index(i)
            
            # İki listede de krallar aynı sırada mı.
            # Eğer aynıysa anlaşma yap.
            if rank_of_i == k:
                # EŞLEŞME BAŞARILI
                m1 = monarchs[i]
                m2 = monarchs[target_idx]
                
                # Parametreleri güncelle
                m1["ally"] = m2["name"]
                m1["ally_years"] = 5  # 5 yıl ittifak süresi
                m2["ally"] = m1["name"]
                m2["ally_years"] = 5
                
                # Eşlenenler lisetesine ekle
                matched_indices.add(i)
                matched_indices.add(target_idx)
                
                new_alliances.append((m1["name"], m2["name"]))

    # ______________________ 4. Ekrana Yaz _______________________
    if verbose:
        if new_alliances:
            print(f"[DIPLOMAT] New alliances formed: {new_alliances}")
        else:
            print("[DIPLOMAT] No new alliances this year.")
            
    return new_alliances

def Council(mon1, mon2, Monarchs, Continent, envoy_MisRate, verbose):
    """
    8.11 Council
    İki kralı karşılaştırır, hamleleri belirler, puanlar ve kaydeder.
    """

    # Hafıza verilerini çek
    hist1 = mon1["memory"].get(mon2["name"], [])
    hist2 = mon2["memory"].get(mon1["name"], []) 
    
    move1 = 'C'
    move2 = 'C'
    
    # Hamle Belirleme.
    if mon1["ally"] == mon2["name"]: # İttifak varsa C zorunlu.
        move1, move2 = 'C', 'C'
    else:
        # Karar işlemcilerini çalıştır.
        move1 = Decide(mon1["strategy"], hist1, mon1["score"], mon2["score"], mon2["trust"], Continent)
        move2 = Decide(mon2["strategy"], hist2, mon2["score"], mon1["score"], mon1["trust"], Continent)
    
    # Elçi hataları.
    real_move1 = EnvoyMis(move1, envoy_MisRate)
    real_move2 = EnvoyMis(move2, envoy_MisRate)
    
    # Puanlama Tablosu
    # (C, C) -> 3, 3
    # (C, D) -> 0, 5
    # (D, C) -> 5, 0
    # (D, D) -> 1, 1
    
    score1, score2 = 0, 0
    if real_move1 == 'C' and real_move2 == 'C':
        score1, score2 = 3, 3
    elif real_move1 == 'C' and real_move2 == 'D':
        score1, score2 = 0, 5
    elif real_move1 == 'D' and real_move2 == 'C':
        score1, score2 = 5, 0
    elif real_move1 == 'D' and real_move2 == 'D':
        score1, score2 = 1, 1
        
    # Skorları güncelle.
    mon1["score"] += score1
    mon2["score"] += score2
    
    # Hafıza Güncelleme.   

    if mon2["name"] not in mon1["memory"]: 
        mon1["memory"][mon2["name"]] = []
        pass
    mon1["memory"][mon2["name"]].append((real_move1, real_move2))
    
    if mon1["name"] not in mon2["memory"]:
        mon2["memory"][mon1["name"]] = []
        pass
    mon2["memory"][mon1["name"]].append((real_move2, real_move1))
    
    # Ekrana Yaz.
    if verbose:
        # [COUNCIL] <Kral1> vs <Kral2> -> (<H1>, <H2>) -> +<Puan1>, <Puan2>
        print(f"[COUNCIL] {mon1['name']} vs {mon2['name']} -> ({real_move1}, {real_move2}) -> +{score1}, +{score2}")
        
    return (mon1, mon2, score1, score2)

def AllianceDecay(monarchs, theta_trust, verbose):
    """
    8.9 Alliance Decay
    İttifak süresini azaltır, süresi biten veya güveni düşen ittifakları bozar.
    """
    # işlenmiş çiftleri bir sette tut.
    checked_pairs = set()

    for m in monarchs:
        # İtifak yoksa geç.
        if m["ally"] is None:
            continue
            
        ally_name = m["ally"]
        
        # ("Edric", "Seren") ile ("Seren", "Edric") aynı kabul et.
        pair_key = tuple(sorted((m["name"], ally_name)))
        
        # Kontrol edildiyse atla.
        if pair_key in checked_pairs:
            continue
            
        # Çifti kontrol edildi olarak işaretle.
        checked_pairs.add(pair_key)
        
        ally_obj = None
        for k in monarchs:
            if k["name"] == ally_name:
                ally_obj = k
                break
            
        # Timer'ı Azalt.
        m["ally_years"] -= 1
        ally_obj["ally_years"] -= 1
        
        reason = None
        
        # _________________________ Bozulma Kontrolü __________________________
        
        #  "expired" (süre bitti)
        if m["ally_years"] <= 0:
            reason = "expired"
            
        # "Trust drop" (güven düştü)
        elif m["trust"] < theta_trust or ally_obj["trust"] < theta_trust:
            reason = "trust drop"
            
        # Eğer bir bozulma sebebi varsa RESETLE
        if reason != None:
            if verbose:
                print(f"[DECAY] Alliance between {m['name']} and {ally_obj['name']} dissolved ({reason}).")
                
            # RESETLE
            m["ally"] = None
            m["ally_years"] = 0
            
            ally_obj["ally"] = None
            ally_obj["ally_years"] = 0
            
def main(years, envoy_rate, gossip_rate, verbose):
    
    monarchs =  [
        {"name": "Edric",   "strategy": "Tit-for-Tat",      "trust": 0.60, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Seren",   "strategy": "Always Cooperate", "trust": 0.70, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Garrick", "strategy": "Always Defect",    "trust": 0.30, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Taren",   "strategy": "Grudger",          "trust": 0.50, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Kael",    "strategy": "Forgiver",         "trust": 0.55, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Varyn",   "strategy": "Random",           "trust": 0.45, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Roderic", "strategy": "Opportunist",      "trust": 0.50, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}},
        
        {"name": "Elaria",  "strategy": "Adaptive",         "trust": 0.50, "score": 0, 
         "coop_rate": 0.0, "ally": None, "ally_years": 0, "memory": {}}
    ]
    
    continent =  {
        "year"       : 0,
        "theta_g"    : 0.2,
        "mean_trust" : 0.5125, # (0.6+0.7+0.3+0.5+0.55+0.45+0.5+0.5)/8
        "mean_coop"  : 0.0,
        "sigma_coop" : 0.0,
        "sigma_prev" : None
    }
    
    # Başlangıçta, kaç yıllık bir senaryo olduğunu yaz
    if verbose:
        print(f"Simulation begins: {years} years total")

    theta_trust_alliance = 0.6 # İttifak kurulumu için sabit eşik
    
    # İttifak ağırlıkları
    wt = 0.7
    wr = 0.3
    p_gate = 0.2
    
    alpha = 0.25 # Trust update coefficient
    beta = 0.3   # Theta_g update coefficient
    
    for y in range(1, years + 1):
        continent["year"] = y
        if verbose:
            print(f"===== YEAR {y} =====")
            
        # Dedikodu (Gossip)
        PalaceGossip(monarchs, gossip_rate, y, verbose)
        
        #İttifak Çürümesi (Decay) - Diplomat'tan ÖNCE olmalı!
        AllianceDecay(monarchs, theta_trust_alliance, verbose)
        
        # Diplomasi (Diplomat)
        Diplomat(monarchs, theta_trust_alliance, wt, wr, p_gate, verbose)
        
        for i in range(len(monarchs)):
            for j in range(i + 1, len(monarchs)):
                # Council: Karar ver, Puanla, Hafızaya Yaz
                Council(monarchs[i], monarchs[j], monarchs, continent, envoy_rate, verbose)
        
        # Yıl sonunda istatistikleri güncelle.
        
        # ÖNEMLİ :  Önce CoopRate hesaplanmalı (Çünkü Trust hesabı buna bağlı)
        for m in monarchs:
            m["coop_rate"] = CoopRate(m)
            
        # Trust güncelle
        for m in monarchs:
            GeneralTrust(m, alpha)
            
        # Kıta Verilerini güncelle
        ContinentData(monarchs, continent)
        
        # Global Eşik (Theta_g) güncelle
        TrustThreshold(continent, beta)
        
        # Yıl Sonu Debug Raporu
        if verbose:
            print(f"Avg Cooperation = {continent['mean_coop']}, Avg Trust {continent['mean_trust']}, theta_g = {continent['theta_g']}")
    
    if verbose:
        print("\n--- FINAL RESULTS ---")
        # Skora göre sırala. (Büyükten küçüğe)
        sorted_monarchs = sorted(monarchs, key=lambda x: x["score"], reverse=True)
        
        # Tablo Başlığı
        print(f"{'Name':<10} {'Score':<10} {'Trust':<10} {'CoopRate':<10} {'Strategy'}")
        print("-" * 55)
        
        # Satırlar
        for m in sorted_monarchs:
            print(f"{m['name']:<10} {m['score']:<10} {m['trust']:<10} {m['coop_rate']:<10} {m['strategy']}")

    return (monarchs, continent)

if __name__ == "__main__":
    main(years=50, envoy_rate=0.05, gossip_rate=0.1, verbose=True)