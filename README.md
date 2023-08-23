# Monte Carlo

Eine Sammlung von Python-Skripten mit [Monte Carlo Simulationen](https://de.wikipedia.org/wiki/Monte-Carlo-Simulation):

>Monte-Carlo-Simulation (auch MC-Simulation oder Monte-Carlo-Studie) ist ein Verfahren aus der Stochastik bzw. Wahrscheinlichkeitstheorie, bei dem wiederholt Zufallsstichproben einer Verteilung mithilfe von Zufallsexperimenten gezogen werden.
>
>\[...\] Die Zufallsexperimente können entweder – etwa durch Würfeln – real durchgeführt werden oder in Computerberechnungen mittels Monte-Carlo-Algorithmen.

## Craps (mccraps.py)

Eine (noch unvollständige) Simulation des Würfelspiels [Craps](https://de.wikipedia.org/wiki/Craps).“

## Sankt-Petersburg-Paradoxon (mcpeter.py)

Eine Simulation des [Sankt-Petersburg-Paradoxon](https://de.wikipedia.org/wiki/Sankt-Petersburg-Paradoxon), auch bekannt als _Sankt-Petersburg-Lotterie_:

>In einem Glücksspiel, für das eine Teilnahmegebühr verlangt wird, wird eine faire Münze so lange geworfen, bis zum ersten Mal „Kopf“ fällt. Dies beendet das Spiel. Der Gewinn richtet sich nach der Anzahl der Münzwürfe insgesamt. War es nur einer, dann erhält der Spieler 1 Euro. Bei zwei Würfen (also einmal „Zahl“, einmal „Kopf“) gibt es 2 Euro, bei drei Würfen 4 Euro, bei vier Würfen 8 Euro und bei jedem weiteren Wurf verdoppelt sich der Betrag.

Das Paradoxon ergibt sich daraus, dass einerseits der Erwartungswert (d.h. der Gewinn) _unendlich_ ist, weswegen man als rationaler Spieler theoretisch jede beliebig hohe Teilnahmegebühr bezahlen sollte.
Andererseits ist die Wahrscheinlichkeit, höhere Summen zu gewinnen, recht klein, was in einem realen Spiel hohe Einsätze nicht rechtfertigen würde:

| Sequenz _(K ~ Kopf; Z ~ Zahl)_ | Gewinn | Wahrscheinlichkeit |
|--------------------------------|--------|--------------------|
| K                              | 1 €    | 1/2 = 50%          |
| Z-K                            | 2 €    | 1/4 = 25%          |
| Z-Z-K                          | 4 €    | 1/8 = 12,5%        |
| Z-Z-Z-K                        | 8 €    | 1/16 = 6,25%       |
| Z-Z-Z-Z-K                      | 16 €   | 1/32 = 3,125%      |
| Z-Z-Z-Z-Z-K                    | 32 €   | 1/64 = 1,5625%     |
| Z-Z-Z-Z-Z-Z-K                  | 64 €   | 1/128 = 0,7812%    |
| Z-Z-Z-Z-Z-Z-Z-K                | 128 €  | 1/256 = 0,3906%    |
| Z-Z-Z-Z-Z-Z-Z-Z-K              | 256 €  | 1/512 = 0,1953%    |
| Z-Z-Z-Z-Z-Z-Z-Z-Z-K            | 512 €  | 1/1024 = 0,0976%   |
| Z-Z-Z-Z-Z-Z-Z-Z-Z-Z-K          | 1024 € | 1/2048 = 0,0488%   |
| Z-Z-Z-Z-Z-Z-Z-Z-Z-Z-Z-K        | 2048 € | 1/4096 = 0,0244%   |

D.h. um 2048 € zu gewinnen, muss elf mal in Folge _Zahl_ geworfen werden, bevor das erste mal _Kopf_ kommen darf.
Das ist nur in einem von 4096 Spielen der Fall, womit die Wahrscheinlichkeit bei 0,000244 (entspricht 0,0244%) liegt.

Da wir aber ehrgeizig sind und viel Zeit mitbringen, stellen wir uns die Frage:

**Wie viele Runden müssten wir spielen, um eine Million Euro zu gewinnen?** [^peter1]

[^peter1]: Im besten Fall reicht natürlich **eine Runde**, bei der mindestens zwanzig mal _Zahl_ am Stück geworfen wird:
$2^{20} > 1.000.000$

Weil wir außerdem pleite sind, leihen wir uns die Einsätze von der Bank.
D.h. unser Startkapital beträgt _0 €_ und wir können - um für jede Runde die Teilnahmegebühr zu bezahlen - beliebig viele Schulden anhäufen.

Beginnen wir mit einer **Teilnahmegebühr von einem Euro**:

```
Teilnahmegebühr:                      1 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                          62,315
Gewinn:                       1,097,339 €
-----------------------------------------
Beste Runde:                    131,072 €	
Niedrigster Kontostand:               0 €

```

Wir mussten also _62.315 Runden_ spielen, um die Million zu knacken.
Der höchste Gewinn in einer Spielrunde betrug _131.072 €_ und unser niedrigster Kontostand lag bei _0 €_, wel wir als Spieler _immer_ mindestens einen Euro gewinnen.

Da aber eine Gebühr von einem Euro für die Bank offensichtlich nicht besonders sinnvoll ist, wollen wir die Gebühr nun auf **zehn Euro** erhöhen:

```
Teilnahmegebühr:                     10 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                          92,999
Gewinn:                       1,004,540 €
-----------------------------------------
Beste Runde:                    524,288 €
Niedrigster Kontostand:             -82 €

```

In dieser Simulation haben wir mit _92.999 Runden_ etwas länger gebraucht und außerdem mussten wir zwischenzeitlich die enorme Schuldenlast von _82 €_ tragen.

Probieren wir es deswegen mal mit **25 €** Teilnahmegebühr:

```
Teilnahmegebühr:                     25 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                           6,252
Gewinn:                       4,112,916 €
-----------------------------------------
Beste Runde:                  4,194,304 €
Niedrigster Kontostand:         -81,363 €

```

Wie wir sehen, ist diese Simulation für uns als Spieler äußerst günstig verlaufen.
Nach nur _6.252 Runden_ haben wir durch einen einzigen Gewinn von _4.194.304 €_[^peter2] unser Ziel weit übertroffen.
Allerdings haben wir es hier an einem Punkt auch schon auf _81.363 €_ Schulden gebracht.

[^peter2]: Entspricht einer Runde, in der 22 mal _Zahl_ geworfen wird, da $log_2 4.194.304 = 22$.

Probieren wir das doch noch mal aus:

```
Teilnahmegebühr:                     25 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                       2,968,123
Gewinn:                       4,422,115 €
-----------------------------------------
Beste Runde:                  8,388,608 €
Niedrigster Kontostand:      -6,743,311 €

```

Hier haben wir mit _2.968.123 Runden_ schon deutlich länger gebraucht.
Das Ergebnis unserer besten Runde haben wir im Vergleich zur letzten Simulation mit _über 8 Millionen Euro_ aber sogar verdoppelt,[^peter3] was bei einem zwischenzeitlichen Kontostand von _fast -7 Millionen Euro_ ganz hilfreich ist.

[^peter3]: Die Anzahl der _Zahl-Würfe_ muss ich jetzt nicht noch einmal vorrechnen, denke ich...

Erhöhen wir die Teilnahmegebühr doch einmal auf **50 €** und schauen, wie lange wir jetzt brauchen:

```
# Simulation 1

Teilnahmegebühr:                     50 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                         308,123
Gewinn:                     124,656,112 €
-----------------------------------------
Beste Runde:                134,217,728 €
Niedrigster Kontostand:      -9,600,244 €


# Simulation 2

Teilnahmegebühr:                     50 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                       1,550,117
Gewinn:                      25,243,300 €
-----------------------------------------
Beste Runde:                 67,108,864 €
Niedrigster Kontostand:     -41,899,598 €


# Simulation 3

Teilnahmegebühr:                     50 €
Gewinnziel:                   1,000,000 €
-----------------------------------------
Runden:                       4,282,948
Gewinn:                      15,889,736 €
-----------------------------------------
Beste Runde:                 134,217,728 €
Niedrigster Kontostand:     -118,327,942 €

```



## Ziegenproblem (mcmonty.py)

Eine Simulation des [Ziegenproblems](https://de.wikipedia.org/wiki/Ziegenproblem), auch bekannt als _Drei-Türen-Problem_ oder _Monty-Hall-Problem_:

>„Nehmen Sie an, Sie wären in einer Spielshow und hätten die Wahl zwischen drei Toren. Hinter einem der Tore ist ein Auto, hinter den anderen sind Ziegen. Sie wählen ein Tor, sagen wir, Tor Nummer 1, und der Showmaster, der weiß, was hinter den Toren ist, öffnet ein anderes Tor, sagen wir, Nummer 3, hinter dem eine Ziege steht. Er fragt Sie nun: ‚Möchten Sie das Tor Nummer 2?‘ Ist es von Vorteil, die Wahl des Tores zu ändern?
