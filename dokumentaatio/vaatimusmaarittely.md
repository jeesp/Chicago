# Vaatismusmäärittely
## Sovelluksen tarkoitus
Sovelluksessa 4 käyttäjää pelaa vastakkain Chicago-korttipeliä. Chicagossa pelataan aluksi 2 kierrosta pokeria ja kierros päätetään tikkiin. Sovelluksessa on noudatettu seuraavia ohjeita:

Wikipedia: https://fi.wikipedia.org/wiki/Chicago_(korttipeli)

## Käyttöliittymä
Sovelluksessa käytetään graafista käyttöliittymää. Alkuruudusta on mahdollista aloittaa peli, sekä tarkastella kokonaispistemäärää. Pelin aloituksen jälkeen avautuu ensimmäisenä vuorossa olevan pelaajan pelinäkymä, josta valitaan vaihdettavat kortit. Oikealla ylälaidassa näkyy pistetaulukko, vasemmalla ylhäällä kerrotaan mahdollisista pokeripisteistä. Jokainen pelaaja saa vuorollaan vaihtaa kaksi kertaa niin monta korttia kuin haluaa, sillä kortit eivät lopu pakasta kesken. Toisen vaihdon aikana näkymään ilmestyy blanco-painike, jota klikkaamalla saa aktivoitua blanco-chicagon huutamisen. Tällöin pitää vaihtaa vähintään yksi kortti. Mikäli joku pelaajista huutaa blancon, muut eivät tätä voi enää tehdä ja näytölle ilmestyy ilmoitus blancosta. Toisen pokerikierroksen jälkeen avautuu tikkinäkymä. Mikäli blancoa ei ole huudettu, on ensimmäisellä kierroksella mahdollista huutaa vielä normaali chicago. Vuorossa ensimmäisenä oleva pelaaja asettaa tikkikierroksen aloituskortin ja muiden pelaajien on pelattava tätä samaa maata, mikäli heidän kädestään kyseistä maata löytyy. Tikkikierroksen jälkeen alkaa joko uusi kierros, tai tavoitepistemäärän ylittyessä peli loppuu. Ennen uuden näkymän ilmestymistä näytölle ilmestyy vielä tekstit kierroksen tapahtumista.
## Toiminnallisuus
Sovelluksessa pidetään kirjaa tuloksista ja voittaja on pelaaja, joka pääsee ensimmäisenä 52 pisteeseen. Pelissä on mahdollista pokerikierroksen jälkeen huutaa chicago, jolloin kyseinen pelaaja aloittaa tikkivuoron ja hänen tulee voittaa jokainen tikkikäsi. Chicagon lisäksi pelaajan on mahdollista huutaa blanco-chicago ennen viimeistä vaihtoa, jolloin kyseisen pelaajan tulee vaihtaa vähintään yksi kortti ja tämän jälkeen onnistua normaalissa chicagossa. Jokaisen kierroksen (paitsi chicago-kierroksen) jälkeen lopussa tarkistetaan vielä pokerikäsi, ja paras käsi saa pisteet.
Pisteytys:
Pari: 1p
Kaksi paria: 2p
Kolmoset: 3p
Suora: 4p
Väri: 5p
Täyskäsi: 6p
Neloset: 8p (ja kaikki muut pelaajat tippuvat 0 pisteeseen)
Värisuora: 52p (ja kaikki muut pelajaat tippuvat 0 pisteeseen, peli loppuu)
Tikin lopetus: 5p
Tikin lopetus kakkosella: 10p
Chicago (onnistunut/epäonnistunut): 15/-15
Blanco-chicago (onnistunut/epäonnistunut): 30/-30

## Todo-lista
Sovelluslogiikka
- [x] Pokerin pisteytykset
- [x] Pokerikierrokset/logiikka
- [x] Korttien vaihtaminen
- [x] Tikin logiikka
- [x] Kortin pelaaminen
- [x] Tulostaulu
- [x] Chicago
- [x] Blanco-chicago
- [x] Graafinen käyttöliittymä 1. pokerinäkymä
- [x] Graafinen käyttöliittymä 2. vaihtonäkymä
- [x] Graafinen käyttöliittymä tikkinäkymä
- [ ] Graafinen käyttöliittymä tulostaulu
- [/] Graafisen käyttöliittymän liittäminen osaksi sovellusta
- [x] Graafinen käyttöliittymä alkunäkymä
- [x] Graafinen käyttöliittymä lopetusnäkymä
- [x] Chicago graafisessa käyttöliittymässä
- [x] Blancochicago graafisessa käyttöliittymässä
- [x] Kokonaispistemäärä tietokannasta

