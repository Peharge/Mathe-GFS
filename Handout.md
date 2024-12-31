# Handout

# Inhaltsverzeichnis

- [Einleitung](#einleitung)
- [Matrizen](#matrizen)
- [Addition und skalare Multiplikation](#addition-und-skalare-multiplikation)
- [Multiplikation von Matritzen]

---

## Einleitung

## Matrizen

> Eine Allgemeine Matrix ($m × n$ Matrix) besteht aus **Zahlen**, die in **Zeilen** und **Spalten** angeordnet sind. Sie hat $m$ Zeilen und $n$ Spalten. Wenn $m$ und $n$ gleich sind, ist die Matrix quadratisch (vgl. 2. Quadratische Matrix).<br>
>
> $$
>     B = \begin{pmatrix}
>     B_{1,1} & B_{1,2} & \dots  & B_{1,m} \\
>     B_{2,1} & B_{2,2} & \dots  & B_{2,m} \\
>     \vdots  & \vdots  & \ddots & \vdots \\
>    B_{n,1} & B_{n,2} & \dots  & B_{n,m}
>     \end{pmatrix}
> $$
>
> Die Zahlen des Schemas heißen **Elemente der Matrix**.
> Matritzen werden immer mit Großbuchstaben benannt.
> Die Elemente der Matrix werden immer mit einem Doppelindex gekennzeichnet, der die Nummer der Zeile und die der Spalte des Elementes angibt.

### Quadratische Matrix
Bei der Quadratische Matrix, sind die Anzahl der Zeilen gleich der Anzahl der Spalten (also $m = n$). Zum Beispiel eine $2 × 2$ Matrix oder eine $3 × 3$ Matrix.<br>

**$2 × 2$ Beispiel**:

$$
     C = \begin{pmatrix}
     1 & 2 \\
     3 & 4
     \end{pmatrix}
$$

**$3 × 3$ Beispiel**:

$$
     D = \begin{pmatrix}
     1 & 0 & 2 \\
     3 & 1 & 4 \\
     5 & 6 & 1
     \end{pmatrix}
$$

### Hauptdiagonale
In jeder quadratischen Matrix sind die Elemente der Hauptdiagonalen die Zahlen, die von oben links nach unten rechts verlaufen. Zum Beispiel:<br>

**$2 × 2$ Matrix (Hauptdiagonale: $1$ und $1$)**:

$$
     E = \begin{pmatrix}
     \textbf{1} & 3 \\
     5 & \textbf{1}
     \end{pmatrix}
$$

**$3 × 3$ Matrix (Hauptdiagonale: $1$, $1$ und $1$)**:

$$
     F = \begin{pmatrix}
     \textbf{1} & 3 & 4 \\
     2 & \textbf{1} & 6 \\
     7 & 8 & \textbf{1}
     \end{pmatrix}
$$

### Diagonalmatrix
In einer Diagonalmatrix sind alle Elemente außerhalb der Hauptdiagonalen null.<br>

**$2 × 2$ Beispiel**:

$$
     G = \begin{pmatrix}
     1 & 0 \\
     0 & 1
     \end{pmatrix}
$$

**$3 × 3$ Beispiel**:

$$
     H = \begin{pmatrix}
     1 & 0 & 0 \\
     0 & 1 & 0 \\
     0 & 0 & 1
     \end{pmatrix}
$$

### Einheitsmatrix (Identitätsmatrix)
In der Einheitsmatrix sind alle Elemente auf der Hauptdiagonalen $1$ und alle anderen Elemente $0$.<br>

**$2 × 2$ Beispiel**:

$$
     I = \begin{pmatrix}
     1 & 0 \\
     0 & 1
     \end{pmatrix}
$$

**$3 × 3$ Beispiel**:

$$
     J = \begin{pmatrix}
     1 & 0 & 0 \\
     0 & 1 & 0 \\
     0 & 0 & 1
     \end{pmatrix}
$$

### Aufgabe

Gegeben sind die Matratzen 

$$
     A = \begin{pmatrix} 
     -2 & 5 & 1 \\ 
     1 & -1 & 7 
     \end{pmatrix}
$$ 

und 

$$
     B = \begin{pmatrix} 
     8 & 1 \\ 
     -3 & -2 \\ 
     1 & 4 
     \end{pmatrix}
$$

a) Bestimmen Sie den Typ von A und B.<br>
b) Geben Sie die Elemente $a_{12}$, $a_{23}$, $b_{21}$ und $b_{32}$ an.<br>
c) Welche Elemente von A und welche von B haben den Wert 1?<br>

<details>
  <summary>Lösung a) anzeigen</summary>
  
  <br>A ist eine $2 × 3$ Matrix, B eine $3 × 2$ Matrix.
  
</details>
<details>
  <summary>Lösung b) anzeigen</summary>
  
  <br> $a_{12} = 5$, $a_{23} = 7$, $b_{21} = -3$ und $b_{32} = 4$
  
</details>
<details>
  <summary>Lösung c) anzeigen</summary>
  
  <br> $a_{13}$, $a_{21}$, $b_{12}$ und $b_{31}$ an.
  
</details>

## Addition und skalare Multiplikation

> Die Addition von Matrizen funktioniert, wenn sie gleich groß sind (gleich viele Zeilen und Spalten). Man addiert die Zahlen **an der gleichen Stelle**. 

**Beispiel**: Wir haben zwei Matrizen:

$$
     A = \begin{pmatrix}
     1 & 2 \\
     3 & 4
     \end{pmatrix}, \quad
     B = \begin{pmatrix}
     5 & 6 \\
     7 & 8
     \end{pmatrix}
$$

Jetzt addieren wir sie, indem wir die Zahlen an den gleichen Positionen zusammenzählen:

$$
     A + B = \begin{pmatrix}
     1+5 & 2+6 \\
     3+7 & 4+8
     \end{pmatrix}
     = \begin{pmatrix}
     6 & 8 \\
     10 & 12
     \end{pmatrix}
$$

> Kurtzgeasgt: Addiere einfach die Zahlen an der gleichen Stelle!

### 2. Skalare Multiplikation
> Ein **Skalar** ist nur eine einzelne Zahl, zum Beispiel $2$ oder $5$. Wenn wir eine Matrix mit einem Skalar multiplizieren, multiplizieren wir **jede Zahl in der Matrix** mit dieser Zahl.

**Beispiel**: Nimm die Matrix:

$$
     C = \begin{pmatrix}
     1 & 2 \\
     3 & 4
     \end{pmatrix}
$$

Wenn wir diese Matrix mit $3$ multiplizieren, sieht das so aus:

$$
     3 \cdot C = 3 \cdot \begin{pmatrix}
     1 & 2 \\
     3 & 4
     \end{pmatrix}
     = \begin{pmatrix}
     3 \cdot 1 & 3 \cdot 2 \\
     3 \cdot 3 & 3 \cdot 4
     \end{pmatrix}
     = \begin{pmatrix}
     3 & 6 \\
     9 & 12
     \end{pmatrix}
$$

### **Warum ist das nützlich?**
- Matrizen werden in vielen Bereichen verwendet, z. B. um Daten zu speichern (wie Tabellen oder Bilder).
- Mit Addition und skalarer Multiplikation können wir Matrizen einfach verändern, zum Beispiel vergrößern oder Werte zusammenfassen.

### Aufgaben

Gegebn sind die Matritzen

$$
     A = \begin{pmatrix} 
     1 & 3 & 5 \\ 
     2 & 4 & 6 
     \end{pmatrix}
$$ 

$$
     B = \begin{pmatrix} 
     -1 & 2 & 3 \\ 
     0 & 1 & 2 
     \end{pmatrix}
$$ 

$$
     C = \begin{pmatrix} 
     1 & 2 & 3 \\ 
     4 & 5 & 6 \\
     7 & 8 & 9 \\
     \end{pmatrix}
$$ 

a) Prüfen Sie, welche Matritzen Sie addieren können, und berechnen Sie die Summe.<br>
b) Bestimmen Sie die Zahl k, für die gilt: 

$$
     k * C = \begin{pmatrix} 
     3 & 6 & 9 \\ 
     12 & 15 & 18 \\
     21 & 24 & 27 \\
     \end{pmatrix}
$$

<details>
  <summary>Lösung a) anzeigen</summary>

  <br> $k * C =$ | 0  5  8  | | 2  5  8 |<br>

</details>
<details>
  <summary>Lösung b) anzeigen</summary>
  
  <br>$k = 3$<br>
  
</details>

## Multiplikation von Matritzen

### Allgemeine Matrix-Vektor-Multiplikation

> Nehmen wir eine Matrix $A$ der Größe $m \times n$ (also $m$ Zeilen und $n$ Spalten) und einen Vektor $\vec{z}$ der Größe $n \times$ (also $n$ Zeilen und 1 Spalte). Die Multiplikation $A \cdot \vec{z}$ ist nur möglich, wenn die Anzahl der **Spalten von $A$** gleich der Anzahl der **Zeilen von $\vec{z}$** ist.
> 
> **Matrix $A$:**
> 
> $$
>      A = \begin{pmatrix}
>      a_{11} & a_{12} & \dots & a_{1n} \\
>      a_{21} & a_{22} & \dots & a_{2n} \\
>      \vdots & \vdots & \ddots & \vdots \\
>      a_{m1} & a_{m2} & \dots & a_{mn}
>      \end{pmatrix}
> $$
> 
> **Vektor $\vec{z}$:**
> 
> $$
>      \vec{z} = \begin{pmatrix}
>      z_1 \\
>      z_2 \\
>      \vdots \\
>      z_n
>      \end{pmatrix}
> $$

### Rechenschritte der Matrix-Vektor-Multiplikation

1. **Ergebnis-Vektor:**
   Das Ergebnis der Multiplikation $A \cdot \vec{z}$ wird ein Vektor $\vec{y}$ der Größe $m \times 1$ sein (also ein Vektor mit $m$ Zeilen). Dieser Vektor hat die Form:

$$
   \vec{y} = A \cdot \vec{z} = \begin{pmatrix}
   y_1 \\
   y_2 \\
   \vdots \\
   y_m
   \end{pmatrix}
$$

2. **Berechnung der Einträge des Ergebnis-Vektors:**
   Jeder Eintrag $y_i$ im Ergebnis-Vektor $\vec{y}$ wird berechnet, indem die **$i$-te Zeile der Matrix $A$** mit dem **Vektor $\vec{z}$** multipliziert wird.

   Der $i$-te Eintrag $y_i$ wird folgendermaßen berechnet:

$$
   y_i = a_{i1} \cdot z_1 + a_{i2} \cdot z_2 + \dots + a_{in} \cdot z_n
$$

   Das bedeutet, dass Sie die **$i$-te Zeile** der Matrix $A$ mit den **entsprechenden Einträgen** des Vektors $\vec{z}$ multiplizierst und die Ergebnisse addierst.

### Beispiel zur Veranschaulichung

Nehmen wir die Matrix $A$ der Größe $2 \times Z$ und den Vektor $\vec{z}$ der Größe $3 \times 1$:

**Matrix $A$:**

$$
     A = \begin{pmatrix}
     a_{11} & a_{12} & a_{13} \\
     a_{21} & a_{22} & a_{23}
     \end{pmatrix}
$$

**Vektor $\vec{z}$:**

$$
     \vec{z} = \begin{pmatrix}
     z_1 \\
     z_2 \\
     z_3
     \end{pmatrix}
$$

Jetzt berechnen wir das Produkt \( A \cdot \vec{z} \):

#### Berechnung des ersten Eintrags $y_1$

Die **erste Zeile** von $A$ ist $(a_{11}, a_{12}, a_{13})$, und der Vektor $\vec{z}$ ist $(z_1, z_2, z_3)$.

$$
     y_1 = a_{11} \cdot z_1 + a_{12} \cdot z_2 + a_{13} \cdot z_3
$$

#### Berechnung des zweiten Eintrags $y_2$

Die **zweite Zeile** von $A$ ist $(a_{21}, a_{22}, a_{23})$, und der Vektor $\vec{z}$ bleibt $(z_1, z_2, z_3)$.

$$
     y_2 = a_{21} \cdot z_1 + a_{22} \cdot z_2 + a_{23} \cdot z_3
$$

#### Ergebnis-Vektor

Das Ergebnis der Matrix-Vektor-Multiplikation ist der Vektor $\vec{y}$:

$$
     \vec{y} = A \cdot \vec{z} = \begin{pmatrix}
     y_1 \\
     y_2
     \end{pmatrix}
     = \begin{pmatrix}
     a_{11} \cdot z_1 + a_{12} \cdot z_2 + a_{13} \cdot z_3 \\
     a_{21} \cdot z_1 + a_{22} \cdot z_2 + a_{23} \cdot z_3
     \end{pmatrix}
$$

### Allgemeine Formel der Matrix-Vektor-Multiplikation

> Zusammengefasst, wenn Sie eine Matrix $A$ mit einem Vektor $\vec{z}$ multiplizierst, berechnet sich der Ergebnis-Vektor $\vec{y}$ folgendermaßen:
> 
> $$
>      \vec{y} = A \cdot \vec{z}
> $$
> 
> Dabei gilt:
> 
> $$
>      y_i = \sum_{j=1}^{n} a_{ij} \cdot z_j \quad \text{für jedes} \quad i = 1, 2, \dots, m
> $$
> 
> Das bedeutet, dass du für jede Zeile der Matrix \( A \) die entsprechenden Elemente mit den Vektorelementen multiplizierst und die Produkte addierst, um die einzelnen Einträge im Ergebnis-Vektor zu berechnen.

### Wichtige Merkmale
- **Dimensionen:** Die Anzahl der **Spalten** der Matrix \( A \) muss mit der Anzahl der **Zeilen** des Vektors \( \vec{z} \) übereinstimmen.
- **Ergebnis:** Das Ergebnis der Multiplikation ist ein Vektor, dessen **Anzahl der Zeilen** der Matrix \( A \) entspricht.

### Aufgaben



## Der KI-Held, der nicht wusste, wie er kämpfen sollte

Stellen wir uns vor, in einem Spiel müssen wir die KI eines Helden trainieren, der gegen Monster kämpft. Der Held hat drei Attribute:

1. **Angriffskraft** (wie stark er zuschlagen kann)
2. **Geschwindigkeit** (wie schnell er sich bewegt)
3. **Verteidigung** (wie gut er Schaden abblocken kann)

Die KI lernt nun durch eine **Matrizenoperation**, welche Kombination dieser Attribute am besten ist, um gegen verschiedene Gegner zu kämpfen. Doch unser Held ist ein bisschen verwirrt und die Gewichtungsmatrix für seine Eigenschaften hat ein paar „unschöne“ Werte – als ob er nicht so recht weiß, wie er die Attribute am besten einsetzen soll!

Die Ausgangsdaten für den Charakter sind in einer **Attributmatrix** wie folgt:

$$
     \begin{bmatrix}
     \text{Angriffskraft} & \text{Geschwindigkeit} & \text{Verteidigung} \\
     8 & 5 & 3 \\
     10 & 4 & 2 \\
     \end{bmatrix}
$$

Und die **Gewichtungsmatrix** für den Trainingsalgorithmus sieht so aus:

$$
     \begin{bmatrix}
     1.5 & -0.5 & 0.8 \\
     -0.2 & 1.2 & 0.5 \\
     1.0 & -1.0 & 1.0 \\
     \end{bmatrix}
$$

Die Gewichtungsmatrix besteht aus „Gewichtungen“ (wie viel jeder Wert zählt), wobei jeder Wert für die Interaktion der **Attribute** eines Charakters mit dem **Spielumfeld** steht. Aber Achtung, der Roboter hat hier irgendwie beim Training etwas durcheinandergebracht!

### Aufgabe: **Matrizenmultiplikation: Berechnung der perfekten Attributskombination**

Nun muss die **Attributmatrix** mit der **Gewichtungsmatrix** multipliziert werden, um die optimalen Werte für den Charakter zu berechnen. So lernt die KI, wie der Held sich verhalten soll, um gegen Monster zu kämpfen.

Wir berechnen das durch **Matrixmultiplikation**:

$$
    \begin{bmatrix}
    8 & 5 & 3 \\
    10 & 4 & 2 \\
    \end{bmatrix}
    \cdot
    \begin{bmatrix}
    1.5 & -0.5 & 0.8 \\
    -0.2 & 1.2 & 0.5 \\
    1.0 & -1.0 & 1.0 \\
    \end{bmatrix}
    =
    \begin{bmatrix}
    8 \cdot 1.5 + 5 \cdot (-0.2) + 3 \cdot 1.0 & 8 \cdot (-0.5) + 5 \cdot 1.2 + 3 \cdot (-1.0) & 8 \cdot 0.8 + 5 \cdot 0.5 + 3 \cdot 1.0 \\
    10 \cdot 1.5 + 4 \cdot (-0.2) + 2 \cdot 1.0 & 10 \cdot (-0.5) + 4 \cdot 1.2 + 2 \cdot (-1.0) & 10 \cdot 0.8 + 4 \cdot 0.5 + 2 \cdot 1.0 \\
    \end{bmatrix}
$$

**Berechnung der Ergebnisse:**

1. **Erste Zeile:**
   - $8 * 1.5 + 5 * (-0.2) + 3 * 1.0 = 12 - 1 + 3 = 14$
   - $8 * (-0.5) + 5 * 1.2 + 3 * (-1.0) = -4 + 6 - 3 = -1$
   - $8 * 0.8 + 5 * 0.5 + 3 * 1.0 = 6.4 + 2.5 + 3 = 11.9$

2. **Zweite Zeile:**
   - $10 * 1.5 + 4 * (-0.2) + 2 * 1.0 = 15 - 0.8 + 2 = 16.2$
   - $10 * (-0.5) + 4 * 1.2 + 2 * (-1.0) = -5 + 4.8 - 2 = -2.2$
   - $10 * 0.8 + 4 * 0.5 + 2 * 1.0 = 8 + 2 + 2 = 12$

Die resultierende Matrix (die optimalen **Attributswerte**) sieht so aus:

$$
     \begin{bmatrix}
     14 & -1 & 11.9 \\
     16.2 & -2.2 & 12 \\
     \end{bmatrix}
$$

### Interpretation:
- Der **erste Wert (14)** zeigt, dass der Held eine hohe Angriffskraft hat – er schlägt kräftig zu.
- Der **zweite Wert (-1)** ist jedoch ein bisschen problematisch. **Negative Geschwindigkeit**? Unser Held hat anscheinend beim Training vergessen, wie er sich bewegen soll! Vielleicht ein zu viele „Null-Frames“ im Spiel…
- Der **dritte Wert (11.9)** bedeutet, dass der Held eine ziemlich gute Verteidigung hat, also wird er nicht so schnell verletzt.

### Humorvolle Schlussfolgerung:
Es sieht so aus, als hätte die KI ihren **Helden** mit einer Menge Angriffskraft und einer beeindruckenden Verteidigung ausgestattet – aber vielleicht sollte sie das nächste Mal an der Geschwindigkeit arbeiten. Unser Held könnte ein bisschen zu „gemütlich“ sein, um effektiv zu kämpfen. Doch keine Sorge, mit mehr Training (und vielleicht weniger Pizza in den Pausen) wird er bald verstehen, dass er nicht nur stark, sondern auch schnell sein muss, um das nächste Monster zu besiegen!
