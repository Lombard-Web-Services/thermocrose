# Thermochrose

Analyse de l'ouvrage sur la Thermochrose de Macedonio Melloni (1850) et recherche des moyens d'identification et de caractérisation de la chaleur rayonnante en s'inspirant des instruments de mesure.

---

## Table des matières

1. [Origine du projet](#origine-du-projet)
2. [Parcours de recherche](#parcours-de-recherche)
3. [Sources et références](#sources-et-références)
4. [Structure du repository](#structure-du-repository)
5. [Documentation complète](#documentation-complète)
6. [Méthodologie](#méthodologie)
7. [Résultats clés](#résultats-clés)
8. [Licence](#licence)

---

## Origine du projet

Ce projet est né d'une remarque fondamentale : **la gravité newtonienne n'explique pas la chaleur**. Cette constatation initiale a conduit à une investigation systématique des mécanismes physiques susceptibles de caractériser la nature de la chaleur rayonnante, aboutissant à la redécouverte et à l'analyse approfondie des travaux de Macedonio Melloni (1850) sur la thermochrose.

### La question initiale

La loi de la gravitation universelle de Newton :

$$F = G \frac{m_1 m_2}{r^2}$$

décrit parfaitement l'attraction entre masses mais demeure muette sur la nature de la chaleur. Cette limitation a motivé une recherche alternative s'appuyant sur les lois d'absorption et la caractérisation spectrale du rayonnement thermique.

---

## Parcours de recherche

### Phase 1 : Exploration des mécanismes fondamentaux

La recherche a successivement examiné plusieurs candidats pour expliquer la chaleur :

| Domaine | Conclusion | Référence |
|---------|------------|-----------|
| Gravité newtonienne | N'explique pas la chaleur (force mécanique entre masses) | Newton, 1687 |
| Magnétisme | Perturbé par la chaleur, ne l'explique pas | Curie, 1895 |
| Infrarouges | Vecteur de transfert, pas explication fondamentale | Herschel, 1800 |
| Lois d'absorption | Décrivent le transfert, pas l'origine | Kirchhoff, 1859 |
| **Thermochrose (Melloni)** | **Nature ondulatoire de la chaleur rayonnante** | **Melloni, 1850** |

### Phase 2 : Cartographie de la loi inverse carrée

L'analyse s'est étendue à l'identification de **150 phénomènes physiques** obéissant à la loi inverse carrée $I \propto 1/r^2$, établissant une classification systématique des sources de chaleur et des mécanismes d'émission.

**Base de données :** [Inverse Square Law Phenomenon Database](https://lombard-web-services.github.io/Docs/Inverse_Square_Law_phenomenon_FR.html)

### Phase 3 : Analyse spectrale des mécanismes d'émission

Identification et classification des 13 mécanismes d'émission de lumière/chaleur :

1. Photoluminescence
2. Chimiluminescence
3. Triboluminescence
4. Radioluminescence
5. **Thermoluminescence** (lien direct avec Melloni)
6. **Plasma LTE** (continuum Planck - corps noir)
7. Sonoluminescence
8. Électroluminescence
9. Et 5 autres mécanismes secondaires

---

## Sources et références

### Source primaire

**Melloni, M. (1850).** *La Thermochrose ou la Coloration Calorifique*. Paris: Librairie Scientifique-Industrielle de L. Mathias (Auguste Durand).

Numérisation disponible sur [Austrian Newspapers Online (ANNO), ÖNB](https://data.onb.ac.at/rep/1031DFBB).

### Références historiques clés

| Auteur | Année | Contribution |
|--------|-------|--------------|
| Newton, I. | 1687 | *Philosophiæ Naturalis Principia Mathematica* - Gravitation universelle |
| Herschel, W. | 1800 | Découverte des rayons infrarouges |
| Seebeck, T.J. | 1821 | Effet thermoélectrique (base du thermomultiplicateur) |
| Nobili, L. | 1830 | Perfectionnement de la pile thermoélectrique |
| **Melloni, M.** | **1850** | **Thermochrose - nature ondulatoire de la chaleur** |
| Kirchhoff, G. | 1859 | Loi d'émission-absorption $\alpha_\lambda = \epsilon_\lambda$ |
| Maxwell, J.C. | 1865 | Électromagnétisme et nature ondulatoire de la lumière |
| Stefan, J. | 1879 | Loi de rayonnement $P = \sigma AT^4$ |
| Boltzmann, L. | 1884 | Fondements statistiques de la thermodynamique |
| Planck, M. | 1901 | Loi du corps noir et quantification |
| Einstein, A. | 1905/1924 | Effet photoélectrique et statistique de Bose-Einstein |

### Références modernes

- Chandrasekhar, S. (1950). *Radiative Transfer*. Oxford: Clarendon Press.
- Rybicki, G.B. & Lightman, A.P. (1979). *Radiative Processes in Astrophysics*. New York: Wiley.
- Landau, L.D. & Lifshitz, E.M. (1980). *Statistical Physics*.
- Hawking, S.W. (1974, 1975). Rayonnement des trous noirs.
- Verlinde, E. (2011). Gravité entropique.

---

## Documentation complète

### Document principal

**[melloni_thermochrose_FINAL.html](https://lombard-web-services.github.io/thermocrose/Identification_des_sources_calorifiques.html)** - Document synthétique de 10 pages comprenant :

1. Les instruments de la thermochrose (thermoscope, thermomultiplicateur, thermactinomètre, œthrioscope)
2. Différenciation des chaleurs incidentes
3. Formalisation mathématique complète
4. Cartographie spectrale des mécanismes d'émission
5. Fondements quantiques
6. Entropie et thermodynamique
7. Méthodes exploratoires pour découvrir de nouvelles sources
8. Sources exotiques et frontières physiques
9. Synthèse : de Melloni à la physique moderne
10. Conclusions et perspectives

### Liens externes

- **Documentation en ligne :** https://lombard-web-services.github.io/thermocrose/Identification_des_sources_calorifiques.html
- **Analyse :** https://lombard-web-services.github.io/thermocrose/Thermocrose_Analysis_by_Thibaut_LOMBARD.html
- **Repository GitHub :** https://github.com/Lombard-Web-Services/thermocrose
- **Base de données 150 phénomènes :** https://lombard-web-services.github.io/Docs/Inverse_Square_Law_phenomenon_FR.html

---

## Méthodologie

### Chaîne de mesure de Melloni

La "chaleur" mesurée par Melloni n'est pas une température absolue mais une **déviation électromagnétique** proportionnelle au flux radiatif :

$$\theta_{rhéo} = G \times \frac{n\alpha_{SA}}{R_{th}} \times \frac{\sigma T^4 A_{source}}{4\pi r^2} \times e^{-\tau} \times \epsilon_{det}$$

Où :
- $\theta_{rhéo}$ = déviation du rhéomètre (unité effective de Melloni)
- $G$ = gain du système astatique
- $n\alpha_{SA}$ = coefficient Seebeck bismuth-antimoine
- $\sigma$ = constante de Stefan-Boltzmann
- $r$ = distance (dépendance en $1/r^2$)
- $\tau$ = profondeur optique (absorption)
- $\epsilon_{det}$ = réponse du détecteur

### Classification des sources de chaleur

| Type | Dépendance spatiale | Instrument |
|------|---------------------|------------|
| Directe | $I \propto 1/r^2$ | Thermoscope + Thermactinomètre |
| Réfléchie | $I = \rho I_0 / r^2$ | Dispositif d'Arago |
| Réfractée | $I \propto 1/r^2$ (avec pertes) | Prisme de sel gemme |
| Diffuse | $I = \text{constante}$ | Œthrioscope |

---

## Résultats clés

### Thèse centrale

La chaleur rayonnante n'est pas une grandeur primitive mais une **manifestation électromagnétique du flux énergétique** obéissant intrinsèquement à la loi inverse carrée. Les instruments de Melloni mesurent le **flux** $\Phi$ [W/m²], pas l'énergie interne $Q$ [J].

### Découverte fondamentale

La "chaleur" telle que mesurée par les instruments historiques est déjà **"contaminée" par la géométrie de l'espace** (loi en $1/r^2$) via son expression électromagnétique. Cela suggère une origine commune entre :
- Gravitation newtonienne ($F \propto 1/r^2$)
- Électromagnétisme ($E \propto 1/r^2$)
- Rayonnement thermique ($\Phi \propto 1/r^2$)

### Unification conceptuelle

| Domaine | Grandeur | Loi | Origine profonde |
|---------|----------|-----|------------------|
| Gravité | Force $F_g$ | $1/r^2$ | Entropie d'écran holographique (Verlinde) |
| Électromagnétisme | Champ $E$ | $1/r^2$ | Symétrie de jauge U(1) |
| Thermique (Melloni) | Flux $\Phi$ | $1/r^2$ | Entropie du rayonnement $S = \frac{4}{3}aT^3$ |

---

## Licence

Ce projet est sous licence [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

**Attribution :** Lombard Web Services

Vous êtes libre de :
- **Partager** — copier, distribuer et communiquer le matériel par tous moyens et sous tous formats
- **Adapter** — remixer, transformer et créer à partir du matéiel pour toute utilisation, y compris commerciale

Selon les conditions suivantes :
- **Attribution** — Vous devez créditer l'Œuvre, intégrer un lien vers la licence et indiquer si des modifications ont été effectuées.

---

## Crédits et outils utilisés

Ce document a été élaboré avec l'assistance des outils d'intelligence artificielle suivants :

- **[MOULT-AI Enterprise](https://lombard-web-services.com/Moult-AI_Enterprise-edition/)** - Orchestration Multi-IA Planification
- **[Kimi](https://kimi.moonshot.cn)** - Analyse structurée pour l'identification des sources calorifiques, formalisation mathématique, génération du document HTML 10 pages
- **[DeepSeek](https://deepseek.com)** - Deboggage du travail d'identification
- **[Grok](https://grok.x.ai)** - Discussion initiale sur les fondements physiques, clarification des concepts de gravité/magnétisme/thermique, ajustement du vocable sur les Gaussienne, premiere génération de l'analyse

**Responsable du projet :** Thibaut LOMBARD (Lombard Web Services)

---

## Contact

Pour toute question ou collaboration concernant ce projet :

- **GitHub :** https://github.com/Lombard-Web-Services
- **Repository :** https://github.com/Lombard-Web-Services/thermocrose

---

*"La thermochrose nous apprend que la chaleur, comme la lumière, est soumise aux lois géométriques de l'espace. Ce n'est pas une substance, mais un flux — et le flux obéit à la sphère."*

— Synthèse des travaux de Macedonio Melloni (1850)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Made with Kimi](https://img.shields.io/badge/Made%20with-Kimi-blue)](https://kimi.moonshot.cn)
[![Made with Grok](https://img.shields.io/badge/Made%20with-Grok-black)](https://grok.x.ai)
