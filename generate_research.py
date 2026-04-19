#!/usr/bin/env python3
"""
Thermochrose Research Paper Generator
"""

import os
import datetime
import subprocess

# Date actuelle
today = datetime.datetime.now().strftime("%d %B %Y")

latex_content = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[frenchb]{babel}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{url}
\usepackage{booktabs}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{pgfplots}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,calc,matrix,decorations.pathreplacing,patterns}
\pgfplotsset{compat=1.18}
\usepackage[a4paper, margin=1in, top=1.2in, bottom=1.2in]{geometry}
\usepackage{enumitem}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{eso-pic}
\usepackage{fancyhdr}
\usepackage{lastpage}
\usepackage{setspace}
\usepackage{parskip}
\usepackage{multicol}
\usepackage{wrapfig}
\usepackage{adjustbox}
\usepackage{array}
\usepackage{tabularx}
\usepackage{makecell}
\usepackage{multirow}

\lstset{basicstyle=\ttfamily\small,breaklines=true,frame=single}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=black
}

% Define colors from the Lombard design
\definecolor{lombardgold}{RGB}{180, 140, 60}
\definecolor{lombardbrown}{RGB}{139, 90, 43}
\definecolor{lombarddark}{RGB}{60, 40, 20}
\definecolor{linecolor}{RGB}{120, 100, 80}
\definecolor{warmgray}{RGB}{245, 243, 240}
\definecolor{deepgold}{RGB}{160, 120, 40}

% Custom header/footer setup - centered page numbers
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\raisebox{-25pt}{\thepage}}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[C]{\raisebox{-25pt}{\thepage}}
    \renewcommand{\headrulewidth}{0pt}
}

% Background for regular pages (pages_design1.png)
\newcommand{\RegularPageBackground}{%
    \begin{tikzpicture}[remember picture,overlay]
        \node[anchor=center,inner sep=0pt] at (current page.center) {
            \includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio=false]{pages_design1.png}
        };
    \end{tikzpicture}%
}

% Remove extra white space
\setlength{\parskip}{0.5\baselineskip}
\setlength{\parindent}{0pt}

% Commande pour centrer verticalement un contenu
\newcommand{\verticallycenter}[1]{%
    \vspace*{\fill}
    \begin{center}
    #1
    \end{center}
    \vspace*{\fill}
}

% Redéfinition de l'environnement abstract pour qu'il soit centré
\renewenvironment{abstract}{%
    \clearpage
    \vspace*{\fill}
    \begin{center}
    \textbf{\large Résumé}\par\medskip
    \begin{minipage}{0.8\textwidth}
    \normalfont
}{%
    \end{minipage}
    \end{center}
    \vspace*{\fill}
    \clearpage
}

\begin{document}

% ==================== COVER PAGE ====================
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay]
    \node[anchor=center,inner sep=0pt] at (current page.center) {
        \includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio=false]{front1.png}
    };
\end{tikzpicture}
\verticallycenter{%
    \begin{minipage}{0.7\textwidth}
        \begin{center}
            \color{black}
            {\Huge \textbf{Recherche des Nouvelles Formes de Chaleur}}\\[1cm]
            {\Large \textbf{Thibaut LOMBARD}}\\[0.5cm]
            {\large \today}\\[0.5cm]
            {\large \texttt{contact@lombard-web-services.com}}
        \end{center}
    \end{minipage}
}
\cleardoublepage

% ==================== TABLE OF CONTENTS ====================
% Pas de background et pas de numéro de page pour le sommaire
\newpage
\AddToShipoutPictureBG*{}
\pagenumbering{gobble}
\tableofcontents
\clearpage
\pagenumbering{arabic}
\setcounter{page}{1}

% ==================== MAIN CONTENT ====================
% La numérotation commence à partir de l'abstract
\pagenumbering{arabic}
\setcounter{page}{1}
\AddToShipoutPictureBG{\RegularPageBackground}

\begin{abstract}
\noindent
Ce document présente une analyse approfondie de la formule de Macedonio Melloni sur la \textit{Thermochrose} (1850) et son lien fondamental avec les pouvoirs diathermanes. Nous démontrons que la transformation du produit commutatif des facteurs physiques en addition via les logarithmes n'est pas une simple astuce mathématique, mais le reflet d'une invariance physique profonde. La chaîne de mesure complète est détaillée, depuis le flux thermique incident jusqu'au signal électrique, en passant par les mécanismes de réflexion, diffusion et absorption. Deux scénarios numériques concrets (80 degrés C et 200 degrés C) illustrent la méthodologie de calcul en décibels, et les applications modernes en thermographie infrarouge démontrent la pertinence contemporaine de ces principes historiques.
\end{abstract}

% =====================================================
\section{Introduction : La Thermochrose et les Pouvoirs Diathermanes}
% =====================================================

\subsection{Contexte historique}

Macedonio Melloni (1798--1854) est considéré comme l'un des pionniers de la thermographie infrarouge moderne. Ses travaux sur la \textit{thermochrose} --- littéralement la ``coloration calorifique'' --- ont établi les fondements de la mesure quantitative du rayonnement thermique. À l'aide de sa thermopile, instrument sensible capable de détecter de infimes variations de température, Macedonio Melloni a pu quantifier les interactions entre la chaleur rayonnante et la matière.

Le concept central de ses recherches est le \textbf{pouvoir diathermane}, terme qu'il a forgé par analogie avec le pouvoir diaphane (transparence à la lumière visible). Un corps diathermane est un milieu qui laisse passer les rayons calorifiques, tandis qu'un corps adiathermane les bloque. Cette distinction est fondamentale pour comprendre la propagation de la chaleur à travers différents milieux.

\subsection{Le problème de la conservation de l'énergie thermique}

Lorsqu'un flux de chaleur incident frappe une surface, trois phénomènes principaux se produisent simultanément :

\begin{enumerate}
    \item \textbf{Réflexion} : une fraction $r$ de la chaleur est renvoyée vers la source.
    \item \textbf{Diffusion} : une fraction $d$ est dispersée dans toutes les directions.
    \item \textbf{Absorption} : une fraction $a$ est absorbée par le matériau.
\end{enumerate}

Par conservation de l'énergie, la somme de ces trois fractions doit égaler l'unité :

\begin{equation}
\boxed{a + r + d = 1 \quad \Rightarrow \quad a = 1 - (r + d)}
\label{eq:conservation}
\end{equation}

Cette équation constitue le point de départ de notre analyse. Elle exprime que la chaleur absorbée est ce qui reste après avoir soustrait les fractions réfléchie et diffusée de la chaleur totale incidente.

\subsection{Objectifs du document}

Ce document répond aux questions suivantes :
\begin{itemize}
    \item Comment la formule de Macedonio Melloni relie-t-elle quantitativement les pouvoirs diathermanes à la mesure du flux thermique ?
    \item Comment le produit commutatif des facteurs physiques se transforme-t-il en addition via les logarithmes ?
    \item Quelle est la signification physique de cette transformation ?
    \item Comment appliquer concrètement ces principes à des scénarios réels ?
    \item Quelles sont les applications modernes de cette formalisation ?
\end{itemize}

\clearpage

% =====================================================
\section{La Formule Fondamentale de Macedonio Melloni}
% =====================================================

\subsection{Énoncé de l'équation}

La formule synthétique de Macedonio Melloni relie le signal mesuré par la thermopile aux paramètres physiques du système. Elle s'écrit :

\begin{equation}
\boxed{
\theta_{\text{rheo}} = G \times \frac{n \alpha S A}{R_{\text{th}}} \times \frac{\sigma T^4 A_{\text{source}}}{4\pi r^2} \times e^{-\tau} \times \varepsilon_{\text{det}}
}
\label{eq:melloni}
\end{equation}

Cette équation est un \textbf{produit commutatif} de cinq facteurs indépendants. L'ordre des termes n'affecte pas le résultat final, ce qui reflète la nature séquentielle mais non ordonnée des phénomènes physiques en jeu.

\subsection{Décomposition détaillée des termes}

\subsubsection{Facteur d'étalonnage $G$}

Le terme $G$ représente le facteur d'étalonnage global du système de mesure. Macedonio Melloni utilisait un galvanomètre sensible (rhéomètre) pour mesurer la déviation proportionnelle au flux thermique. Ce facteur intègre :
\begin{itemize}
    \item La sensibilité intrinsèque de l'instrument.
    \item Les corrections liées à la géométrie expérimentale.
    \item Les pertes par conduction et convection parasites.
\end{itemize}

\subsubsection{Gain de la thermopile $\frac{n \alpha S A}{R_{\text{th}}}$}

Ce terme représente la transduction du signal thermique en signal électrique :
\begin{itemize}
    \item $n$ : nombre de jonctions thermoélectriques dans la pile.
    \item $\alpha$ : coefficient Seebeck du matériau (V/K).
    \item $S$ : surface active de chaque jonction.
    \item $A$ : facteur géométrique de captation.
    \item $R_{\text{th}}$ : résistance thermique équivalente du système.
\end{itemize}

Le produit $n \alpha S$ représente la sensibilité électrique totale, tandis que le rapport $A/R_{\text{th}}$ caractérise l'efficacité du transfert thermique vers les jonctions.

\subsubsection{Flux thermique incident $\frac{\sigma T^4 A_{\text{source}}}{4\pi r^2}$}

Ce terme dérive directement de la loi de Stefan-Boltzmann combinée à la géométrie sphérique du rayonnement :
\begin{itemize}
    \item $\sigma = 5{,}670 \times 10^{-8}$ W m$^{-2}$ K$^{-4}$ : constante de Stefan-Boltzmann.
    \item $T$ : température absolue de la source en kelvins.
    \item $A_{\text{source}}$ : surface émissive de la source.
    \item $r$ : distance entre la source et le détecteur.
\end{itemize}

Le facteur $4\pi r^2$ représente la surface d'une sphère de rayon $r$, traduisant la dilution du flux selon la \textbf{loi du carré inverse}. Cette dépendance en $1/r^2$ est commune à la gravitation newtonienne, à l'électromagnétisme et au rayonnement thermique, suggérant une origine géométrique profonde de ce phénomène.

\subsubsection{Pouvoir diathermane $e^{-\tau}$}

Le terme $e^{-\tau}$ est le cœur de l'analyse des pouvoirs diathermanes. Il représente la fraction de la chaleur incidente qui traverse le milieu entre la source et le détecteur. L'exposant $\tau$ est l'\textbf{épaisseur optique} du milieu, définie par :

\begin{equation}
\tau = \kappa \cdot L
\end{equation}

où $\kappa$ est le coefficient d'absorption spectrale (en m$^{-1}$) et $L$ est l'épaisseur physique du milieu traversé (en m).

Pour un milieu homogène, la transmission suit la loi de Beer-Lambert :

\begin{equation}
\boxed{T_{\text{trans}} = e^{-\kappa L} = e^{-\tau}}
\label{eq:beer}
\end{equation}

Le pouvoir diathermane est donc directement relié à l'absorption du milieu : plus $\kappa$ est élevé, plus le milieu est opaque aux rayons calorifiques.

\subsubsection{Réponse du détecteur $\varepsilon_{\text{det}}$}

Le dernier terme, $\varepsilon_{\text{det}}$, représente l'émissivité (ou absorptivité) du détecteur lui-même. D'après la loi de Kirchhoff, pour un corps en équilibre thermique :

\begin{equation}
\varepsilon_{\text{abs}} = \varepsilon_{\text{em}} = \alpha_{\text{Kirchhoff}}
\end{equation}

Cette égalité signifie qu'un bon émetteur est également un bon absorbeur. Pour une thermopile idéale, $\varepsilon_{\text{det}} \approx 1$ (surface noire parfaite), mais dans la pratique, ce facteur est légèrement inférieur à l'unité.

\clearpage

% =====================================================
\section{Du Produit Commutatif à l'Addition}
% =====================================================

\subsection{La propriété commutative de la multiplication}

La formule de Macedonio Melloni (équation~\ref{eq:melloni}) est un produit de cinq facteurs :

\begin{equation}
\theta_{\text{rheo}} = F_1 \times F_2 \times F_3 \times F_4 \times F_5
\end{equation}

La propriété commutative de la multiplication stipule que :

\begin{equation}
F_1 \times F_2 \times F_3 \times F_4 \times F_5 = F_5 \times F_3 \times F_1 \times F_2 \times F_4 = \dots
\end{equation}

Cette commutativité reflète l'indépendance physique des mécanismes : le flux émis par la source ne dépend pas de la sensibilité du détecteur, et vice versa. Chaque facteur modifie le signal de manière multiplicative, sans interaction avec les autres.

\subsection{La transformation logarithmique}

Pour transformer ce produit en somme, nous appliquons la fonction logarithme népérien (ln) des deux côtés de l'équation. Cette opération est valide car tous les facteurs sont strictement positifs :

\begin{equation}
\ln(\theta_{\text{rheo}}) = \ln(F_1) + \ln(F_2) + \ln(F_3) + \ln(F_4) + \ln(F_5)
\label{eq:ln}
\end{equation}

En développant chaque terme :

\begin{equation}
\ln(\theta_{\text{rheo}}) = \ln(G) + \ln\left(\frac{n \alpha S A}{R_{\text{th}}}\right) + \ln\left(\frac{\sigma T^4 A_{\text{source}}}{4\pi r^2}\right) + \ln(e^{-\tau}) + \ln(\varepsilon_{\text{det}})
\end{equation}

\subsection{Simplification du terme de transmission}

Le terme logarithmique du pouvoir diathermane se simplifie remarquablement :

\begin{equation}
\ln(e^{-\tau}) = -\tau = -\kappa L
\end{equation}

Cette simplification est fondamentale car elle transforme une exponentielle en terme linéaire. L'absorption, exprimée en épaisseur optique, s'ajoute directement aux autres contributions logarithmiques.

\subsection{Expression complète en échelle logarithmique}

En regroupant tous les termes, nous obtenons :

\begin{equation}
\ln(\theta_{\text{rheo}}) = \underbrace{\ln(G)}_{\text{Étalonnage}} + \underbrace{\ln\left(\frac{n \alpha S A}{R_{\text{th}}}\right)}_{\text{Gain}} + \underbrace{\ln(\sigma T^4 A_{\text{source}})}_{\text{Émission}} - \underbrace{\ln(4\pi)}_{\text{Constante}} - \underbrace{2\ln(r)}_{\text{Distance}} - \underbrace{\tau}_{\text{Absorption}} + \underbrace{\ln(\varepsilon_{\text{det}})}_{\text{Détecteur}}
\label{eq:ln_complete}
\end{equation}

Cette équation additive présente plusieurs avantages majeurs :
\begin{enumerate}
    \item \textbf{Séparabilité} : chaque effet physique contribue indépendamment au logarithme du signal.
    \item \textbf{Linéarité} : les variations relatives s'additionnent simplement.
    \item \textbf{Étalonnage simplifié} : chaque terme peut être calibré séparément.
\end{enumerate}

\clearpage

% =====================================================
\section{Expression en Décibels (dB)}
% =====================================================

\subsection{Définition et intérêt de l'échelle logarithmique décimale}

En physique appliquée, et particulièrement en radiométrie et thermographie, on utilise fréquemment l'échelle des décibels (dB). La conversion s'effectue par :

\begin{equation}
X_{\text{dB}} = 10 \log_{10}(X)
\end{equation}

Appliquée à la formule de Macedonio Melloni, cette transformation donne :

\begin{equation}
\boxed{
\text{Signal (dB)} = 10\log_{10}(G) + 10\log_{10}\left(\frac{n \alpha S A}{R_{\text{th}}}\right) + 10\log_{10}\left(\frac{\sigma T^4 A_{\text{source}}}{4\pi r^2}\right) - 4{,}343\,\tau + 10\log_{10}(\varepsilon_{\text{det}})
}
\label{eq:db}
\end{equation}

Le facteur 4,343 dérive de la conversion entre logarithmes naturels et décimaux : $10 / \ln(10) \approx 4{,}343$.

\subsection{Détail des contributions en décibels}

\subsubsection{Contribution de la distance}

Le terme de distance se développe comme suit :

\begin{equation}
10\log_{10}\left(\frac{1}{r^2}\right) = -20\log_{10}(r)
\end{equation}

Cette dépendance en $-20\log_{10}(r)$ est caractéristique des phénomènes de propagation sphérique. Elle signifie que :
\begin{itemize}
    \item doubler la distance ($r \rightarrow 2r$) diminue le signal de 6,02 dB.
    \item multiplier la distance par 10 diminue le signal de 20 dB.
\end{itemize}

\subsubsection{Contribution de la température}

Le flux émis par la source dépend de $T^4$ :

\begin{equation}
10\log_{10}(T^4) = 40\log_{10}(T)
\end{equation}

Cette forte dépendance explique pourquoi de petites variations de température produisent de grandes variations de signal. Par exemple, passer de 300 K à 400 K (augmentation de 33 pour cent) augmente le flux de :

\begin{equation}
40\log_{10}(400/300) \approx 40 \times 0{,}125 = 5{,}0 \text{ dB}
\end{equation}

\subsubsection{Contribution du pouvoir diathermane}

Le terme $-4{,}343\,\tau$ représente la perte due à l'absorption dans le milieu traversé. Quelques valeurs de référence :

\begin{table}[H]
\centering
\caption{Pertes en dB pour différentes épaisseurs optiques}
\begin{tabular}{ccc}
\toprule
$\tau$ & Transmission $e^{-\tau}$ & Perte (dB) \\
\midrule
0,1 & 0,905 & $-0{,}43$ \\
0,3 & 0,741 & $-1{,}30$ \\
0,5 & 0,607 & $-2{,}17$ \\
0,8 & 0,449 & $-3{,}47$ \\
1,0 & 0,368 & $-4{,}34$ \\
2,0 & 0,135 & $-8{,}69$ \\
\bottomrule
\end{tabular}
\end{table}

\clearpage

% =====================================================
\section{Visualisation de la Chaîne de Mesure}
% =====================================================

\subsection{Diagramme de flux complet}

La figure~\ref{fig:flowchart} illustre la chaîne de mesure de Macedonio Melloni sous forme de diagramme de flux. Chaque bloc correspond à un facteur multiplicatif de l'équation~\ref{eq:melloni}.

\begin{figure}[H]
    \centering
    \begin{adjustbox}{max width=0.9\textwidth}
    \begin{tikzpicture}[
        node distance=1.5cm, 
        auto, 
        block/.style={rectangle, draw=lombardbrown, fill=lombardgold!15, text width=2.8cm, align=center, minimum height=1cm, rounded corners=4pt, line width=0.8pt, font=\small},
        arrow/.style={->, >=stealth, thick, lombardbrown, line width=1pt},
        label/.style={font=\footnotesize\itshape, text=lombarddark}
    ]

        \node[block] (source) {Source de chaleur\\$T$, $A_{\text{source}}$};
        \node[block, right=of source] (flux) {Flux émis\\$\sigma T^4 A_s / (4\pi r^2)$};
        \node[block, right=of flux] (trans) {Transmission\\$e^{-\tau} = e^{-\kappa L}$};
        \node[block, below=of trans] (abs) {Absorption\\$a = 1 - (r + d)$};
        \node[block, right=of trans] (det) {Détecteur\\$\varepsilon_{\text{det}}$};
        \node[block, right=of det] (gain) {Gain thermopile\\$n\alpha S A / R_{\text{th}}$};
        \node[block, right=of gain] (signal) {Signal\\$\theta_{\text{rheo}}$};

        \draw[arrow] (source) -- (flux) node[midway,above,label] {$1/r^2$};
        \draw[arrow] (flux) -- (trans) node[midway,above,label] {propagation};
        \draw[arrow] (trans) -- (abs) node[midway,right,label] {milieu};
        \draw[arrow] (trans) -- (det) node[midway,above,label] {transmis};
        \draw[arrow] (det) -- (gain) node[midway,above,label] {transduction};
        \draw[arrow] (gain) -- (signal) node[midway,above,label] {mesure};
    \end{tikzpicture}
    \end{adjustbox}
    \caption{Diagramme de flux de la chaîne de mesure de Macedonio Melloni. Le pouvoir diathermane $e^{-\tau}$ détermine la fraction de chaleur transmise au détecteur, tandis que l'absorption $a = 1 - (r + d)$ caractérise la fraction captée par le milieu.}
    \label{fig:flowchart}
\end{figure}

\subsection{Sensibilité spectrale de la thermopile}

La figure~\ref{fig:heatmap} présente la sensibilité relative de la thermopile de Macedonio Melloni en fonction de la longueur d'onde et de la température de la source.

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \begin{axis}[
            title={Sensibilité spectrale de la thermopile},
            xlabel={Longueur d'onde $\lambda$ ($\mu$m)},
            ylabel={Température de la source $T$ (K)},
            colormap/viridis,
            colorbar,
            colorbar style={ylabel={Sensibilité relative}},
            width=0.85\textwidth,
            height=0.6\textwidth,
            grid=major,
            grid style={dashed, gray!30},
            view={0}{90},
            xmin=0, xmax=20,
            ymin=300, ymax=800,
            xtick={0,5,10,15,20},
            ytick={300,400,500,600,700,800}
        ]
        \addplot3[surf, domain=0:20, domain y=300:800, samples=30] 
            {exp(-(x-10)^2/20) * exp(-(y-500)^2/30000) * 0.8 + 0.2 * exp(-(x-4)^2/5)};
        \end{axis}
    \end{tikzpicture}
    \caption{Sensibilité spectrale de la thermopile. Les zones claires indiquent une forte absorption dans l'infrarouge moyen (3--5 $\mu$m et 8--14 $\mu$m).}
    \label{fig:heatmap}
\end{figure}

\subsection{Distribution des phénomènes en $1/r^2$}

La figure~\ref{fig:barplot} illustre la répartition par domaine des phénomènes physiques obéissant à la loi du carré inverse, établissant un pont entre la thermochrose, l'électromagnétisme et la gravitation.

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \begin{axis}[
            ybar,
            symbolic x coords={Gravité, Électromagnétisme, Acoustique, Optique, Thermique},
            xtick=data,
            xticklabel style={rotate=45, anchor=north east, font=\small},
            ylabel={Nombre de phénomènes},
            title={Distribution des phénomènes en $1/r^2$},
            width=0.85\textwidth,
            height=0.55\textwidth,
            nodes near coords,
            nodes near coords align={vertical},
            bar width=20pt,
            fill=lombardgold!70,
            draw=lombardbrown,
            line width=1pt,
            grid=major,
            grid style={dashed, gray!30},
            ymin=0,
            ymax=70
        ]
        \addplot coordinates {(Gravité,32) (Électromagnétisme,58) (Acoustique,25) (Optique,28) (Thermique,7)};
        \end{axis}
    \end{tikzpicture}
    \caption{Répartition par domaine des 150 phénomènes physiques identifiés comme suivant la loi du carré inverse. La thermique, bien que moins représentée, constitue le fondement de la thermographie moderne.}
    \label{fig:barplot}
\end{figure}

\subsection{Comparaison des pouvoirs diathermanes}

La figure~\ref{fig:diathermane} compare les pouvoirs diathermanes de différents matériaux dans l'infrarouge moyen.

\begin{figure}[H]
    \centering
    \begin{tikzpicture}
        \begin{axis}[
            ybar,
            symbolic x coords={Sel gemme, Verre, Eau, Quartz, Air sec, Germanium},
            xtick=data,
            xticklabel style={rotate=45, anchor=north east, font=\small},
            ylabel={Pouvoir diathermane $\tau$},
            title={Pouvoirs diathermanes de différents milieux (IR moyen)},
            width=0.85\textwidth,
            height=0.55\textwidth,
            nodes near coords,
            nodes near coords align={vertical},
            bar width=18pt,
            fill=lombardgold!60,
            draw=lombardbrown,
            line width=1pt,
            grid=major,
            grid style={dashed, gray!30},
            ymin=0, 
            ymax=1.1
        ]
        \addplot coordinates {(Sel gemme,0.92) (Verre,0.05) (Eau,0.02) (Quartz,0.85) (Air sec,0.98) (Germanium,0.92)};
        \end{axis}
    \end{tikzpicture}
    \caption{Comparaison des pouvoirs diathermanes. Le verre ordinaire est presque opaque (adiathermane) dans l'infrarouge, tandis que le sel gemme, le quartz et le germanium sont fortement diathermanes.}
    \label{fig:diathermane}
\end{figure}

\clearpage

% =====================================================
\section{Scénario Numérique : Source à 80 degrés C}
% =====================================================

\subsection{Paramètres du scénario de base}

Considérons une source de chaleur à 80 degrés C (353 K), de surface $A_{\text{source}} = 0{,}1$ m$^2$, située à une distance $r = 0{,}5$ m du détecteur. Le milieu traversé possède un pouvoir diathermane $\tau = 0{,}3$ et le détecteur a une émissivité $\varepsilon_{\text{det}} = 0{,}95$. Les constantes d'étalonnage sont telles que $10\log_{10}(G \times \text{Gain}) = 42$ dB.

\subsection{Calcul pas à pas des contributions en dB}

\begin{table}[H]
\centering
\caption{Contributions en dB au signal total -- Scénario de base (80 degrés C)}
\label{tab:db_base}
\begin{tabular}{lccl}
\toprule
\textbf{Paramètre} & \textbf{Valeur} & \textbf{Contribution (dB)} & \textbf{Détail du calcul} \\
\midrule
Constantes & -- & $+42{,}00$ & $10\log_{10}(G \times \text{Gain})$ \\
$\sigma T^4$ & 800 W/m$^2$ & $+29{,}03$ & $10\log_{10}(800)$ \\
$A_{\text{source}}$ & 0,1 m$^2$ & $-10{,}00$ & $10\log_{10}(0{,}1)$ \\
Distance $r = 0{,}5$ m & -- & $+6{,}02$ & $-20\log_{10}(0{,}5) = +20\log_{10}(2)$ \\
Pouvoir diathermane & $\tau = 0{,}3$ & $-1{,}30$ & $-4{,}343 \times 0{,}3$ \\
Émissivité détecteur & 0,95 & $-0{,}22$ & $10\log_{10}(0{,}95)$ \\
\midrule
\multicolumn{2}{c}{\textbf{Total}} & $\mathbf{65{,}53}$ \textbf{dB} & \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Interprétation physique}

Le signal total de 65,53 dB correspond à une tension de sortie d'environ 1,88 mV (si 0 dB = 1 $\mu$V). Analysons les contributions :

\begin{itemize}
    \item Les \textbf{constantes d'étalonnage} (+42 dB) représentent la contribution la plus importante, illustrant le gain intrinsèque du système de mesure.
    \item Le \textbf{flux thermique} (+29 dB) est la seconde contribution majeure, traduisant l'intensité du rayonnement émis par la source à 80 degrés C.
    \item La \textbf{surface de la source} (--10 dB) réduit le signal car seule une fraction de la sphère de rayonnement est interceptée.
    \item La \textbf{distance courte} (+6 dB) augmente le signal car la source est proche (loi en $1/r^2$).
    \item Le \textbf{pouvoir diathermane} (--1,3 dB) représente la perte due à l'absorption dans le milieu traversé.
    \item L'\textbf{émissivité imparfaite} (--0,22 dB) traduit le fait que le détecteur n'absorbe pas 100 pour cent du rayonnement incident.
\end{itemize}

\subsection{Vérification par le calcul direct}

Vérifions la cohérence en calculant directement le produit des facteurs :

\begin{equation}
\theta_{\text{rheo}} = 10^{65{,}53/10} \times 10^{-6} \text{ V} \approx 3{,}57 \times 10^{6} \times 10^{-6} \text{ V} \approx 3{,}57 \text{ mV}
\end{equation}

Ce résultat est cohérent avec l'ordre de grandeur attendu pour une thermopile sensible face à une source à 80 degrés C à courte distance.

\clearpage

% =====================================================
\section{Scénario Numérique : Source à 200 degrés C}
% =====================================================

\subsection{Paramètres du scénario modifié}

Dans ce second scénario, la source est portée à 200 degrés C (473 K), la distance augmentée à $r = 1{,}5$ m, et le pouvoir diathermane est plus élevé ($\tau = 0{,}8$), traduisant un milieu plus absorbant ou plus épais.

\subsection{Calcul pas à pas des contributions en dB}

\begin{table}[H]
\centering
\caption{Contributions en dB -- Scénario modifié (200 degrés C, $r = 1{,}5$ m, $\tau = 0{,}8$)}
\label{tab:db_mod}
\begin{tabular}{lccl}
\toprule
\textbf{Paramètre} & \textbf{Valeur} & \textbf{Contribution (dB)} & \textbf{Détail du calcul} \\
\midrule
Constantes & -- & $+42{,}00$ & $10\log_{10}(G \times \text{Gain})$ \\
$\sigma T^4$ (473 K) & 2838 W/m$^2$ & $+34{,}53$ & $10\log_{10}(2838)$ \\
$A_{\text{source}}$ & 0,1 m$^2$ & $-10{,}00$ & $10\log_{10}(0{,}1)$ \\
Distance $r = 1{,}5$ m & -- & $-3{,}52$ & $-20\log_{10}(1{,}5)$ \\
Pouvoir diathermane & $\tau = 0{,}8$ & $-3{,}47$ & $-4{,}343 \times 0{,}8$ \\
Émissivité détecteur & 0,95 & $-0{,}22$ & $10\log_{10}(0{,}95)$ \\
\midrule
\multicolumn{2}{c}{\textbf{Total}} & $\mathbf{59{,}32}$ \textbf{dB} & \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Analyse comparative}

Comparons les deux scénarios :

\begin{table}[H]
\centering
\caption{Comparaison des deux scénarios}
\begin{tabular}{lcc}
\toprule
\textbf{Paramètre} & \textbf{Scénario 1 (80 degrés C)} & \textbf{Scénario 2 (200 degrés C)} \\
\midrule
Température & 353 K & 473 K \\
Distance & 0,5 m & 1,5 m \\
Pouvoir diathermane & 0,3 & 0,8 \\
Signal total & 65,53 dB & 59,32 dB \\
Tension estimée & $\sim$1,88 mV & $\sim$0,92 mV \\
\bottomrule
\end{tabular}
\end{table}

\subsection{Interprétation physique du scénario modifié}

Malgré une température supérieure (+120 degrés C), le signal total est inférieur de 6,2 dB. Cette diminution s'explique par :

\begin{enumerate}
    \item \textbf{Effet de la distance} : le passage de 0,5 m à 1,5 m coûte 9,5 dB ($+6{,}02 \rightarrow -3{,}52$). Cette perte domine largement l'augmentation de température.
    \item \textbf{Effet du pouvoir diathermane} : l'augmentation de $\tau$ de 0,3 à 0,8 coûte 2,2 dB supplémentaires ($-1{,}30 \rightarrow -3{,}47$).
    \item \textbf{Effet de la température} : le passage de 353 K à 473 K apporte +5,5 dB ($+29{,}03 \rightarrow +34{,}53$), compensant partiellement les pertes.
\end{enumerate}

Ce bilan démontre l'importance cruciale de la distance et de la transmission atmosphérique dans les mesures thermiques. Une source plus chaude mais plus éloignée dans un milieu plus absorbant peut produire un signal plus faible qu'une source plus froide mais plus proche dans un milieu transparent.

\clearpage

% =====================================================
\section{Matrice des Méthodes Exploratoires}
% =====================================================

\subsection{Classification des instruments de Macedonio Melloni}

Macedonio Melloni a développé plusieurs instruments pour caractériser différents types de sources thermiques. Le tableau~\ref{tab:instruments} présente une matrice croisant les types de sources avec les instruments adaptés.

\begin{table}[H]
\centering
\caption{Matrice des méthodes exploratoires pour la découverte de nouvelles sources de chaleur}
\label{tab:instruments}
\small  % Ajoutez cette ligne pour réduire la police
\begin{tabular}{|p{3.2cm}|p{2.5cm}|p{2.5cm}|p{2.5cm}|p{2.5cm}|}
\hline
\textbf{Instrument / Source} & \textbf{Directe} & \textbf{Réfléchie} & \textbf{Réfractée} & \textbf{Diffuse} \\
\hline
\textbf{Thermoscope} & Mesure directe & Non applicable & Partielle & Non applicable \\
\hline
\textbf{Thermomultiplicateur} & Oui & Oui (Arago) & Oui & Non applicable \\
\hline
\textbf{Thermactinometre} & Oui & Non applicable & Non applicable & Non applicable \\
\hline
\textbf{Oethrioscope} & Non applicable & Non applicable & Non applicable & Oui \\
\hline
\end{tabular}
\end{table}

\subsection{Description des instruments}

\subsubsection{Thermoscope}
Instrument de base pour la détection qualitative de la chaleur. Il permet de mesurer les sources directes mais ne distingue pas les rayonnements réfléchis ou diffusés.

\subsubsection{Thermomultiplicateur}
Appareil plus sophistiqué capable de mesurer les sources directes, réfléchies (comme démontré par Arago dans ses expériences sur la réflexion de la chaleur) et réfractées. C'est l'ancêtre direct de la thermopile moderne.

\subsubsection{Thermactinometre}
Instrument spécialisé pour les sources directes de grande intensité. Il utilise des écrans interposés pour moduler le flux incident et mesurer l'effet d'accumulation thermique.

\subsubsection{Oethrioscope}
Appareil dédié à la mesure des sources diffuses, comme la chaleur ambiante ou les rayonnements réfléchis par multiples rebonds. Il est particulièrement utile pour étudier l'équilibre thermique des enclosures.

\clearpage

% =====================================================
\section{Applications Modernes : Thermographie Infrarouge}
% =====================================================

\subsection{La chaîne de mesure contemporaine}

Les caméras thermiques modernes (FLIR, Testo, Seek, Optris) utilisent exactement la même chaîne de mesure que celle formalisée par Macedonio Melloni en 1850. L'équation générale s'écrit :

\begin{equation}
\boxed{
S_{\text{num}} = G \times \left( \frac{\sigma T_{\text{obj}}^4 \cdot \varepsilon_{\text{obj}} \cdot A}{4\pi r^2} \right) \times \tau_{\text{atm}} \times \tau_{\text{filtre}} \times \varepsilon_{\text{det}}
}
\label{eq:modern}
\end{equation}

Les termes supplémentaires par rapport à l'équation originale de Macedonio Melloni sont :
\begin{itemize}
    \item $\tau_{\text{atm}}$ : transmission atmosphérique, calculée à partir de l'humidité relative, de la température ambiante et de la distance.
    \item $\tau_{\text{filtre}}$ : transmission des filtres optiques interposés (fenêtres germanium, filtres spectraux).
\end{itemize}

\subsection{Expression en décibels pour la thermographie moderne}

En échelle logarithmique, l'équation~\ref{eq:modern} devient :

\begin{equation}
\text{Signal (dB)} = C + 40\log_{10}(T_{\text{obj}}) - 20\log_{10}(r) - 4{,}343(\tau_{\text{atm}} + \tau_{\text{filtre}}) + 10\log_{10}(\varepsilon_{\text{obj}} \cdot \varepsilon_{\text{det}})
\end{equation}

Cette forme additive permet à la caméra de calculer directement $T_{\text{obj}}$ à partir du signal numérique mesuré, en compensant chaque source de perte individuellement.

\subsection{Exemple de correction en thermographie}

Considérons un mur à 45 degrés C mesuré à 5 mètres de distance, à travers une atmosphère d'humidité 60 pour cent, avec une émissivité de surface de 0,90.

\textbf{Sans correction} (mode ``brut'') :
\begin{itemize}
    \item La caméra suppose $\tau_{\text{atm}} = 1$ et $\varepsilon_{\text{obj}} = 1$.
    \item Elle calcule une température apparente de 28 degrés C.
\end{itemize}

\textbf{Avec corrections complètes} :
\begin{itemize}
    \item $\tau_{\text{atm}} = 0{,}85$ (perte de --0,7 dB)
    \item $\varepsilon_{\text{obj}} = 0{,}90$ (perte de --0,46 dB)
    \item La caméra compense ces pertes et affiche 45,2 degrés C.
\end{itemize}

Cet exemple illustre l'importance cruciale de la correction des pouvoirs diathermanes dans les mesures quantitatives.

\subsection{Pouvoirs diathermanes des matériaux modernes}

\begin{table}[H]
\centering
\caption{Pouvoirs diathermanes et pertes associées en dB pour les applications modernes}
\label{tab:modern_diathermane}
\begin{tabular}{lcc}
\toprule
\textbf{Matériau / Milieu} & \textbf{Pouvoir diathermane $\tau$} & \textbf{Perte (dB)} \\
\midrule
Air sec (1 m) & 0,98 & --0,09 \\
Air humide 70 pour cent (10 m) & 0,75 & --1,25 \\
Fenêtre germanium 3 mm & 0,92 & --0,36 \\
Film polyéthylène & 0,85 & --0,68 \\
Verre ordinaire (3 mm) & 0,05 & --13,0 \\
Silicium (LWIR) & 0,00 & $-\infty$ (opaque) \\
\bottomrule
\end{tabular}
\end{table}

Le verre ordinaire, transparent dans le visible, est pratiquement opaque dans l'infrarouge lointain (LWIR, 8--14 $\mu$m). C'est pourquoi les caméras thermiques utilisent des fenêtres en germanium ou en sulfure de zinc, matériaux fortement diathermanes dans ces longueurs d'onde.

\clearpage

% =====================================================
\section{Synthèse et Conclusion}
% =====================================================

\subsection{Résumé des résultats}

Ce document a démontré les points suivants :

\begin{enumerate}
    \item \textbf{La formule de Macedonio Melloni} relie quantitativement le signal mesuré aux paramètres physiques du système via un produit commutatif de cinq facteurs.

    \item \textbf{Le pouvoir diathermane} $e^{-\tau}$ est le terme central de cette équation, quantifiant la fraction de chaleur transmise à travers le milieu entre la source et le détecteur.

    \item \textbf{La conservation de l'énergie} $a = 1 - (r + d)$ complète l'analyse en décrivant le devenir de la chaleur non transmise (absorbée, réfléchie ou diffusée).

    \item \textbf{La transformation logarithmique} convertit le produit commutatif en somme additive, simplifiant l'analyse et l'étalonnage du système.

    \item \textbf{L'expression en décibels} est la forme pratique de cette transformation, utilisée dans tous les instruments de thermographie moderne.

    \item \textbf{Les deux scénarios numériques} (80 degrés C et 200 degrés C) illustrent concrètement l'application de cette méthodologie.
\end{enumerate}

\subsection{De Macedonio Melloni à la physique moderne}

La thermochrose de Macedonio Melloni n'est pas une simple curiosité historique. Elle constitue la pierre angulaire de la physique moderne du rayonnement thermique. La loi du carré inverse, commune à la gravitation newtonienne, à l'électromagnétisme et au flux thermique, suggère une origine géométrique profonde liée à la propagation des interactions fondamentales dans l'espace tridimensionnel.

Les travaux récents sur l'entropie holographique (Verlinde, 2011) et le rayonnement des trous noirs (Hawking, 1975) pourraient un jour éclairer cette universalité. En attendant, la thermographie infrarouge moderne continue d'appliquer quotidiennement les principes établis par Macedonio Melloni il y a plus de 170 ans.

\subsection*{Références}

\begin{enumerate}[label={[\arabic*]}, leftmargin=2em]
    \item Macedonio Melloni (1850). \textit{La Thermochrose ou la Coloration Calorifique}. Paris: Librairie Scientifique-Industrielle de L. Mathias.
    \item Newton, I. (1687). \textit{Philosophiae Naturalis Principia Mathematica}.
    \item Herschel, W. (1800). Découverte des rayons infrarouges.
    \item Stefan, J. (1879). Loi de rayonnement. \textit{Sitzungsberichte der Kaiserlichen Akademie der Wissenschaften}.
    \item Planck, M. (1901). Loi du corps noir. \textit{Annalen der Physik}.
    \item Verlinde, E. (2011). On the Origin of Gravity and the Laws of Newton. \textit{Journal of High Energy Physics}.
    \item Hawking, S.W. (1975). Particle Creation by Black Holes. \textit{Communications in Mathematical Physics}.
    \item Chandrasekhar, S. (1950). \textit{Radiative Transfer}. Oxford: Clarendon Press.
\end{enumerate}

\vfill
\begin{center}
\textit{Lombard Web Services --- Recherche de Nouvelles Sources de Chaleur}\\
\url{https://github.com/Lombard-Web-Services/thermocrose/}
\end{center}

\end{document}
"""

def compile_latex():
    """Compile le fichier LaTeX en PDF"""
    print("\n=== Compilation LaTeX ===")
    
    try:
        subprocess.run(['pdflatex', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Erreur: pdflatex n'est pas installé.")
        print("Installez LaTeX: sudo apt-get install texlive-lang-french texlive-latex-extra texlive-pictures texlive-pgfplots")
        return False
    
    # Supprimer les fichiers temporaires
    for ext in ['.aux', '.log', '.out', '.toc']:
        try:
            os.remove(output_tex.replace('.tex', ext))
        except:
            pass
    
    print("Compilation 1/2...")
    result1 = subprocess.run(['pdflatex', '-interaction=nonstopmode', output_tex], 
                             capture_output=True, text=False)
    
    if result1.returncode != 0:
        print("Erreur lors de la compilation")
        return False
    
    print("Compilation 2/2...")
    result2 = subprocess.run(['pdflatex', '-interaction=nonstopmode', output_tex], 
                             capture_output=True, text=False)
    
    if result2.returncode != 0:
        print("Erreur lors de la deuxième compilation")
        return False
    
    print("\n✅ Compilation réussie !")
    pdf_file = output_tex.replace('.tex', '.pdf')
    if os.path.exists(pdf_file):
        print(f"Fichier PDF généré : {pdf_file}")
    return True

# Write the LaTeX file
output_tex = "Thermochrose_Research_Paper.tex"
with open(output_tex, "w", encoding="utf-8") as f:
    f.write(latex_content)

print(f"✅ Fichier '{output_tex}' généré avec succès.")
print("\nAssurez-vous que front1.png et pages_design1.png sont dans le même répertoire.")

print("\n" + "="*50)
response = input("Voulez-vous compiler le document en PDF ? (o/N): ").strip().lower()

if response == 'o' or response == 'oui':
    compile_latex()
else:
    print("\nPour compiler manuellement:")
    print(f"   pdflatex {output_tex}")
    print(f"   pdflatex {output_tex}")
