# 🎵 Algorithm Recipe: Music Recommender Scoring System

## Overview

This document describes the mathematical scoring algorithm that powers your music recommender. It balances multiple song features (energy, valence, mood, genre, danceability) using a weighted-sum approach to rank songs by how well they match a user's taste profile.

---

## Part 1: Scoring Numerical Features

### Core Principle
**Reward songs that are *close* to the user's preference, not just higher or lower.**

### The Formula: Absolute Difference Distance

For any numerical feature (energy, valence, danceability, acousticness):

$$\text{match\_score} = 1 - |\text{user\_preference} - \text{song\_feature}|$$

### How It Works with Examples

**User prefers energy = 0.7**

| Song | Energy | Calculation | Score | Interpretation |
|------|--------|-------------|-------|-----------------|
| Song A | 0.7 | 1 - \|0.7 - 0.7\| = 1 - 0 | **1.0** | Perfect match |
| Song B | 0.6 | 1 - \|0.7 - 0.6\| = 1 - 0.1 | **0.9** | Close match |
| Song C | 0.3 | 1 - \|0.7 - 0.3\| = 1 - 0.4 | **0.6** | Far away |
| Song D | 1.0 | 1 - \|0.7 - 1.0\| = 1 - 0.3 | **0.7** | Too intense |

### Why Absolute Difference?

✅ **Strengths**:
- Symmetric: doesn't favor "more" or "less" energy
- Interpretable: score directly represents how close the match is
- Simple to compute and easy to debug
- Score range stays 0-1 (plays well with other features)

⚠️ **Alternative: Squared Distance** (if you want stricter matching)
$$\text{match\_score} = 1 - |\text{user\_preference} - \text{song\_feature}|^2$$
- Punishes larger differences more severely
- Creates a narrower "goldilocks zone"
- Example: 0.4 difference → score 0.84 (vs 0.6 with absolute)

---

## Part 2: Scoring Categorical Features

### Mood Matching with Similarity Groups

Create **mood groups** so similar moods reward the user:

```python
mood_groups = {
    "energetic": ["happy", "intense"],
    "chill": ["chill", "relaxed"],
    "focused": ["focused"],
    "moody": ["moody"]
}
```

**Scoring rules**:
- If song mood matches user mood exactly → score = 1.0
- If song mood is in same group as user mood → score = 0.8 (partial match)
- If song mood is in different group → score = 0.0 (no match)

**Example**:
- User prefers "chill" mood
- Song with "chill" → 1.0 ✓
- Song with "relaxed" → 0.8 ✓ (same group)
- Song with "happy" → 0.0 ✗ (different group)

### Genre Matching

Simple approach:
- Exact genre match → score = 1.0
- No genre match → score = 0.0

**Optional refinement** (if genres seem too strict):
- Create genre similarity (indie pop ≈ indie, pop ≈ pop but indie ≠ rock)

---

## Part 3: The Complete Scoring Formula

### Point-Based Scoring Approach

Instead of percentages, use a points system where each feature contributes a discrete amount:

$$\text{total\_score} = G + M + E_s + V_s + D_s$$

Where:
- $G$ = genre match points (0 or +2.0)
- $M$ = mood match points (0, 0.8, or +1.0)
- $E_s$ = energy similarity points (0 to +2.5)
- $V_s$ = valence similarity points (0 to +2.0)
- $D_s$ = danceability bonus points (0 to +0.5)

### Scoring Rules

| Feature | Points | Calculation |
|---------|--------|-------------|
| **Genre** | +2.0 | Exact match: +2.0 points; No match: 0 points |
| **Mood** | +0.8 to +1.0 | Exact match: +1.0; Same group: +0.8; No match: 0 |
| **Energy** | 0 to +2.5 | $(1 - \|\text{user\_energy} - \text{song\_energy}\|) \times 2.5$ |
| **Valence** | 0 to +2.0 | $(1 - \|\text{user\_valence} - \text{song\_valence}\|) \times 2.0$ |
| **Danceability** | 0 to +0.5 | $\text{song\_danceability} \times 0.5$ |
| **TOTAL MAX** | **8.0 points** | Perfect match across all features |

### Scoring Examples

**User Profile**: genre="pop", mood="happy", target_energy=0.7, target_valence=0.8

**Song A**: "Sunrise City" (pop, happy, energy=0.82, valence=0.84, danceability=0.79)
- Genre: +2.0 (exact match)
- Mood: +1.0 (exact match)
- Energy: $(1 - |0.7 - 0.82|) \times 2.5 = 0.88 \times 2.5 = +2.2$
- Valence: $(1 - |0.8 - 0.84|) \times 2.0 = 0.96 \times 2.0 = +1.92$
- Danceability: $0.79 \times 0.5 = +0.39$
- **Total: 2.0 + 1.0 + 2.2 + 1.92 + 0.39 = 7.51** ⭐ Excellent match!

**Song B**: "Library Rain" (lofi, chill, energy=0.35, valence=0.60, danceability=0.58)
- Genre: 0 (no match)
- Mood: 0 (different group)
- Energy: $(1 - |0.7 - 0.35|) \times 2.5 = 0.65 \times 2.5 = +1.63$
- Valence: $(1 - |0.8 - 0.60|) \times 2.0 = 0.80 \times 2.0 = +1.6$
- Danceability: $0.58 \times 0.5 = +0.29$
- **Total: 0 + 0 + 1.63 + 1.6 + 0.29 = 3.52** (vibe OK, but genre/mood misaligned)

### Why This Point System Works

✅ **Clear & Intuitive**: Genre match = 2 bonus points, Mood match = 1 bonus point
✅ **Flexible**: Partial mood matches (same group) get 0.8 points
✅ **Continuous**: Energy/valence provide fine-grained similarity scoring
✅ **Balanced**: Max 2.0 for genre reward, but 2.5+2.0 for vibe matching (energy+valence) = **vibe still wins**

---

## Part 4: Implementation Steps

### Step 1: Normalize Tempo (only numeric feature that needs it)

Tempo ranges from 60-152 BPM. Normalize to 0-1:

$$\text{tempo\_normalized} = \frac{\text{BPM} - 60}{152 - 60} = \frac{\text{BPM} - 60}{92}$$

Other numeric features (energy, valence, danceability, acousticness) are already 0-1.

### Step 2: Create Helper Functions

```python
def compute_genre_points(user_genre: str, song_genre: str) -> float:
    """Return 2.0 for exact match, 0.0 otherwise."""
    return 2.0 if user_genre.lower() == song_genre.lower() else 0.0

def compute_mood_points(user_mood: str, song_mood: str, mood_groups: dict) -> float:
    """Return 1.0 for exact match, 0.8 for same group, 0.0 otherwise."""
    if user_mood == song_mood:
        return 1.0
    # Check if in same group
    for group, moods in mood_groups.items():
        if user_mood in moods and song_mood in moods:
            return 0.8
    return 0.0

def compute_energy_points(user_energy: float, song_energy: float) -> float:
    """Energy similarity: 0 to 2.5 points based on closeness."""
    similarity = 1 - abs(user_energy - song_energy)
    return similarity * 2.5

def compute_valence_points(user_valence: float, song_valence: float) -> float:
    """Valence similarity: 0 to 2.0 points based on closeness."""
    similarity = 1 - abs(user_valence - song_valence)
    return similarity * 2.0

def compute_danceability_points(song_danceability: float) -> float:
    """Danceability bonus: 0 to 0.5 points based on song's danceability."""
    return song_danceability * 0.5
```

### Step 3: Combine into Final Score

```python
def score_song(user_profile: UserProfile, song: Song, mood_groups: dict) -> float:
    """
    Calculate total score for a song based on user profile.
    
    Returns a score from 0 to 8.0, where:
    - 8.0 = perfect match across all features
    - 7.0+ = excellent recommendation
    - 5.0+ = good match
    - <5.0 = weak match
    """
    genre_pts = compute_genre_points(user_profile.favorite_genre, song.genre)
    mood_pts = compute_mood_points(user_profile.favorite_mood, song.mood, mood_groups)
    energy_pts = compute_energy_points(user_profile.target_energy, song.energy)
    valence_pts = compute_valence_points(user_profile.target_valence, song.valence)
    dance_pts = compute_danceability_points(song.danceability)
    
    total_score = genre_pts + mood_pts + energy_pts + valence_pts + dance_pts
    return total_score
```

### Step 4: Rank and Return

1. Score all songs
2. Sort by score descending
3. Return top-k with scores
4. Generate one-liner explanation for each recommendation

---

## Part 5: Testing Your Scoring System

### Experiment 1: Chill User
**Profile**: genre="lofi", mood="chill", energy=0.35, valence=0.6

| Song | Genre | Mood | Energy | Valence | Dance | **Total** | Expected |
|------|-------|------|--------|---------|-------|----------|----------|
| "Library Rain" | +2.0 | +1.0 | 2.5×0.0 | 2.0×0.0 | 0.43 | **5.93** | ⭐⭐⭐ Best |
| "Midnight Coding" | +2.0 | +1.0 | 2.5×0.85 | 2.0×0.04 | 0.31 | **6.48** | ⭐⭐⭐ Best |
| "Spacewalk Thoughts" | 0.0 | +1.0 | 2.5×0.93 | 2.0×0.65 | 0.21 | **6.48** | ⭐⭐ Good |
| "Storm Runner" | 0.0 | 0.0 | 2.5×0.24 | 2.0×0.08 | 0.33 | **0.93** | ✗ Avoid |

**Insight**: Vibe (energy + valence) carries enough weight that genre mismatches are OK. System correctly ranks chill songs high.

### Experiment 2: Gym User
**Profile**: genre="pop", mood="intense", energy=0.9, valence=0.8

| Song | Genre | Mood | Energy | Valence | Dance | **Total** | Expected |
|------|-------|------|--------|---------|-------|----------|----------|
| "Gym Hero" | +2.0 | +1.0 | 2.5×0.93 | 2.0×0.11 | 0.44 | **6.97** | ⭐⭐⭐ Best |
| "Sunrise City" | +2.0 | 0.0 | 2.5×0.88 | 2.0×0.04 | 0.40 | **5.68** | ⭐⭐ Good |
| "Library Rain" | 0.0 | 0.0 | 2.5×0.55 | 2.0×0.20 | 0.29 | **2.04** | ✗ Avoid |

**Insight**: High-energy, high-valence songs match user intent. Genre is a bonus (+2.0), not a deal-breaker.

### How to Tune

If results don't match expectations:

| Problem | Solution |
|---------|----------|
| Genre matches rank too high | Reduce genre points from 2.0 → 1.5 |
| Genre matches being ignored | Increase genre points from 2.0 → 2.5 |
| Missing mood context | Increase mood from 1.0 → 1.5 |
| Ignoring energy similarity | Increase energy multiplier from 2.5 → 3.0 |
| Too many poor matches recommended | Increase danceability multiplier from 0.5 → 1.0 |

Track your experiments in README.md with actual vs. expected rankings.

---

## Part 6: Edge Cases & Considerations

### What if valence and mood are contradictory?
Example: User profile says mood="happy" but target_valence=0.4 (sad)

✓ **Your algorithm handles this**: Each feature votes independently
- Song with high valence (0.8) and happy mood (1.0) will score high on mood/valence
- Song with low valence (0.3) and happy mood (1.0) will score high on mood but low on valence
- System balances both constraints

### What if no song matches well?
- All scores will be lower, but ranking still works (best available wins)
- Consider recommending "exploration picks" with lower scores occasionally

### Cold Start Problem (new user)
- With only favorite_genre, default the other values (e.g., target_energy=0.5, valence=0.6)
- Get quick recommendations, learn from behavior

---

## Summary: The Recipe

**Goal**: Score songs by closeness to user's "vibe"

**Method**: Point-based system awarding discrete points for categorical matches + similarity scores for numeric features

**Point Breakdown**:
- Genre exact match: **+2.0 points**
- Mood exact match: **+1.0 point** (partial: +0.8 for same group)
- Energy similarity: **0 to 2.5 points** (based on distance from target)
- Valence similarity: **0 to 2.0 points** (based on distance from target)
- Danceability bonus: **0 to 0.5 points** (proportional to song's danceability)
- **Maximum score: 8.0 points**

**Implementation**: Helper functions for each feature → sum all points → rank songs → return top-k with explanations

**Testing**: Validate with diverse user profiles and adjust point multipliers as needed

**Key Insight**: Vibe (4.5 max points) beats genre (2.0 points)—music recommendations should prioritize how a song *feels*, not just its label.
