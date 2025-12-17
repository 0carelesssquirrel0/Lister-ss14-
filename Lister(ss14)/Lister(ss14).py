buzzword = 0
def item(name, dec):
    nm = name
    def name():
        print("\n")
        print(nm)
        print(dec)
    name()
    
    


while True:
    buzzword = input("\nWelcome to Lister(ss14) please insert a buzzword ('g' for groups 'e' for end 'p' for problems): ").lower()
    if buzzword == "g":
        print("\nGROUPS:")
        print("\nGUNS:")
        print("gun")
        print("pistol")
        print("revolver")
        print("rifles")
        print("smg")
        print("machine gun")
        print("shotgun")
        print("sniper")
        print("bow")
        print("laser")
        print("pulse")
        print("\nFACTIONS:")
        print("ert")
        print("death squad")
        print("\nMISK:")
        print("ammo")
        print("shotgun shell/shell")
        print("grenade")
        print("improvised")

    elif buzzword == "p":
        print("\nProblems:")
        print("Launcher grenades have no damage value")
        print("missing certin laser weopons (laser shotgun, the new hos gun, disabler, probly other things):")
        print("No explosives exepet launcher grenades(this is because theres no damage values on wiki)")
        print("No improvised shotgun shell")
        print("//NON WEOPONS WILL COME LATER, MORE GROUPS LIKE SEC, TRATOR, ETC WILL COME LATER//")
    elif buzzword == "e":
        print("\nThank you for using Lister... By By\nCredits: Careless Squirrel, https://wiki.spacestation14.com/wiki")    
        break
    else:
        #everything else goes here

        if buzzword == "cobra" or buzzword == "gun" or buzzword == "pistol" :
            item("Cobra",".25 caseless, 19 piercing, traitor uplink")
        if buzzword == "mk 58" or buzzword == "gun" or buzzword == "pistol":
            item("Mk 58",".35 auto, 16 piercing, armory")
        if buzzword == "viper" or buzzword == "gun" or buzzword == "pistol":
            item("Viper",".35 auto, 16 peircing, traitor upling")
        if buzzword == "flintlock pistol" or buzzword == "gun" or buzzword == "pistol" or buzzword == "sniper":
            item("Flintlock Pistol",".60 anti-material, 75 piercing 226 structural, Salvge?")

        if buzzword == "deckard" or buzzword == "gun" or buzzword == "pistol" or buzzword == "revolver":
            item("Deckard",".45 magnum, 35 peircing, vault freezer")
        if buzzword == "mateba" or buzzword == "gun" or buzzword == "pistol" or buzzword == "revolver":
            item("Mateba",".45 magnum, 35 peircing, death squad")
        if buzzword == "inspector" or buzzword == "gun" or buzzword == "pistol" or buzzword == "revolver":
            item("Inspector",".45 magnum, 35 peircing, Detective/Detectives Office")
        if buzzword == "pirate revolver" or buzzword == "gun" or buzzword == "pistol" or buzzword == "revolver":
            item("Pirate revolver",".45 magnum, 35 peircing, salvage/?")
        if buzzword == "python" or buzzword == "gun" or buzzword == "pistol" or buzzword == "revolver":
            item("Python",".45 magnum, 35 peircing/true damage?, Traitor uplink")

        if buzzword == "akms" or buzzword == "gun" or buzzword == "rifles":
            item("AKMS",".30 rifle, 19 peircing, Nukie uplink(disabled)")
        if buzzword == "lecter" or buzzword == "gun" or buzzword == "rifles":
            item("Lecter",".20 rifle, 17 peircing, Armory")
        if buzzword == "m-90gl" or buzzword == "gun" or buzzword == "rifles":
            item("M-90gl",".20 rifle, 17 peircing, Disabled")
            
        if buzzword == "atreides" or buzzword == "gun" or buzzword == "smg":
            item("Atreides",".35 auto, 16 peircing, centcom warden room")
        if buzzword == "c-20r" or buzzword == "gun" or buzzword == "smg":
            item("C-20R",".35 auto, 16 peircing, Traitor Uplink")
        if buzzword == "wt550" or buzzword == "gun" or buzzword == "smg":
            item("WT550",".35 auto, 16 peircing, cargo/sometimes armory")
        if buzzword == "drozd" or buzzword == "gun" or buzzword == "smg":
            item("Drozd",".35 auto, 16 peircing, Armory")

        if buzzword == "l6 saw" or buzzword == "gun" or buzzword == "machine gun":
            item("L6 SAW",".30 rifle, 19 peircing, Traitor Uplink")
        if buzzword == "minigun" or buzzword == "gun" or buzzword == "machine gun":
            item("Minigun",".30 rifle, 19 peircing, random weopon spell")

        if buzzword == "bulldog" or buzzword == "gun" or buzzword == "shotgun":
            item("Bulldog","Shotgun shells, depends on shell, Traitor Uplink")
        if buzzword == "double-barreled shotgun" or buzzword == "gun" or buzzword == "shotgun":
            item("Double-Barreled Shotgun","Shotgun shells, depends on shell, bar")
        if buzzword == "enforcer" or buzzword == "gun" or buzzword == "shotgun":
            item("Enforcer","Shotgun shells, depends on shell, Armory/Cargo")
        if buzzword == "kammerer" or buzzword == "gun" or buzzword == "shotgun":
            item("Kammerer","Shotgun shells, depends on shell, Armory")
        if buzzword == "sawed-off shotgun" or buzzword == "gun" or buzzword == "shotgun":
            item("sawed-off shotgun","Shotgun shells, depends on shell, bar")
        if buzzword == "improvised shotgun" or buzzword == "gun" or buzzword == "shotgun" or buzzword == "improvised":
            item("Improvised Shotgun","Shotgun shells, depends on shell, construction")
        
        if buzzword == "shell (.50)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell (.50)","6 pellets, 5 brute each, max 30")
        if buzzword == "shell (.50 beanbag)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell (.50 Beanbag)","1 pellets, 10 brute each, max 10, stamina damage")
        if buzzword == "shell (.50 Flare)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell .50","1 pellets, 14 burn each, 4 stacks of fire")
        if buzzword == "shell (.50 flash)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell (.50 Flash)","6 pellets, 2 brute each, max 12, flashes on hit")
        if buzzword == "shell (.50 incendiary)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell (.50 Incendiary)","6 pellets, 5 burn each, 1 stack of fire")
        if buzzword == "shell (.50 practice)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell (.50 Practice)","6 pellets, 1 brute each, max 6")
        if buzzword == "shell (.50 slug)" or buzzword == "ammo" or buzzword == "shell" or buzzword == "shotgun shell":
            item("Shell (.50 Slug)","4 pellets, 5 brute each, max 20, spreads less than normal")
        
        if buzzword == "improvised bow" or buzzword == "gun" or buzzword == "sniper" or buzzword == "improvised" or buzzword == "bow":
            item("Improvised Bow","Arrows/Plungers, 25 Pierce, construction")
        if buzzword == "hristov" or buzzword == "gun" or buzzword == "sniper":
            item("Hristov",".60 anti-material, 75 Pierce 226 structural, Traitor Uplink")
        if buzzword == "kardashev-mosin" or buzzword == "gun" or buzzword == "sniper" or buzzword == "rifle":
            item("kardashev-mosin",".30 rifle, 19 Pierce, Traitor Uplink")
        if buzzword == "musket" or buzzword == "gun" or buzzword == "sniper":
            item("Musket",".60 anti-material, 75 Pierce 226 structural, ???")
        
        if buzzword == "china-lake" or buzzword == "gun" or buzzword == "grenade":
            item("China-lake","grenade(spesificaly launcher grenades?), depends on grenade, Traitor Uplink")

        if buzzword == "baton grenade" or buzzword == "ammo" or buzzword == "grenade":
            item("Baton Grenade","launcher grenade, stuns //NOTE NO DAMMAGE VALUES HELP FOR ANY LAUNCHER GRENADES//")
        if buzzword == "blast grenade" or buzzword == "ammo" or buzzword == "grenade":
            item("Blast Grenade","launcher grenade, 4 tile radius explosion //NOTE NO DAMMAGE VALUES HELP FOR ANY LAUNCHER GRENADES//")
        if buzzword == "flash grenade" or buzzword == "ammo" or buzzword == "grenade":
            item("Flash Grenade","launcher grenade, flashes //NOTE NO DAMMAGE VALUES HELP FOR ANY LAUNCHER GRENADES//")
        if buzzword == "frag grenade" or buzzword == "ammo" or buzzword == "grenade":
            item("Frag Grenade","launcher grenade, 7 tile  radius //NOTE NO DAMMAGE VALUES HELP FOR ANY LAUNCHER GRENADES//")
        
        if buzzword == "antique laser gun" or buzzword == "gun" or buzzword == "laser" :
            item("Antique Laser Gun"," energy(regens), 17 heat, captains locker")
        if buzzword == "laser cannon" or buzzword == "gun" or buzzword == "laser" :
            item("Laser Cannon"," energy, 28 heat, research")
        if buzzword == "laser gun" or buzzword == "gun" or buzzword == "laser" :
            item("Laser Gun"," energy, 14 heat, armory/cargo")
        if buzzword == "makeshift laser gun" or buzzword == "gun" or buzzword == "laser" :
            item("Makeshift Laser Gun"," energy, 14 heat, research")
        if buzzword == "retro laser gun" or buzzword == "gun" or buzzword == "laser" :
            item("Retro Laser Gun"," energy, 16 heat, cargo")
        
        if buzzword == "pulse carbine" or buzzword == "gun" or buzzword == "laser" or buzzword == "pulse" or buzzword == "ert":
            item("Pulse Carbine"," energy, 35 heat, ERT")
        if buzzword == "pulse pistol" or buzzword == "gun" or buzzword == "laser" or buzzword == "pulse" or buzzword == "ert" or buzzword == "pistol":
            item("Pulse Pistol"," energy, 35 heat, ERT")
        if buzzword == "pulse rifle" or buzzword == "gun" or buzzword == "laser" or buzzword == "pulse" or buzzword == "death squad":
            item("Pulse Rifle"," energy, 35 heat, Death Squad")
        
        if buzzword == "chimp handcannon" or buzzword == "gun" or buzzword == "laser" or buzzword == "pulse" or buzzword == "ERT":
            item("Chimp Handcannon"," anomaly partical cartriges, 5 burn(delta zeta epsilon ) 20 burn(omega), research (omega through a 'upgrade chip' a sydicate item)")
    
        

