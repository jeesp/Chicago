<h1> Chigago-sovellus </h1>

Sovelluksessa 4 käyttäjää pelaa vastakkain Chicago-korttipeliä. Chicagossa pelataan aluksi 2 kierrosta pokeria ja kierros päätetään tikkiin. Sovelluksessa on noudatettu seuraavia ohjeita:

Wikipedia: https://fi.wikipedia.org/wiki/Chicago_(korttipeli)

Testauksen helpottamiseksi vuorojen välissä ei ole viivettä ja peli on asetettu päättymään 10 pisteeseen. Pelin päättävää pistemäärää voi halutessaan muuttaa src/game_logic/game_actions-tiedostosta App-luokan metodista points_check.
<h3> Python-versio </h3>
Sovelluksen toimintaa on testattu Python-versiolla 3.6.0. Vanhempien Python-versioiden kanssa saattaa esiintyä ongelmia. 

<h3> Linkki Github-releaseen </h3>

[Release](https://github.com/jeesp/ot-harjoitustyo/releases/tag/viikko6)

<h3> Dokumentaatio </h3>

[Vaatimusmäärittely](https://github.com/jeesp/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/jeesp/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/jeesp/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

<h3> Asennus </h3>

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

Ohjeet Poetryn lataamiseen löydät tarvittaessa esimerkiksi [täältä](https://ohjelmistotekniikka-hy.github.io/python/poetry)

2. Alusta tietokanta komennolla:

```bash
poetry run invoke build
```

<h3> Sovelluksen käyttö </h3>

1. Käynnistä sovellus:

```bash
poetry run invoke start
```

<h3> Testaus </h3>

1. Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

2. Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

3. Pylint-tarkistuksen voi suorittaa komennolla:

```bash
poetry run invoke lint
```

<h4> Lisätietoja </h4>

Graafisessa käyttöliittymässä käytetään MIT-lisenssin kuvia.



