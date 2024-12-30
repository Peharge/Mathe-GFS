# Handout

# Inhaltsverzeichnis

- [Einleitung](#einleitung)
- [Matrizen](#matrizen)
- []


## Matrizen


1. **Allgemeine Matrix ($m × n$ Matrix)**:<br>
Eine Allgemeine Matrix besteht aus **Zahlen**, die in **Zeilen** und **Spalten** angeordnet sind. Sie hat $m$ Zeilen und $n$ Spalten. Wenn $m$ und $n$ gleich sind, ist die Matrix quadratisch (vgl. 2. Quadratische Matrix).

$$
     B = \begin{pmatrix}
     B_{1,1} & B_{1,2} & \dots  & B_{1,m} \\
     B_{2,1} & B_{2,2} & \dots  & B_{2,m} \\
     \vdots  & \vdots  & \ddots & \vdots \\
     B_{n,1} & B_{n,2} & \dots  & B_{n,m}
     \end{pmatrix}
$$

2. **Quadratische Matrix**:<br>
Bei der Quadratische Matrix, sind die Anzahl der Zeilen gleich der Anzahl der Spalten (also $m = n$). Zum Beispiel eine $2 × 2$ Matrix oder eine $3 × 3$ Matrix.

   - **$2 × 2$ Beispiel**:

$$
     C = \begin{pmatrix}
     1 & 2 \\
     3 & 4
     \end{pmatrix}
$$

   - **$3 × 3$ Beispiel**:

$$
     D = \begin{pmatrix}
     1 & 0 & 2 \\
     3 & 1 & 4 \\
     5 & 6 & 1
     \end{pmatrix}
$$

3. **Hauptdiagonale**:<br>
In jeder quadratischen Matrix sind die Elemente der Hauptdiagonalen die Zahlen, die von oben links nach unten rechts verlaufen. Zum Beispiel:
   - **$2 × 2$ Matrix (Hauptdiagonale: $1$ und $1$)**:

$$
     E = \begin{pmatrix}
     \textbf{1} & 3 \\
     5 & \textbf{1}
     \end{pmatrix}
$$

   - **$3 × 3$ Matrix (Hauptdiagonale: $1$, $1$ und $1$)**:

$$
     F = \begin{pmatrix}
     \textbf{1} & 3 & 4 \\
     2 & \textbf{1} & 6 \\
     7 & 8 & \textbf{1}
     \end{pmatrix}
$$

4. **Diagonalmatrix**:<br>
In einer Diagonalmatrix sind alle Elemente außerhalb der Hauptdiagonalen null.
   - **$2 × 2$ Beispiel**:

$$
     G = \begin{pmatrix}
     1 & 0 \\
     0 & 1
     \end{pmatrix}
$$

   - **$3 × 3$ Beispiel**:

$$
     H = \begin{pmatrix}
     1 & 0 & 0 \\
     0 & 1 & 0 \\
     0 & 0 & 1
     \end{pmatrix}
     $$

5. **Einheitsmatrix (Identitätsmatrix)**:<br>
In der Einheitsmatrix sind alle Elemente auf der Hauptdiagonalen $1$ und alle anderen Elemente $0$.
   - **$2 × 2$ Beispiel**:

$$
     I = \begin{pmatrix}
     1 & 0 \\
     0 & 1
     \end{pmatrix}
$$

   - **$3 × 3$ Beispiel**:

$$
     J = \begin{pmatrix}
     1 & 0 & 0 \\
     0 & 1 & 0 \\
     0 & 0 & 1
     \end{pmatrix}
$$

### Aufgabe

Gegeben sind die Matratzen $ A = \begin{pmatrix} -2 & 5 & 1 \\ 1 & -1 & 7 \end{pmatrix}$ und $ B = \begin{pmatrix} 8 & 1 \\ -3 & -2 \\ 1 & 4 \end{pmatrix}$

a) Bestimmen Sie den Typ von A und B.

<details>
  <summary>Lösung a) anzeigen</summary>
  
  A ist eine $2 × 3$ Matrix, B eine $3 × 2$ Matrix.
  
</details>

b) Geben Sie die Elemente $

## **Der KI-Held, der nicht wusste, wie er kämpfen sollte**

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
    8*1.5 + 5*(-0.2) + 3*1.0 & 8*(-0.5) + 5*1.2 + 3*(-1.0) & 8*0.8 + 5*0.5 + 3*1.0 \\
    10*1.5 + 4*(-0.2) + 2*1.0 & 10*(-0.5) + 4*1.2 + 2*(-1.0) & 10*0.8 + 4*0.5 + 2*1.0 \\
    \end{bmatrix}
$$

**Berechnung der Ergebnisse:**

1. **Erste Zeile:**
   - $ 8 * 1.5 + 5 * (-0.2) + 3 * 1.0 = 12 - 1 + 3 = 14 $
   - $ 8 * (-0.5) + 5 * 1.2 + 3 * (-1.0) = -4 + 6 - 3 = -1 $
   - $ 8 * 0.8 + 5 * 0.5 + 3 * 1.0 = 6.4 + 2.5 + 3 = 11.9 $

2. **Zweite Zeile:**
   - $ 10 * 1.5 + 4 * (-0.2) + 2 * 1.0 = 15 - 0.8 + 2 = 16.2 $
   - $ 10 * (-0.5) + 4 * 1.2 + 2 * (-1.0) = -5 + 4.8 - 2 = -2.2 $
   - $ 10 * 0.8 + 4 * 0.5 + 2 * 1.0 = 8 + 2 + 2 = 12 $

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
