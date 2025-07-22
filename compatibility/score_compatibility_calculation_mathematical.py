# import itertools
# import math
# from typing import List, Tuple, Dict

# # ─── 1) Enhanced aspect weights and planet importance multipliers ─────────────

# # Enhanced aspect weights based on astrological tradition
# aspect_base: Dict[str, int] = {
#     "conjunction":  5,    # Increased - most powerful blend
#     "trine":        4,    # Increased - natural harmony
#     "sextile":      2,    # Keep - opportunity/ease
#     "square":      -3,    # More negative - creates tension
#     "opposition":  -2,    # Less negative than square - can be balancing
# }

# # Refined planet importance weights for synastry
# planet_score: Dict[str, float] = {
#     "sun":        1.4,    # Increased - core identity in synastry
#     "moon":       1.3,    # Increased - emotional compatibility crucial
#     "ascendant":  1.2,    # Increased - immediate attraction/chemistry
#     "venus":      1.1,    # Increased - love/attraction deserves higher weight
#     "mars":       1.1,    # Increased - passion/sexual chemistry
#     "mercury":    1.0,    # Keep - communication baseline
#     "medium_coeli": 1.0,  # Slightly decreased - less immediate than ASC
#     "jupiter":    0.9,    # Keep - expansion/growth
#     "saturn":     0.9,    # Increased - commitment/longevity crucial
#     "pluto":      0.8,    # Keep - transformation/intensity
#     "uranus":     0.6,    # Decreased - can be disruptive
#     "neptune":    0.6,    # Decreased - can create illusions
# }

# # ─── 2) Dynamically build compatibility_scores ───────────────────────────────

# compatibility_scores: Dict[Tuple[str, str, str], int] = {
#     (p1, p2, asp): round(aspect_base[asp] * (planet_score[p1] + planet_score[p2]) / 2)
#     for p1, p2 in itertools.combinations_with_replacement(planet_score.keys(), 2)
#     for asp in aspect_base.keys()
# }

# # ─── 3) Aspect list and enhanced orb allowances ──────────────────────────────

# ASPECTS = ["conjunction", "sextile", "trine", "square", "opposition"]

# # Enhanced orb maximums based on astrological tradition
# ORB_MAX: Dict[str, float] = {
#     "conjunction": 10.0,  # Increased - most influential
#     "opposition":  10.0,  # Increased - matches conjunction
#     "trine":       8.0,   # Keep - harmonious flow
#     "square":      8.0,   # Increased - tension needs wider orb
#     "sextile":     6.0,   # Keep - subtler aspect
# }

# # ─── 4) Symmetry helper ───────────────────────────────────────────────────────

# def get_score(p1: str, p2: str, aspect: str) -> int:
#     """
#     Return the base weight for (p1,p2,aspect) or (p2,p1,aspect), or 0 if not defined.
#     """
#     if (p1, p2, aspect) in compatibility_scores:
#         return compatibility_scores[(p1, p2, aspect)]
#     if (p2, p1, aspect) in compatibility_scores:
#         return compatibility_scores[(p2, p1, aspect)]
#     return 0

# # ─── 5) Enhanced orb attenuation ──────────────────────────────────────────────

# # def orb_factor(aspect: str, orb: float) -> float:
# #     """
# #     Enhanced orb attenuation with non-linear decay.
# #     Returns a multiplier in [0,1], where orb=0 → 1.0, and orb ≥ max_orb → 0.0.
# #     """
# #     max_orb = ORB_MAX.get(aspect, max(ORB_MAX.values()))
# #     if orb >= max_orb:
# #         return 0.0
    
# #     # Non-linear decay - stronger aspects maintain power longer
# #     normalized_orb = orb / max_orb
# #     if aspect in ["conjunction", "opposition"]:
# #         return (1.0 - normalized_orb) ** 1.5  # Gentler decay for major aspects
# #     else:
# #         return (1.0 - normalized_orb) ** 2.0  # Steeper decay for minor aspects

# def orb_factor(aspect: str, orb: float) -> float:
#     """
#     Enhanced orb attenuation with softer non-linear decay.
#     """
#     max_orb = ORB_MAX.get(aspect, max(ORB_MAX.values()))
#     if orb >= max_orb:
#         return 0.0
    
#     normalized_orb = orb / max_orb
#     if aspect in ["conjunction", "opposition"]:
#         return (1.0 - normalized_orb) ** 1.2  # Softer decay
#     else:
#         return (1.0 - normalized_orb) ** 1.7  # Softer for trine/sextile/square

# # ─── 6) Special aspect combinations bonus system ──────────────────────────────

# # def apply_special_combinations(detected_aspects: List[Tuple[str, str, str, float]]) -> float:
# #     """
# #     Bonus points for particularly significant aspect patterns in synastry.
# #     """
# #     bonus = 0.0
    
# #     # Create lookup for efficient checking
# #     aspect_set = {(p1, p2, asp) for p1, p2, asp, _ in detected_aspects}
    
# #     # Double whammy bonus (same aspect both ways)
# #     for p1, p2, asp, _ in detected_aspects:
# #         if (p2, p1, asp) in aspect_set:
# #             bonus += 2.0  # Significant mutual aspect
    
# #     # Sun-Moon aspects (classic compatibility indicator)
# #     sun_moon_aspects = [
# #         (p1, p2, asp) for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"sun", "moon"}
# #     ]
# #     if sun_moon_aspects:
# #         bonus += 3.0  # Fundamental compatibility
    
# #     # Venus-Mars aspects (attraction and chemistry)
# #     venus_mars_aspects = [
# #         (p1, p2, asp) for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"venus", "mars"}
# #     ]
# #     if venus_mars_aspects:
# #         bonus += 2.0  # Sexual/romantic chemistry
    
# #     # Sun-Venus aspects (love and admiration)
# #     sun_venus_aspects = [
# #         (p1, p2, asp) for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"sun", "venus"}
# #     ]
# #     if sun_venus_aspects:
# #         bonus += 1.5  # Mutual admiration and affection
    
# #     # Moon-Venus aspects (emotional affection)
# #     moon_venus_aspects = [
# #         (p1, p2, asp) for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"moon", "venus"}
# #     ]
# #     if moon_venus_aspects:
# #         bonus += 1.5  # Emotional harmony in love
    
# #     return bonus

# def apply_special_combinations(detected_aspects: List[Tuple[str, str, str, float]]) -> float:
#     bonus = 0.0
#     aspect_set = {(p1, p2, asp) for p1, p2, asp, _ in detected_aspects}

#     # Mutual aspect (double whammy)
#     for p1, p2, asp, _ in detected_aspects:
#         if (p2, p1, asp) in aspect_set:
#             bonus += 3.0  # Previously 2.0

#     # Core relational patterns
#     if any({p1, p2} == {"sun", "moon"} for p1, p2, asp, _ in detected_aspects):
#         bonus += 5.0  # Previously 3.0

#     if any({p1, p2} == {"venus", "mars"} for p1, p2, asp, _ in detected_aspects):
#         bonus += 3.0  # Previously 2.0

#     if any({p1, p2} == {"sun", "venus"} for p1, p2, asp, _ in detected_aspects):
#         bonus += 2.0  # Previously 1.5

#     if any({p1, p2} == {"moon", "venus"} for p1, p2, asp, _ in detected_aspects):
#         bonus += 2.0  # Previously 1.5

#     return bonus

# # ─── 7) Compute per-pair bounds for normalization ────────────────────────────

# def compute_pair_bounds() -> Dict[Tuple[str,str], Tuple[float,float]]:
#     """
#     For each unique planet-pair, returns (max_positive, max_negative_as_positive).
#     """
#     pairs = set((p1, p2) for (p1, p2, _) in compatibility_scores.keys())
#     bounds: Dict[Tuple[str,str], Tuple[float,float]] = {}
#     for p1, p2 in pairs:
#         key = tuple(sorted((p1, p2)))
#         vals = [get_score(p1, p2, asp) for asp in ASPECTS]
#         bounds[key] = (max(vals), abs(min(vals)))
#     return bounds

# # ─── 8) Normalization helper ──────────────────────────────────────────────────

# def normalize(raw: float, scale_pos: float, scale_neg: float) -> float:
#     """
#     Maps raw ∈ [−scale_pos+scale_neg, +scale_pos−scale_neg] to [0,100].
#     """
#     denom = scale_pos + scale_neg
#     return float("nan") if denom == 0 else (raw + scale_neg) / denom * 100

# # ─── 9) Main scoring routine ─────────────────────────────────────────────────

# def compute_scores(
#     detected_aspects: List[Tuple[str, str, str, float]]
# ) -> Dict[str, float]:
#     """
#     Input:
#       detected_aspects: list of (planet1, planet2, aspect, orb_degrees)
#     Returns:
#       A dict with "Overall" and six enhanced sub-score percentages.
#     """
#     # Precompute pair bounds
#     pair_bounds = compute_pair_bounds()

#     # 1) Raw aspect sum (with enhanced orb attenuation)
#     raw_total = sum(
#         get_score(p1, p2, asp) * orb_factor(asp, orb)
#         for p1, p2, asp, orb in detected_aspects
#     )
    
#     # 2) Apply special combination bonuses
#     combination_bonus = apply_special_combinations(detected_aspects)
#     raw_total += combination_bonus

#     # 3) Compute normalization scales
#     uniq_pairs = {tuple(sorted((p1, p2))) for p1, p2, _, _ in detected_aspects}
#     scale_pos = sum(pair_bounds[p][0] for p in uniq_pairs)
#     scale_neg = sum(pair_bounds[p][1] for p in uniq_pairs)
    
#     # Add potential bonus to positive scale for proper normalization
#     #scale_pos += 20.0  # Reasonable maximum expected bonus
#     scale_pos += 30.0
#     # Overall percentage
#     overall_pct = normalize(raw_total, scale_pos, scale_neg)

#     # 4) Enhanced sub-score categories
#     categories = {
#         "Emotional Rapport":      {"planets": {"moon", "venus"}},      # Added Venus
#         "Intellectual Rapport":   {"planets": {"mercury", "jupiter"}}, # Added Jupiter
#         "Affection & Love":       {"planets": {"venus", "sun"}},       # Added Sun
#         "Physical Chemistry":     {"planets": {"mars", "venus", "pluto"}}, # Added Venus/Pluto
#         "Growth & Vision":        {"planets": {"jupiter", "sun"}},     # Added Sun
#         "Stability & Commitment": {"planets": {"saturn", "moon"}},     # Added Moon
#     }

#     results: Dict[str, float] = {"Overall": overall_pct}

#     for name, cfg in categories.items():
#         ps = cfg["planets"]
#         rel = [
#             (p1, p2, asp, orb)
#             for p1, p2, asp, orb in detected_aspects
#             if p1 in ps or p2 in ps
#         ]
        
#         # Calculate raw category score with orb attenuation
#         raw_cat = sum(
#             get_score(p1, p2, asp) * orb_factor(asp, orb)
#             for p1, p2, asp, orb in rel
#         )
        
#         # Apply category-specific bonuses
#         category_bonus = 0.0
#         if name == "Affection & Love":
#             # Extra bonus for Sun-Venus and Moon-Venus in this category
#             sun_venus_in_cat = any(
#                 {p1, p2} == {"sun", "venus"} for p1, p2, _, _ in rel
#             )
#             moon_venus_in_cat = any(
#                 {p1, p2} == {"moon", "venus"} for p1, p2, _, _ in rel
#             )
#             if sun_venus_in_cat:
#                 category_bonus += 1.5
#             if moon_venus_in_cat:
#                 category_bonus += 1.5
        
#         elif name == "Physical Chemistry":
#             # Extra bonus for Venus-Mars in this category
#             venus_mars_in_cat = any(
#                 {p1, p2} == {"venus", "mars"} for p1, p2, _, _ in rel
#             )
#             if venus_mars_in_cat:
#                 category_bonus += 2.0
        
#         elif name == "Emotional Rapport":
#             # Extra bonus for Sun-Moon in this category
#             sun_moon_in_cat = any(
#                 {p1, p2} == {"sun", "moon"} for p1, p2, _, _ in rel
#             )
#             if sun_moon_in_cat:
#                 category_bonus += 3.0
        
#         raw_cat += category_bonus
        
#         # Normalize category score
#         uniq_cat = {tuple(sorted((p1, p2))) for p1, p2, _, _ in rel}
#         if uniq_cat:  # Only if there are aspects in this category
#             pos_cat = sum(pair_bounds[p][0] for p in uniq_cat)
#             neg_cat = sum(pair_bounds[p][1] for p in uniq_cat)
#             #pos_cat += 10.0  # Add potential category bonus to scale
#             pos_cat += 15.0
#             results[name] = normalize(raw_cat, pos_cat, neg_cat)
#         else:
#             results[name] = 50.0  # Neutral score if no aspects

#     return results

# # ─── 9) Example usage ────────────────────────────────────────────────────────

# if __name__ == "__main__":
#     # Example: parsed from your synastry output

# #     detected_aspects = [
# #     ("sun", "moon", "conjunction", 5.64),
# #     ("sun", "mercury", "opposition", 1.62),
# #     ("sun", "venus", "trine", 0.95),
# #     ("sun", "saturn", "opposition", 9.01),
# #     ("sun", "neptune", "sextile", 0.73),
# #     ("sun", "pluto", "conjunction", 4.56),
# #     ("moon", "sun", "trine", 4.90),
# #     ("moon", "jupiter", "square", 5.81),
# #     ("moon", "saturn", "trine", 6.86),
# #     ("moon", "uranus", "trine", 1.51),
# #     ("moon", "ascendant", "conjunction", 0.61),
# #     ("mercury", "mars", "trine", 3.93),
# #     ("mercury", "jupiter", "trine", 0.28),
# #     ("mercury", "medium_coeli", "trine", 4.18),
# #     ("venus", "sun", "trine", 4.41),
# #     ("venus", "saturn", "trine", 7.35),
# #     ("venus", "uranus", "trine", 1.02),
# #     ("venus", "ascendant", "conjunction", 0.12),
# #     ("mars", "mercury", "trine", 3.82),
# #     ("mars", "venus", "opposition", 4.49),
# #     ("mars", "neptune", "conjunction", 4.70),
# #     ("jupiter", "sun", "sextile", 6.56),
# #     ("jupiter", "moon", "trine", 8.56),
# #     ("jupiter", "jupiter", "square", 4.15),
# #     ("jupiter", "saturn", "sextile", 5.20),
# #     ("jupiter", "uranus", "sextile", 3.17),
# #     ("jupiter", "ascendant", "opposition", 2.27),
# #     ("saturn", "venus", "square", 1.31),
# #     ("saturn", "mars", "sextile", 5.49),
# #     ("saturn", "neptune", "square", 1.09),
# #     ("saturn", "medium_coeli", "sextile", 5.24),
# #     ("uranus", "moon", "sextile", 3.34),
# #     ("uranus", "mercury", "trine", 3.92),
# #     ("uranus", "venus", "opposition", 3.25),
# #     ("uranus", "saturn", "trine", 6.71),
# #     ("uranus", "neptune", "conjunction", 3.04),
# #     ("uranus", "pluto", "sextile", 2.25),
# #     ("neptune", "mercury", "trine", 7.38),
# #     ("neptune", "venus", "opposition", 8.05),
# #     ("neptune", "neptune", "conjunction", 8.26),
# #     ("neptune", "ascendant", "square", 4.53),
# #     ("pluto", "moon", "conjunction", 6.55),
# #     ("pluto", "mercury", "opposition", 0.71),
# #     ("pluto", "venus", "trine", 0.04),
# #     ("pluto", "saturn", "opposition", 9.92),
# #     ("pluto", "neptune", "sextile", 0.17),
# #     ("pluto", "pluto", "conjunction", 5.46),
# #     ("ascendant", "moon", "trine", 6.60),
# #     ("ascendant", "saturn", "sextile", 3.23),
# #     ("ascendant", "uranus", "opposition", 5.14),
# #     ("ascendant", "pluto", "trine", 7.69),
# #     ("ascendant", "ascendant", "sextile", 4.24),
# #     ("medium_coeli", "venus", "square", 1.78),
# #     ("medium_coeli", "mars", "sextile", 5.01),
# #     ("medium_coeli", "neptune", "square", 1.57),
# #     ("medium_coeli", "medium_coeli", "sextile", 4.76)
# # ]
#     excellent_aspects = [
#     # Strong Sun-Moon connection
#     ("sun", "moon", "trine", 2.0),           # Harmonious core compatibility
    
#     # Good Venus-Mars chemistry
#     ("venus", "mars", "sextile", 1.5),       # Moderate attraction/chemistry
#     ("mars", "venus", "conjunction", 4.0),   # Passionate connection (wider orb)
    
#     # Love and admiration
#     ("sun", "venus", "conjunction", 2.5),    # Strong mutual admiration
#     ("moon", "venus", "trine", 3.0),         # Emotional love harmony
    
#     # Attraction and chemistry
#     ("venus", "ascendant", "conjunction", 1.0), # Strong immediate attraction
#     ("mars", "ascendant", "sextile", 2.5),   # Physical attraction
    
#     # Communication
#     ("mercury", "mercury", "sextile", 2.0),  # Good mental connection
#     ("mercury", "moon", "trine", 1.8),       # Emotional understanding
    
#     # Growth and vision
#     ("jupiter", "sun", "sextile", 4.0),      # Mutual growth (wider orb)
#     ("jupiter", "jupiter", "trine", 3.5),    # Shared vision and philosophy
    
#     # Some challenges (but manageable)
#     ("saturn", "mars", "square", 5.0),       # Some tension in action/discipline
#     ("moon", "saturn", "opposition", 6.0),   # Emotional vs security needs
    
#     # Stability factors
#     ("saturn", "sun", "trine", 3.0),         # Stability and commitment
#     ("saturn", "venus", "sextile", 4.5),     # Stable love expression
    
#     # Depth and transformation
#     ("pluto", "moon", "trine", 2.0),         # Deep emotional transformation
#     ("uranus", "venus", "sextile", 3.0),     # Exciting and stimulating love
    
#     # Additional harmonious aspects
#     ("mercury", "jupiter", "trine", 1.0),    # Expansive communication
#     ("venus", "jupiter", "sextile", 2.0)
#     ]
#     scores = compute_scores(excellent_aspects)
#     for cat, pct in scores.items():
#         print(f"{cat:25s}: {pct:5.1f}%")


# # import itertools
# # import math
# # from typing import List, Tuple, Dict

# # # ─── 1) Enhanced aspect weights and planet importance multipliers ─────────────

# # # Enhanced aspect weights based on astrological tradition
# # aspect_base: Dict[str, int] = {
# #     "conjunction":  5,    # Most powerful blend
# #     "trine":        4,    # Natural harmony
# #     "sextile":      2,    # Opportunity/ease
# #     "square":      -2,    # REDUCED from -3 - creates tension but manageable
# #     "opposition":  -1,    # REDUCED from -2 - can be balancing
# # }

# # # Refined planet importance weights for synastry
# # planet_score: Dict[str, float] = {
# #     "sun":        1.4,    # Core identity in synastry
# #     "moon":       1.3,    # Emotional compatibility crucial
# #     "ascendant":  1.2,    # Immediate attraction/chemistry
# #     "venus":      1.1,    # Love/attraction
# #     "mars":       1.1,    # Passion/sexual chemistry
# #     "mercury":    1.0,    # Communication baseline
# #     "coeli": 1.0,         # Career/public image
# #     "jupiter":    0.9,    # Expansion/growth
# #     "saturn":     0.9,    # Commitment/longevity
# #     "pluto":      0.8,    # Transformation/intensity
# #     "uranus":     0.6,    # Can be disruptive
# #     "neptune":    0.6,    # Can create illusions
# # }

# # # ─── 2) Dynamically build compatibility_scores ───────────────────────────────

# # compatibility_scores: Dict[Tuple[str, str, str], int] = {
# #     (p1, p2, asp): round(aspect_base[asp] * (planet_score[p1] + planet_score[p2]) / 2)
# #     for p1, p2 in itertools.combinations_with_replacement(planet_score.keys(), 2)
# #     for asp in aspect_base.keys()
# # }

# # # ─── 3) Aspect list and enhanced orb allowances ──────────────────────────────

# # ASPECTS = ["conjunction", "sextile", "trine", "square", "opposition"]

# # # Enhanced orb maximums based on astrological tradition
# # ORB_MAX: Dict[str, float] = {
# #     "conjunction": 10.0,  # Most influential
# #     "opposition":  10.0,  # Matches conjunction
# #     "trine":       8.0,   # Harmonious flow
# #     "square":      8.0,   # Tension needs wider orb
# #     "sextile":     6.0,   # Subtler aspect
# # }

# # # ─── 4) Symmetry helper ───────────────────────────────────────────────────────

# # def get_score(p1: str, p2: str, aspect: str) -> int:
# #     """
# #     Return the base weight for (p1,p2,aspect) or (p2,p1,aspect), or 0 if not defined.
# #     """
# #     if (p1, p2, aspect) in compatibility_scores:
# #         return compatibility_scores[(p1, p2, aspect)]
# #     if (p2, p1, aspect) in compatibility_scores:
# #         return compatibility_scores[(p2, p1, aspect)]
# #     return 0

# # # ─── 5) IMPROVED orb attenuation (gentler for harmonious aspects) ─────────────

# # def orb_factor(aspect: str, orb: float) -> float:
# #     """
# #     IMPROVED orb attenuation with gentler decay for harmonious aspects.
# #     Returns a multiplier in [0,1], where orb=0 → 1.0, and orb ≥ max_orb → 0.0.
# #     """
# #     max_orb = ORB_MAX.get(aspect, max(ORB_MAX.values()))
# #     if orb >= max_orb:
# #         return 0.0
    
# #     normalized_orb = orb / max_orb
    
# #     # GENTLER attenuation for harmonious aspects
# #     if aspect in ["conjunction", "trine", "sextile"]:
# #         return (1.0 - normalized_orb) ** 1.2  # Much gentler decay
# #     else:  # square, opposition
# #         return (1.0 - normalized_orb) ** 1.8  # Moderate decay (was 2.0)

# # # ─── 6) ENHANCED special aspect combinations bonus system ─────────────────────

# # def apply_special_combinations(detected_aspects: List[Tuple[str, str, str, float]]) -> float:
# #     """
# #     ENHANCED bonus points for particularly significant aspect patterns in synastry.
# #     """
# #     bonus = 0.0
    
# #     # Create lookup for efficient checking
# #     aspect_set = {(p1, p2, asp) for p1, p2, asp, _ in detected_aspects}
    
# #     # Double whammy bonus (same aspect both ways) - INCREASED
# #     double_whammy_count = 0
# #     for p1, p2, asp, _ in detected_aspects:
# #         if (p2, p1, asp) in aspect_set:
# #             double_whammy_count += 1
# #     bonus += double_whammy_count * 1.5  # Increased from 2.0 but counting all instances
    
# #     # Sun-Moon aspects (classic compatibility indicator) - INCREASED
# #     sun_moon_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"sun", "moon"}
# #     ]
# #     for asp in sun_moon_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 5.0  # Major bonus for harmonious Sun-Moon
# #         elif asp == "sextile":
# #             bonus += 3.0  # Good bonus for sextile
# #         else:  # square, opposition
# #             bonus += 1.0  # Small bonus even for challenging (still important)
    
# #     # Venus-Mars aspects (attraction and chemistry) - INCREASED
# #     venus_mars_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"venus", "mars"}
# #     ]
# #     for asp in venus_mars_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 4.0  # Major chemistry bonus
# #         elif asp == "sextile":
# #             bonus += 2.5  # Good chemistry
# #         else:  # square, opposition
# #             bonus += 1.5  # Tension but still attraction
    
# #     # Sun-Venus aspects (love and admiration) - INCREASED
# #     sun_venus_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"sun", "venus"}
# #     ]
# #     for asp in sun_venus_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 3.0
# #         elif asp == "sextile":
# #             bonus += 2.0
# #         else:
# #             bonus += 0.5
    
# #     # Moon-Venus aspects (emotional affection) - INCREASED
# #     moon_venus_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"moon", "venus"}
# #     ]
# #     for asp in moon_venus_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 3.0
# #         elif asp == "sextile":
# #             bonus += 2.0
# #         else:
# #             bonus += 0.5
    
# #     # NEW: Sun-Ascendant aspects (immediate attraction)
# #     sun_asc_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"sun", "ascendant"}
# #     ]
# #     for asp in sun_asc_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 2.5
# #         elif asp == "sextile":
# #             bonus += 1.5
# #         else:
# #             bonus += 0.5
    
# #     # NEW: Moon-Ascendant aspects (emotional comfort)
# #     moon_asc_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"moon", "ascendant"}
# #     ]
# #     for asp in moon_asc_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 2.5
# #         elif asp == "sextile":
# #             bonus += 1.5
# #         else:
# #             bonus += 0.5
    
# #     # NEW: Venus-Ascendant aspects (attraction and charm)
# #     venus_asc_aspects = [
# #         asp for p1, p2, asp, _ in detected_aspects
# #         if {p1, p2} == {"venus", "ascendant"}
# #     ]
# #     for asp in venus_asc_aspects:
# #         if asp in ["conjunction", "trine"]:
# #             bonus += 2.0
# #         elif asp == "sextile":
# #             bonus += 1.0
# #         else:
# #             bonus += 0.5
    
# #     # NEW: Harmonious aspect pattern bonus
# #     harmonious_count = sum(1 for _, _, asp, _ in detected_aspects if asp in ["conjunction", "trine", "sextile"])
# #     total_aspects = len(detected_aspects)
# #     if total_aspects > 0:
# #         harmony_ratio = harmonious_count / total_aspects
# #         if harmony_ratio >= 0.7:
# #             bonus += 3.0  # High harmony bonus
# #         elif harmony_ratio >= 0.6:
# #             bonus += 2.0  # Good harmony bonus
# #         elif harmony_ratio >= 0.5:
# #             bonus += 1.0  # Moderate harmony bonus
    
# #     return bonus

# # # ─── 7) IMPROVED normalization system ─────────────────────────────────────────

# # def compute_pair_bounds() -> Dict[Tuple[str,str], Tuple[float,float]]:
# #     """
# #     For each unique planet-pair, returns (max_positive, max_negative_as_positive).
# #     """
# #     pairs = set((p1, p2) for (p1, p2, _) in compatibility_scores.keys())
# #     bounds: Dict[Tuple[str,str], Tuple[float,float]] = {}
# #     for p1, p2 in pairs:
# #         key = tuple(sorted((p1, p2)))
# #         vals = [get_score(p1, p2, asp) for asp in ASPECTS]
# #         bounds[key] = (max(vals), abs(min(vals)))
# #     return bounds

# # def normalize(raw: float, scale_pos: float, scale_neg: float) -> float:
# #     """
# #     IMPROVED normalization that's more generous with positive scores.
# #     Maps raw scores to a 0-100 scale with better distribution.
# #     """
# #     denom = scale_pos + scale_neg
# #     if denom == 0:
# #         return 50.0  # Neutral if no valid aspects
    
# #     # Calculate base percentage
# #     base_pct = (raw + scale_neg) / denom * 100
    
# #     # Apply S-curve transformation to make middle-high scores more achievable
# #     # This compresses very low scores and expands middle-to-high scores
# #     if base_pct < 50:
# #         # Compress low scores less severely
# #         return base_pct * 0.8 + 10
# #     else:
# #         # Expand high scores more generously
# #         excess = base_pct - 50
# #         return 50 + (excess * 1.3)

# # # ─── 8) IMPROVED main scoring routine ─────────────────────────────────────────

# # def compute_scores(
# #     detected_aspects: List[Tuple[str, str, str, float]]
# # ) -> Dict[str, float]:
# #     """
# #     IMPROVED scoring with better normalization and more generous bonuses.
# #     """
# #     # Precompute pair bounds
# #     pair_bounds = compute_pair_bounds()

# #     # 1) Raw aspect sum (with improved orb attenuation)
# #     raw_total = sum(
# #         get_score(p1, p2, asp) * orb_factor(asp, orb)
# #         for p1, p2, asp, orb in detected_aspects
# #     )
    
# #     # 2) Apply enhanced special combination bonuses
# #     combination_bonus = apply_special_combinations(detected_aspects)
# #     raw_total += combination_bonus

# #     # 3) Compute normalization scales with adjustment for bonuses
# #     uniq_pairs = {tuple(sorted((p1, p2))) for p1, p2, _, _ in detected_aspects}
# #     scale_pos = sum(pair_bounds[p][0] for p in uniq_pairs)
# #     scale_neg = sum(pair_bounds[p][1] for p in uniq_pairs)
    
# #     # Increase potential bonus scale for better normalization
# #     scale_pos += 30.0  # Increased from 20.0 to account for larger bonuses

# #     # Overall percentage with improved normalization
# #     overall_pct = normalize(raw_total, scale_pos, scale_neg)

# #     # 4) Enhanced sub-score categories with better bonuses
# #     categories = {
# #         "Emotional Rapport":      {"planets": {"moon", "venus", "sun"}},      # Added Sun
# #         "Intellectual Rapport":   {"planets": {"mercury", "jupiter", "uranus"}}, # Added Uranus
# #         "Affection & Love":       {"planets": {"venus", "sun", "moon"}},       # Added Moon
# #         "Physical Chemistry":     {"planets": {"mars", "venus", "pluto"}},
# #         "Growth & Vision":        {"planets": {"jupiter", "sun", "uranus"}},   # Added Uranus
# #         "Stability & Commitment": {"planets": {"saturn", "moon", "sun"}},      # Added Sun
# #     }

# #     results: Dict[str, float] = {"Overall": overall_pct}

# #     for name, cfg in categories.items():
# #         ps = cfg["planets"]
# #         rel = [
# #             (p1, p2, asp, orb)
# #             for p1, p2, asp, orb in detected_aspects
# #             if p1 in ps or p2 in ps
# #         ]
        
# #         # Calculate raw category score with orb attenuation
# #         raw_cat = sum(
# #             get_score(p1, p2, asp) * orb_factor(asp, orb)
# #             for p1, p2, asp, orb in rel
# #         )
        
# #         # Apply enhanced category-specific bonuses
# #         category_bonus = 0.0
        
# #         if name == "Affection & Love":
# #             # Enhanced bonuses for love aspects
# #             for p1, p2, asp, _ in rel:
# #                 if {p1, p2} == {"sun", "venus"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 3.0
# #                 elif {p1, p2} == {"moon", "venus"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 3.0
# #                 elif {p1, p2} == {"sun", "moon"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 2.0
        
# #         elif name == "Physical Chemistry":
# #             # Enhanced bonuses for chemistry aspects
# #             for p1, p2, asp, _ in rel:
# #                 if {p1, p2} == {"venus", "mars"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 4.0
# #                 elif {p1, p2} == {"venus", "mars"} and asp in ["sextile"]:
# #                     category_bonus += 2.0
# #                 elif {p1, p2} == {"venus", "pluto"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 2.0
        
# #         elif name == "Emotional Rapport":
# #             # Enhanced bonuses for emotional connection
# #             for p1, p2, asp, _ in rel:
# #                 if {p1, p2} == {"sun", "moon"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 4.0
# #                 elif {p1, p2} == {"moon", "venus"} and asp in ["conjunction", "trine"]:
# #                     category_bonus += 3.0
        
# #         raw_cat += category_bonus
        
# #         # Normalize category score with improved system
# #         uniq_cat = {tuple(sorted((p1, p2))) for p1, p2, _, _ in rel}
# #         if uniq_cat:
# #             pos_cat = sum(pair_bounds[p][0] for p in uniq_cat)
# #             neg_cat = sum(pair_bounds[p][1] for p in uniq_cat)
# #             pos_cat += 15.0  # Increased potential category bonus
# #             results[name] = normalize(raw_cat, pos_cat, neg_cat)
# #         else:
# #             results[name] = 50.0  # Neutral score if no aspects

# #     return results

# # # ─── 9) Example usage with the same data ─────────────────────────────────────

# # if __name__ == "__main__":
# #     # Example: parsed from your synastry output
# #     # detected_aspects = [('sun', 'sun', 'trine', 2.55), ('sun', 'mercury', 'trine', 1.21), ('sun', 'saturn', 'opposition', 0.62), ('sun', 'neptune', 'sextile', 0.73), ('sun', 'pluto', 'conjunction', 6.29), ('sun', 'ascendant', 'trine', 0.56), ('moon', 'moon', 'sextile', 6.64), ('moon', 'venus', 'opposition', 5.95), ('moon', 'uranus', 'trine', 0.27), ('mercury', 'mars', 'opposition', 2.12), ('venus', 'moon', 'sextile', 6.15), ('venus', 'venus', 'opposition', 5.45), ('venus', 'uranus', 'trine', 0.22), ('mars', 'mercury', 'sextile', 4.23), ('mars', 'venus', 'square', 2.75), ('mars', 'saturn', 'trine', 4.82), ('mars', 'neptune', 'conjunction', 4.71), ('mars', 'ascendant', 'opposition', 6.0), ('jupiter', 'venus', 'conjunction', 7.6), ('jupiter', 'uranus', 'sextile', 1.93), ('jupiter', 'pluto', 'trine', 7.92), ('saturn', 'moon', 'trine', 7.85), ('saturn', 'venus', 'conjunction', 8.54), ('saturn', 'jupiter', 'sextile', 4.29), ('saturn', 'neptune', 'square', 1.09), ('saturn', 'ascendant', 'square', 0.2), ('uranus', 'sun', 'sextile', 0.25), ('uranus', 'mercury', 'sextile', 3.51), ('uranus', 'saturn', 'trine', 2.92), ('uranus', 'neptune', 'conjunction', 3.03), ('uranus', 'pluto', 'sextile', 3.99), ('uranus', 'ascendant', 'opposition', 1.74), ('neptune', 'venus', 'square', 0.81), ('neptune', 'saturn', 'trine', 8.38), ('neptune', 'neptune', 'conjunction', 8.26), ('neptune', 'ascendant', 'opposition', 9.55), ('pluto', 'sun', 'trine', 3.46), ('pluto', 'mercury', 'trine', 0.3), ('pluto', 'saturn', 'opposition', 0.29), ('pluto', 'neptune', 'sextile', 0.18), ('pluto', 'pluto', 'conjunction', 7.2), ('pluto', 'ascendant', 'trine', 1.47), ('ascendant', 'mars', 'square', 0.34), ('ascendant', 'uranus', 'opposition', 3.9), ('ascendant', 'pluto', 'trine', 5.95), ('coeli', 'moon', 'trine', 8.32), ('coeli', 'venus', 'conjunction', 9.02), ('coeli', 'jupiter', 'sextile', 4.77), ('coeli', 'neptune', 'square', 1.57), ('coeli', 'ascendant', 'square', 0.28)]
# #     excellent_aspects = [
# #     # Strong Sun-Moon connection
# #     ("sun", "moon", "trine", 2.0),           # Harmonious core compatibility
    
# #     # Good Venus-Mars chemistry
# #     ("venus", "mars", "sextile", 1.5),       # Moderate attraction/chemistry
# #     ("mars", "venus", "conjunction", 4.0),   # Passionate connection (wider orb)
    
# #     # Love and admiration
# #     ("sun", "venus", "conjunction", 2.5),    # Strong mutual admiration
# #     ("moon", "venus", "trine", 3.0),         # Emotional love harmony
    
# #     # Attraction and chemistry
# #     ("venus", "ascendant", "conjunction", 1.0), # Strong immediate attraction
# #     ("mars", "ascendant", "sextile", 2.5),   # Physical attraction
    
# #     # Communication
# #     ("mercury", "mercury", "sextile", 2.0),  # Good mental connection
# #     ("mercury", "moon", "trine", 1.8),       # Emotional understanding
    
# #     # Growth and vision
# #     ("jupiter", "sun", "sextile", 4.0),      # Mutual growth (wider orb)
# #     ("jupiter", "jupiter", "trine", 3.5),    # Shared vision and philosophy
    
# #     # Some challenges (but manageable)
# #     ("saturn", "mars", "square", 5.0),       # Some tension in action/discipline
# #     ("moon", "saturn", "opposition", 6.0),   # Emotional vs security needs
    
# #     # Stability factors
# #     ("saturn", "sun", "trine", 3.0),         # Stability and commitment
# #     ("saturn", "venus", "sextile", 4.5),     # Stable love expression
    
# #     # Depth and transformation
# #     ("pluto", "moon", "trine", 2.0),         # Deep emotional transformation
# #     ("uranus", "venus", "sextile", 3.0),     # Exciting and stimulating love
    
# #     # Additional harmonious aspects
# #     ("mercury", "jupiter", "trine", 1.0),    # Expansive communication
# #     ("venus", "jupiter", "sextile", 2.0)
# #     ]

# #     print("=== IMPROVED SCORING SYSTEM RESULTS ===")
# #     scores = compute_scores(excellent_aspects)
# #     for cat, pct in scores.items():
# #         print(f"{cat:25s}: {pct:5.1f}%")
    
# #     print("\n=== COMPARISON WITH ORIGINAL SYSTEM ===")
# #     print("This should show noticeably higher scores while maintaining astrological integrity.")

# Define compatibility data 

# compatibility_data = {
#     "Aries": {
#         "Aries": {"overall": 80, "communication": 70, "emotional": 60, "intimacy": 85, "explanation": "Both are fiery and passionate, but may clash due to similar strong personalities."},
#         "Taurus": {"overall": 65, "communication": 50, "emotional": 70, "intimacy": 80, "explanation": "Taurus provides stability, while Aries brings excitement. Differences in pace may cause friction."},
#         "Gemini": {"overall": 75, "communication": 85, "emotional": 60, "intimacy": 70, "explanation": "Both enjoy mental stimulation and variety, but Gemini's indecisiveness may frustrate Aries."},
#         "Cancer": {"overall": 60, "communication": 50, "emotional": 75, "intimacy": 65, "explanation": "Cancer's emotional depth contrasts with Aries' directness, leading to potential misunderstandings."},
#         "Leo": {"overall": 85, "communication": 75, "emotional": 70, "intimacy": 90, "explanation": "Both are passionate and love attention, but may compete for dominance."},
#         "Virgo": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 60, "explanation": "Virgo's practicality may clash with Aries' impulsiveness, but both value honesty."},
#         "Libra": {"overall": 70, "communication": 80, "emotional": 65, "intimacy": 75, "explanation": "Libra's diplomacy can balance Aries' directness, but Libra's indecisiveness may frustrate Aries."},
#         "Scorpio": {"overall": 65, "communication": 55, "emotional": 70, "intimacy": 80, "explanation": "Scorpio's intensity may overwhelm Aries, but both are passionate and loyal."},
#         "Sagittarius": {"overall": 90, "communication": 80, "emotional": 75, "intimacy": 85, "explanation": "Both love adventure and freedom, making for a dynamic and exciting relationship."},
#         "Capricorn": {"overall": 50, "communication": 45, "emotional": 55, "intimacy": 60, "explanation": "Capricorn's caution may frustrate Aries' spontaneity, but both are loyal and committed."},
#         "Aquarius": {"overall": 75, "communication": 80, "emotional": 65, "intimacy": 70, "explanation": "Both value independence and intellectual stimulation, but Aquarius' detachment may frustrate Aries."},
#         "Pisces": {"overall": 60, "communication": 55, "emotional": 70, "intimacy": 65, "explanation": "Pisces' sensitivity may clash with Aries' directness, but both are compassionate and caring."}
#     },
#     "Taurus": {
#         "Aries": {"overall": 65, "communication": 50, "emotional": 70, "intimacy": 80, "explanation": "Taurus provides stability, while Aries brings excitement. Differences in pace may cause friction."},
#         "Taurus": {"overall": 90, "communication": 80, "emotional": 85, "intimacy": 90, "explanation": "Both value stability and sensuality, leading to a harmonious and secure relationship."},
#         "Gemini": {"overall": 60, "communication": 70, "emotional": 50, "intimacy": 65, "explanation": "Gemini's need for variety may frustrate Taurus' desire for routine, but both enjoy mental stimulation."},
#         "Cancer": {"overall": 85, "communication": 75, "emotional": 90, "intimacy": 80, "explanation": "Both value security and emotional connection, leading to a nurturing and stable relationship."},
#         "Leo": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 85, "explanation": "Both are loyal and passionate, but Leo's need for attention may clash with Taurus' desire for stability."},
#         "Virgo": {"overall": 80, "communication": 85, "emotional": 75, "intimacy": 80, "explanation": "Both are practical and detail-oriented, leading to a harmonious and efficient relationship."},
#         "Libra": {"overall": 85, "communication": 90, "emotional": 80, "intimacy": 85, "explanation": "Both value harmony and beauty, leading to a balanced and aesthetically pleasing relationship."},
#         "Scorpio": {"overall": 80, "communication": 70, "emotional": 85, "intimacy": 90, "explanation": "Both are intense and passionate, leading to a deep and transformative relationship."},
#         "Sagittarius": {"overall": 60, "communication": 65, "emotional": 55, "intimacy": 70, "explanation": "Sagittarius' love for adventure may clash with Taurus' desire for stability, but both are optimistic and enthusiastic."},
#         "Capricorn": {"overall": 90, "communication": 80, "emotional": 85, "intimacy": 90, "explanation": "Both are practical and ambitious, leading to a stable and successful relationship."},
#         "Aquarius": {"overall": 50, "communication": 60, "emotional": 45, "intimacy": 55, "explanation": "Aquarius' need for independence may frustrate Taurus' desire for closeness, but both value intellectual stimulation."},
#         "Pisces": {"overall": 70, "communication": 65, "emotional": 80, "intimacy": 75, "explanation": "Both are compassionate and sensitive, leading to a deep and empathetic relationship."}
#     },
#     "Gemini": {
#         "Aries": {"overall": 75, "communication": 85, "emotional": 60, "intimacy": 70, "explanation": "Both enjoy mental stimulation and variety, but Gemini's indecisiveness may frustrate Aries."},
#         "Taurus": {"overall": 60, "communication": 70, "emotional": 50, "intimacy": 65, "explanation": "Gemini's need for variety may frustrate Taurus' desire for routine, but both enjoy mental stimulation."},
#         "Gemini": {"overall": 85, "communication": 95, "emotional": 70, "intimacy": 80, "explanation": "Both enjoy mental stimulation and variety, leading to a lively and intellectually stimulating relationship."},
#         "Cancer": {"overall": 65, "communication": 70, "emotional": 75, "intimacy": 60, "explanation": "Cancer's emotional depth may clash with Gemini's need for variety, but both are adaptable and caring."},
#         "Leo": {"overall": 70, "communication": 80, "emotional": 65, "intimacy": 75, "explanation": "Both enjoy attention and mental stimulation, but Leo's need for dominance may frustrate Gemini's need for variety."},
#         "Virgo": {"overall": 75, "communication": 85, "emotional": 70, "intimacy": 70, "explanation": "Both are detail-oriented and enjoy mental stimulation, leading to a practical and intellectually stimulating relationship."},
#         "Libra": {"overall": 80, "communication": 90, "emotional": 75, "intimacy": 80, "explanation": "Both value harmony and intellectual stimulation, leading to a balanced and intellectually stimulating relationship."},
#         "Scorpio": {"overall": 50, "communication": 55, "emotional": 60, "intimacy": 65, "explanation": "Scorpio's intensity may overwhelm Gemini, but both are curious and enjoy mental stimulation."},
#         "Sagittarius": {"overall": 80, "communication": 85, "emotional": 75, "intimacy": 80, "explanation": "Both enjoy adventure and intellectual stimulation, leading to a dynamic and exciting relationship."},
#         "Capricorn": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 60, "explanation": "Capricorn's caution may frustrate Gemini's need for variety, but both are loyal and committed."},
#         "Aquarius": {"overall": 85, "communication": 90, "emotional": 80, "intimacy": 85, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Pisces": {"overall": 60, "communication": 65, "emotional": 70, "intimacy": 65, "explanation": "Pisces' sensitivity may clash with Gemini's need for variety, but both are compassionate and caring."}
#     },
#     "Cancer": {
#         "Aries": {"overall": 60, "communication": 50, "emotional": 75, "intimacy": 65, "explanation": "Cancer's emotional depth contrasts with Aries' directness, leading to potential misunderstandings."},
#         "Taurus": {"overall": 85, "communication": 75, "emotional": 90, "intimacy": 80, "explanation": "Both value security and emotional connection, leading to a nurturing and stable relationship."},
#         "Gemini": {"overall": 65, "communication": 70, "emotional": 75, "intimacy": 60, "explanation": "Cancer's emotional depth may clash with Gemini's need for variety, but both are adaptable and caring."},
#         "Cancer": {"overall": 90, "communication": 85, "emotional": 95, "intimacy": 90, "explanation": "Both are deeply emotional and nurturing, leading to a very intimate and caring relationship."},
#         "Leo": {"overall": 70, "communication": 65, "emotional": 80, "intimacy": 75, "explanation": "Leo's need for attention may clash with Cancer's emotional depth, but both are loyal and passionate."},
#         "Virgo": {"overall": 80, "communication": 80, "emotional": 85, "intimacy": 80, "explanation": "Both are nurturing and detail-oriented, leading to a harmonious and caring relationship."},
#         "Libra": {"overall": 75, "communication": 80, "emotional": 80, "intimacy": 75, "explanation": "Both value harmony and emotional connection, leading to a balanced and caring relationship."},
#         "Scorpio": {"overall": 85, "communication": 80, "emotional": 90, "intimacy": 90, "explanation": "Both are deeply emotional and passionate, leading to a very intimate and transformative relationship."},
#         "Sagittarius": {"overall": 60, "communication": 65, "emotional": 55, "intimacy": 65, "explanation": "Sagittarius' love for adventure may clash with Cancer's need for security, but both are optimistic and enthusiastic."},
#         "Capricorn": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 75, "explanation": "Both value security and stability, leading to a stable and committed relationship."},
#         "Aquarius": {"overall": 50, "communication": 55, "emotional": 50, "intimacy": 55, "explanation": "Aquarius' need for independence may frustrate Cancer's need for closeness, but both value intellectual stimulation."},
#         "Pisces": {"overall": 90, "communication": 85, "emotional": 95, "intimacy": 90, "explanation": "Both are deeply emotional and compassionate, leading to a very intimate and empathetic relationship."}
#     },
#     "Leo": {
#         "Aries": {"overall": 85, "communication": 75, "emotional": 70, "intimacy": 90, "explanation": "Both are passionate and love attention, but may compete for dominance."},
#         "Taurus": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 85, "explanation": "Both are loyal and passionate, but Leo's need for attention may clash with Taurus' desire for stability."},
#         "Gemini": {"overall": 70, "communication": 80, "emotional": 65, "intimacy": 75, "explanation": "Both enjoy attention and mental stimulation, but Leo's need for dominance may frustrate Gemini's need for variety."},
#         "Cancer": {"overall": 70, "communication": 65, "emotional": 80, "intimacy": 75, "explanation": "Leo's need for attention may clash with Cancer's emotional depth, but both are loyal and passionate."},
#         "Leo": {"overall": 85, "communication": 80, "emotional": 85, "intimacy": 90, "explanation": "Both are passionate and love attention, leading to a dynamic and exciting relationship."},
#         "Virgo": {"overall": 60, "communication": 65, "emotional": 55, "intimacy": 65, "explanation": "Virgo's practicality may clash with Leo's need for attention, but both are loyal and detail-oriented."},
#         "Libra": {"overall": 80, "communication": 85, "emotional": 80, "intimacy": 85, "explanation": "Both value harmony and beauty, leading to a balanced and aesthetically pleasing relationship."},
#         "Scorpio": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 85, "explanation": "Both are intense and passionate, leading to a deep and transformative relationship."},
#         "Sagittarius": {"overall": 85, "communication": 80, "emotional": 80, "intimacy": 90, "explanation": "Both enjoy adventure and freedom, leading to a dynamic and exciting relationship."},
#         "Capricorn": {"overall": 60, "communication": 55, "emotional": 60, "intimacy": 65, "explanation": "Capricorn's caution may frustrate Leo's spontaneity, but both are loyal and committed."},
#         "Aquarius": {"overall": 65, "communication": 70, "emotional": 60, "intimacy": 65, "explanation": "Aquarius' need for independence may frustrate Leo's need for attention, but both value intellectual stimulation."},
#         "Pisces": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 70, "explanation": "Pisces' sensitivity may clash with Leo's directness, but both are compassionate and caring."}
#     },
#     "Virgo": {
#         "Aries": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 60, "explanation": "Virgo's practicality may clash with Aries' impulsiveness, but both value honesty."},
#         "Taurus": {"overall": 80, "communication": 85, "emotional": 75, "intimacy": 80, "explanation": "Both are practical and detail-oriented, leading to a harmonious and efficient relationship."},
#         "Gemini": {"overall": 75, "communication": 85, "emotional": 70, "intimacy": 70, "explanation": "Both are detail-oriented and enjoy mental stimulation, leading to a practical and intellectually stimulating relationship."},
#         "Cancer": {"overall": 80, "communication": 80, "emotional": 85, "intimacy": 80, "explanation": "Both are nurturing and detail-oriented, leading to a harmonious and caring relationship."},
#         "Leo": {"overall": 60, "communication": 65, "emotional": 55, "intimacy": 65, "explanation": "Virgo's practicality may clash with Leo's need for attention, but both are loyal and detail-oriented."},
#         "Virgo": {"overall": 85, "communication": 90, "emotional": 80, "intimacy": 85, "explanation": "Both are practical and detail-oriented, leading to a very harmonious and efficient relationship."},
#         "Libra": {"overall": 75, "communication": 85, "emotional": 75, "intimacy": 80, "explanation": "Both value harmony and intellectual stimulation, leading to a balanced and intellectually stimulating relationship."},
#         "Scorpio": {"overall": 70, "communication": 75, "emotional": 75, "intimacy": 80, "explanation": "Both are detail-oriented and passionate, leading to a deep and transformative relationship."},
#         "Sagittarius": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 60, "explanation": "Sagittarius' love for adventure may clash with Virgo's need for stability, but both are optimistic and enthusiastic."},
#         "Capricorn": {"overall": 80, "communication": 80, "emotional": 80, "intimacy": 85, "explanation": "Both are practical and ambitious, leading to a stable and successful relationship."},
#         "Aquarius": {"overall": 65, "communication": 70, "emotional": 60, "intimacy": 65, "explanation": "Aquarius' need for independence may frustrate Virgo's need for closeness, but both value intellectual stimulation."},
#         "Pisces": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 70, "explanation": "Pisces' sensitivity may clash with Virgo's practicality, but both are compassionate and caring."}
#     },
#     "Libra": {
#         "Aries": {"overall": 70, "communication": 80, "emotional": 65, "intimacy": 75, "explanation": "Libra's diplomacy can balance Aries' directness, but Libra's indecisiveness may frustrate Aries."},
#         "Taurus": {"overall": 85, "communication": 90, "emotional": 80, "intimacy": 85, "explanation": "Both value harmony and beauty, leading to a balanced and aesthetically pleasing relationship."},
#         "Gemini": {"overall": 80, "communication": 90, "emotional": 75, "intimacy": 80, "explanation": "Both value harmony and intellectual stimulation, leading to a balanced and intellectually stimulating relationship."},
#         "Cancer": {"overall": 75, "communication": 80, "emotional": 80, "intimacy": 75, "explanation": "Both value harmony and emotional connection, leading to a balanced and caring relationship."},
#         "Leo": {"overall": 80, "communication": 85, "emotional": 80, "intimacy": 85, "explanation": "Both value harmony and beauty, leading to a balanced and aesthetically pleasing relationship."},
#         "Virgo": {"overall": 75, "communication": 85, "emotional": 75, "intimacy": 80, "explanation": "Both value harmony and intellectual stimulation, leading to a balanced and intellectually stimulating relationship."},
#         "Libra": {"overall": 85, "communication": 95, "emotional": 85, "intimacy": 90, "explanation": "Both value harmony and beauty, leading to a very balanced and aesthetically pleasing relationship."},
#         "Scorpio": {"overall": 70, "communication": 75, "emotional": 80, "intimacy": 80, "explanation": "Both value depth and intensity, leading to a deep and transformative relationship."},
#         "Sagittarius": {"overall": 75, "communication": 80, "emotional": 75, "intimacy": 80, "explanation": "Both enjoy adventure and intellectual stimulation, leading to a dynamic and exciting relationship."},
#         "Capricorn": {"overall": 70, "communication": 75, "emotional": 70, "intimacy": 75, "explanation": "Capricorn's caution may frustrate Libra's need for harmony, but both are loyal and committed."},
#         "Aquarius": {"overall": 80, "communication": 85, "emotional": 80, "intimacy": 85, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Pisces": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 80, "explanation": "Pisces' sensitivity may clash with Libra's need for harmony, but both are compassionate and caring."}
#     },
#     "Scorpio": {
#         "Aries": {"overall": 65, "communication": 55, "emotional": 70, "intimacy": 80, "explanation": "Scorpio's intensity may overwhelm Aries, but both are passionate and loyal."},
#         "Taurus": {"overall": 80, "communication": 70, "emotional": 85, "intimacy": 90, "explanation": "Both are intense and passionate, leading to a deep and transformative relationship."},
#         "Gemini": {"overall": 50, "communication": 55, "emotional": 60, "intimacy": 65, "explanation": "Scorpio's intensity may overwhelm Gemini, but both are curious and enjoy mental stimulation."},
#         "Cancer": {"overall": 85, "communication": 80, "emotional": 90, "intimacy": 90, "explanation": "Both are deeply emotional and passionate, leading to a very intimate and transformative relationship."},
#         "Leo": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 85, "explanation": "Both are intense and passionate, leading to a deep and transformative relationship."},
#         "Virgo": {"overall": 70, "communication": 75, "emotional": 75, "intimacy": 80, "explanation": "Both are detail-oriented and passionate, leading to a deep and transformative relationship."},
#         "Libra": {"overall": 70, "communication": 75, "emotional": 80, "intimacy": 80, "explanation": "Both value depth and intensity, leading to a deep and transformative relationship."},
#         "Scorpio": {"overall": 90, "communication": 85, "emotional": 95, "intimacy": 95, "explanation": "Both are deeply emotional and passionate, leading to a very intimate and transformative relationship."},
#         "Sagittarius": {"overall": 65, "communication": 70, "emotional": 65, "intimacy": 70, "explanation": "Sagittarius' love for adventure may clash with Scorpio's need for depth, but both are optimistic and enthusiastic."},
#         "Capricorn": {"overall": 80, "communication": 75, "emotional": 85, "intimacy": 85, "explanation": "Both are intense and ambitious, leading to a stable and successful relationship."},
#         "Aquarius": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 55, "explanation": "Aquarius' need for independence may frustrate Scorpio's need for depth, but both value intellectual stimulation."},
#         "Pisces": {"overall": 85, "communication": 80, "emotional": 90, "intimacy": 90, "explanation": "Both are deeply emotional and compassionate, leading to a very intimate and empathetic relationship."}
#     },
#     "Sagittarius": {
#         "Aries": {"overall": 90, "communication": 80, "emotional": 75, "intimacy": 85, "explanation": "Both love adventure and freedom, making for a dynamic and exciting relationship."},
#         "Taurus": {"overall": 60, "communication": 65, "emotional": 55, "intimacy": 70, "explanation": "Sagittarius' love for adventure may clash with Taurus' desire for stability, but both are optimistic and enthusiastic."},
#         "Gemini": {"overall": 80, "communication": 85, "emotional": 75, "intimacy": 80, "explanation": "Both enjoy adventure and intellectual stimulation, leading to a dynamic and exciting relationship."},
#         "Cancer": {"overall": 60, "communication": 65, "emotional": 55, "intimacy": 65, "explanation": "Sagittarius' love for adventure may clash with Cancer's need for security, but both are optimistic and enthusiastic."},
#         "Leo": {"overall": 85, "communication": 80, "emotional": 80, "intimacy": 90, "explanation": "Both enjoy adventure and freedom, leading to a dynamic and exciting relationship."},
#         "Virgo": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 60, "explanation": "Sagittarius' love for adventure may clash with Virgo's need for stability, but both are optimistic and enthusiastic."},
#         "Libra": {"overall": 75, "communication": 80, "emotional": 75, "intimacy": 80, "explanation": "Both enjoy adventure and intellectual stimulation, leading to a dynamic and exciting relationship."},
#         "Scorpio": {"overall": 65, "communication": 70, "emotional": 65, "intimacy": 70, "explanation": "Sagittarius' love for adventure may clash with Scorpio's need for depth, but both are optimistic and enthusiastic."},
#         "Sagittarius": {"overall": 90, "communication": 85, "emotional": 80, "intimacy": 90, "explanation": "Both love adventure and freedom, making for a very dynamic and exciting relationship."},
#         "Capricorn": {"overall": 60, "communication": 55, "emotional": 60, "intimacy": 65, "explanation": "Capricorn's caution may frustrate Sagittarius' spontaneity, but both are loyal and committed."},
#         "Aquarius": {"overall": 80, "communication": 85, "emotional": 80, "intimacy": 85, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Pisces": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 75, "explanation": "Pisces' sensitivity may clash with Sagittarius' directness, but both are compassionate and caring."}
#     },
#     "Capricorn": {
#         "Aries": {"overall": 50, "communication": 45, "emotional": 55, "intimacy": 60, "explanation": "Capricorn's caution may frustrate Aries' spontaneity, but both are loyal and committed."},
#         "Taurus": {"overall": 90, "communication": 80, "emotional": 85, "intimacy": 90, "explanation": "Both are practical and ambitious, leading to a stable and successful relationship."},
#         "Gemini": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 60, "explanation": "Capricorn's caution may frustrate Gemini's need for variety, but both are loyal and committed."},
#         "Cancer": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 75, "explanation": "Both value security and stability, leading to a stable and committed relationship."},
#         "Leo": {"overall": 60, "communication": 55, "emotional": 60, "intimacy": 65, "explanation": "Capricorn's caution may frustrate Leo's spontaneity, but both are loyal and committed."},
#         "Virgo": {"overall": 80, "communication": 80, "emotional": 80, "intimacy": 85, "explanation": "Both are practical and ambitious, leading to a stable and successful relationship."},
#         "Libra": {"overall": 70, "communication": 75, "emotional": 70, "intimacy": 75, "explanation": "Capricorn's caution may frustrate Libra's need for harmony, but both are loyal and committed."},
#         "Scorpio": {"overall": 80, "communication": 75, "emotional": 85, "intimacy": 85, "explanation": "Both are intense and ambitious, leading to a stable and successful relationship."},
#         "Sagittarius": {"overall": 60, "communication": 55, "emotional": 60, "intimacy": 65, "explanation": "Capricorn's caution may frustrate Sagittarius' spontaneity, but both are loyal and committed."},
#         "Capricorn": {"overall": 90, "communication": 85, "emotional": 85, "intimacy": 90, "explanation": "Both are practical and ambitious, leading to a very stable and successful relationship."},
#         "Aquarius": {"overall": 70, "communication": 75, "emotional": 70, "intimacy": 75, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Pisces": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 80, "explanation": "Pisces' sensitivity may clash with Capricorn's practicality, but both are compassionate and caring."}
#     },
#     "Aquarius": {
#         "Aries": {"overall": 75, "communication": 80, "emotional": 65, "intimacy": 70, "explanation": "Both value independence and intellectual stimulation, but Aquarius' detachment may frustrate Aries."},
#         "Taurus": {"overall": 50, "communication": 60, "emotional": 45, "intimacy": 55, "explanation": "Aquarius' need for independence may frustrate Taurus' desire for closeness, but both value intellectual stimulation."},
#         "Gemini": {"overall": 85, "communication": 90, "emotional": 80, "intimacy": 85, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Cancer": {"overall": 50, "communication": 55, "emotional": 50, "intimacy": 55, "explanation": "Aquarius' need for independence may frustrate Cancer's need for closeness, but both value intellectual stimulation."},
#         "Leo": {"overall": 65, "communication": 70, "emotional": 60, "intimacy": 65, "explanation": "Aquarius' need for independence may frustrate Leo's need for attention, but both value intellectual stimulation."},
#         "Virgo": {"overall": 65, "communication": 70, "emotional": 60, "intimacy": 65, "explanation": "Aquarius' need for independence may frustrate Virgo's need for closeness, but both value intellectual stimulation."},
#         "Libra": {"overall": 80, "communication": 85, "emotional": 80, "intimacy": 85, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Scorpio": {"overall": 55, "communication": 60, "emotional": 50, "intimacy": 55, "explanation": "Aquarius' need for independence may frustrate Scorpio's need for depth, but both value intellectual stimulation."},
#         "Sagittarius": {"overall": 80, "communication": 85, "emotional": 80, "intimacy": 85, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Capricorn": {"overall": 70, "communication": 75, "emotional": 70, "intimacy": 75, "explanation": "Both value independence and intellectual stimulation, leading to a unique and intellectually stimulating relationship."},
#         "Aquarius": {"overall": 85, "communication": 90, "emotional": 85, "intimacy": 90, "explanation": "Both value independence and intellectual stimulation, leading to a very unique and intellectually stimulating relationship."},
#         "Pisces": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 75, "explanation": "Pisces' sensitivity may clash with Aquarius' detachment, but both are compassionate and caring."}
#     },
#     "Pisces": {
#         "Aries": {"overall": 60, "communication": 55, "emotional": 70, "intimacy": 65, "explanation": "Pisces' sensitivity may clash with Aries' directness, but both are compassionate and caring."},
#         "Taurus": {"overall": 70, "communication": 65, "emotional": 80, "intimacy": 75, "explanation": "Both are compassionate and sensitive, leading to a deep and empathetic relationship."},
#         "Gemini": {"overall": 60, "communication": 65, "emotional": 70, "intimacy": 65, "explanation": "Pisces' sensitivity may clash with Gemini's need for variety, but both are compassionate and caring."},
#         "Cancer": {"overall": 90, "communication": 85, "emotional": 95, "intimacy": 90, "explanation": "Both are deeply emotional and compassionate, leading to a very intimate and empathetic relationship."},
#         "Leo": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 70, "explanation": "Pisces' sensitivity may clash with Leo's directness, but both are compassionate and caring."},
#         "Virgo": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 70, "explanation": "Pisces' sensitivity may clash with Virgo's practicality, but both are compassionate and caring."},
#         "Libra": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 80, "explanation": "Pisces' sensitivity may clash with Libra's need for harmony, but both are compassionate and caring."},
#         "Scorpio": {"overall": 85, "communication": 80, "emotional": 90, "intimacy": 90, "explanation": "Both are deeply emotional and compassionate, leading to a very intimate and transformative relationship."},
#         "Sagittarius": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 75, "explanation": "Pisces' sensitivity may clash with Sagittarius' directness, but both are compassionate and caring."},
#         "Capricorn": {"overall": 75, "communication": 70, "emotional": 80, "intimacy": 80, "explanation": "Pisces' sensitivity may clash with Capricorn's practicality, but both are compassionate and caring."},
#         "Aquarius": {"overall": 70, "communication": 65, "emotional": 75, "intimacy": 75, "explanation": "Pisces' sensitivity may clash with Aquarius' detachment, but both are compassionate and caring."},
#         "Pisces": {"overall": 90, "communication": 85, "emotional": 95, "intimacy": 95, "explanation": "Both are deeply emotional and compassionate, leading to a very intimate and empathetic relationship."}
#     }
# }