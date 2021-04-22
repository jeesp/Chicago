<h1> Chigago-sovellus </h1>

Sovelluksessa 4 käyttäjää pystyy pelaamaan vastakkain Chicago-korttipeliä. Chicagossa pelataan aluksi 2 kierrosta pokeria ja kierros päätetään tikkiin. Kummankin pokerikierroksen jälkeen pelaajan on mahdollista vaihtaa enintään 4 korttia. Wikipedia: https://fi.wikipedia.org/wiki/Chicago_(korttipeli)

<h3> Python-versio </h3>
Sovelluksen toimintaa on testattu Python-versiolla 3.6.0. Vanhempien Python-versioiden kanssa saattaa esiintyä ongelmia. 

<h3> Dokumentaatio </h3>

[Vaatimusmäärittely](https://github.com/jeesp/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/jeesp/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/jeesp/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

<h3> Asennus </h3>

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

<h3> Sovelluksen käyttö </h3>

1. Käynnistä sovellus:

```bash
poetry run invoke start
```

<h3> Testaus </h3>

1. Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```
2. Tee Pylint-testi seuraavalla komennolla:

```bash
poetry run invoke lint
```

<h4> Lisätietoja </h4>

Graafisessa käyttöliittymässä käytetään MIT-lisenssin kuvia.



