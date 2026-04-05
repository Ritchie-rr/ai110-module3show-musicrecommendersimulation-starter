"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop":   {"genre": "pop",     "mood": "energetic", "energy": 0.9,  "target_valence": 0.85},
    "Chill Lofi":        {"genre": "lofi",    "mood": "chill",     "energy": 0.3,  "target_valence": 0.4},
    "Deep Intense Rock": {"genre": "rock",    "mood": "intense",   "energy": 0.85, "target_valence": 0.3},
    # --- Adversarial / Edge Case Profiles ---
    # Conflicting: high energy but deeply sad — energy score should be high, valence should suffer
    "Energetic but Sad": {"genre": "pop",     "mood": "melancholic", "energy": 0.9,  "target_valence": 0.05},
    # Boundary: everything maxed — tests upper-limit scoring math
    "Perfect Extremes":  {"genre": "rock",    "mood": "intense",     "energy": 1.0,  "target_valence": 1.0},
    # Boundary: everything zeroed — tests lower-limit / zero-division safety
    "Dead Zone":         {"genre": "ambient", "mood": "chill",       "energy": 0.0,  "target_valence": 0.0},
    # Genre that likely doesn't exist in the catalog — mood+energy become the only differentiators
    "Genre Ghost":       {"genre": "zydeco",  "mood": "focused",     "energy": 0.6,  "target_valence": 0.5},
}


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "="*60)
        print(f"TOP 5 RECOMMENDATIONS — {profile_name}")
        print("="*60 + "\n")

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"{i}. {song['title']} ({score:.2f} pts)")
            print(f"   {explanation}\n")


if __name__ == "__main__":
    main()
