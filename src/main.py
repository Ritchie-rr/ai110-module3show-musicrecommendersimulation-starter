"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    user_prefs = {"genre": "jazz", "mood": "chill", "energy": 0.4, "target_valence": 0.6}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*60)
    print("TOP 5 RECOMMENDATIONS")
    print("="*60 + "\n")
    
    for i, rec in enumerate(recommendations, 1):
        # Unpack recommendation tuple
        song, score, explanation = rec
        
        # Format: ordered number, title, score on one line
        print(f"{i}. {song['title']} ({score:.2f} pts)")
        
        # Explanation on indented line below
        print(f"   {explanation}\n")


if __name__ == "__main__":
    main()
