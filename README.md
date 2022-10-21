# Animeunity Scraper

Recently I have been learning Italian, so I watched some anime with Italian dub/sub in a site that I came across: 

https://www.animeunity.tv

I am interested to know which anime has both dub and sub versions, so I can compare the two versions. To achieve this task, I decided to scrape all animes on the Italian anime streaming site using Playwright in Python, and output a csv file so I can know which animes that contain the "(ITA)" keyword (dub version) also have a counterpart without this keyword (sub version). 

To run the code, first install the required packages:
```
pip install -r requirements.txt
```
You also have to install the Playwright webdrivers:
```
playwright install
```
Then simply run the code by the command
```
python scrape_animeunity.py
```
After about a minute, the scraping will be finished and you will have a csv file containing the information of all animes available on the site. The code should be easily generalizable to all sites that show further search results by scrolling.

An automatic anime downloader should be easy to write, since the download link is directly available for all episodes. I may do it later. 

Up to 21/10/2022, the following 173 animes series (different seasons and movies/OVAs are considered as separate anime series) have both Italian dub and sub versions:

* 5 cm al secondo
* 7 Seeds
* BASTARD!! Heavy Metal, Dark Fantasy
* Back Street Girls: Gokudolls
* Baki (2018)
* Baki: Dai Raitaisai-hen
* Beastars
* Beastars 2
* Beelzebub
* Black★Rock Shooter (TV)
* Black★★Rock Shooter: Dawn Fall
* Bleach
* Blue Period
* Boku no Hero Academia
* Boku no Hero Academia 2
* Boku no Hero Academia 3
* Boku no Hero Academia 4
* Boku no Hero Academia 5
* Boku no Hero Academia the Movie 3: World Heroes' Mission
* Brand New Animal
* Bright: Samurai Soul
* Bubble
* Cardcaptor Sakura: Clear Card
* Cardcaptor Sakura: Clear Card-hen Prologue - Sakura to Futatsu no Kuma
* Carole & Tuesday
* Castlevania
* Castlevania 2
* Cells at Work Special
* Cells at Work!
* Cells at Work! 2
* Cells at Work! Code Black
* Child of Kamiari Month
* Cutie Honey Universe
* Cyberpunk: Edgerunners
* DNA²
* DNA² OVA
* DanMachi
* DanMachi 2
* DanMachi 2 OVA
* DanMachi 3
* DanMachi Gaiden: Sword Oratoria
* DanMachi OVA
* Death Parade
* Demon Slayer
* Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train
* Detective Conan: Zero no Tea Time
* Dorohedoro
* Dragon Ball Super
* Dragon Ball Super Movie: Broly
* Drifters
* Drifting Dragons
* Drifting Home
* Earwig and the Witch
* Edens Zero
* Evangelion: 3.0+1.0 Thrice Upon a Time
* Fairy Tail
* Fate/Apocrypha
* Fate/EXTRA Last Encore - Illustrias Tendousetsu
* Fate/Extra: Last Encore
* Fate/stay night: Unlimited Blade Works
* Fate/stay night: Unlimited Blade Works 2
* Fire Force
* Fire Force 2
* Full Metal Panic!
* Fullmetal Alchemist: Brotherhood
* Fullmetal Alchemist: The Sacred Star of Milos
* Getter Robo Arc
* Goblin Slayer
* Goblin Slayer: Goblin's Crown
* Godzilla: S.P
* Gokushufudou
* Gokushufudou Part 2
* Great Pretender
* Haikyuu!!
* Haikyuu!! 2
* Haikyuu!! 3
* Haikyuu!!: Lev Genzan!
* Hanma Baki: Son of Ogre
* Hero Mask
* Hero Mask (2019)
* High Score Girl 2
* High Score Girl: Extra Stage
* Highschool Of The Dead
* Hisone to Maso-tan
* Holly e Benji (2018)
* Hunter x Hunter (2011)
* JoJo no Kimyou na Bouken Part 6: Stone Ocean
* JoJo no Kimyou na Bouken Part 6: Stone Ocean Part 2
* Jujutsu Kaisen
* Jujutsu Kaisen 0 Movie
* Kakegurui
* Kakegurui Twin
* Kakegurui××
* Katekyo Hitman Reborn!
* Kengan Ashura
* Kengan Ashura 2
* Kiseijuu: Sei no Kakuritsu
* Kishibe Rohan wa Ugokanai
* Komi Can't Communicate
* Komi Can't Communicate 2
* Koro Sensei Quest!
* Kotarou wa Hitorigurashi
* Koutetsujou no Kabaneri Movie 3: Unato Kessen
* Kujira no Kora wa Sajou ni Utau
* Levius
* Little Witch Academia
* Liz to Aoi Tori
* Lovely★Complex
* Made in Abyss
* Made in Abyss: The Golden City of the Scorching Sun
* Magic Kaito 1412
* Mardock Scramble: The First Compression
* Mawaru Penguindrum
* Mix: Meisei Story
* Nanatsu no Taizai
* Nanatsu no Taizai Movie 2: Hikari ni Norowareshi Mono-tachi
* Nanatsu no Taizai Movie: Tenkuu no Torawarebito
* Nanatsu no Taizai: Fundo no Shinpan
* Nanatsu no Taizai: Imashime no Fukkatsu
* Nanatsu no Taizai: Kamigami no Gekirin
* Nanatsu no Taizai: Seisen no Shirushi
* Naruto
* Naruto Shippuden
* Ni no Kuni
* One Piece
* One Punch Man
* One Punch Man 2
* Ookami Shoujo to Kuro Ouji
* Paranoia Agent
* Pokemon Evolutions
* Pokemon Sole e Luna
* Prison School
* Psycho-Pass
* Ranking of Kings
* Record of Ragnarok
* Romeo x Juliet
* Ryuu no Haisha
* Saiki Kusuo no Ψ-nan: Shidou-hen
* Senza Famiglia
* Shaman King (2021)
* Sirius the Jaeger
* Sono Bisque Doll wa Koi wo Suru
* Soul Eater
* Special A
* Spy x Family
* Steins;Gate
* Steins;Gate 0
* Steins;Gate: Fuka Ryouiki no Déjà vu
* Summertime Render
* Super Crooks
* Suzumiya Haruhi no Yuuutsu
* Sword Art Online
* Sword Art Online Alternative: Gun Gale Online
* Sword Art Online II
* Sword Art Online the Movie: Progressive - Aria of a Starless Night
* Sword Art Online: Alicization
* Sword Art Online: Alicization - War of Underworld
* Sword Art Online: Alicization - War of Underworld 2
* Uchuu Senkan Yamato 2199
* Ultraman 2
* Vampire Knight
* Vampire Knight: Guilty
* Vampire in the Garden
* Vinland Saga
* Violet Evergarden
* Violet Evergarden Movie
* Violet Evergarden Side Story: Eternity and the Auto Memory Doll
* Violet Evergarden Specials
* Voglio mangiare il tuo pancreas
* Yasuke
* Your Name.
* Yu-Gi-Oh! VRAINS
* Zankyou no Terror
