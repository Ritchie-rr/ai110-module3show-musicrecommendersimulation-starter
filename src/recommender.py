from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
import os

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with a list of Song objects."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs best matching the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable string explaining why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file, converting numeric fields to int/float."""
    # Construct absolute path relative to this file's location (src/)
    # Go up one level (..) to project root, then access data/songs.csv
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    full_path = os.path.join(project_root, csv_path)
    
    songs = []
    
    # Define which fields need type conversion
    int_fields = {'id'}
    float_fields = {'energy', 'valence', 'danceability', 'acousticness', 'tempo_bpm'}
    
    with open(full_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert integer fields
            for field in int_fields:
                if field in row and row[field]:
                    row[field] = int(row[field])
            
            # Convert float fields (for numerical scoring later)
            for field in float_fields:
                if field in row and row[field]:
                    row[field] = float(row[field])
            
            songs.append(row)
    
    print(f"Loaded songs: {len(songs)}")
    return songs


# Mood grouping for partial credit in scoring
MOOD_GROUPS = {
    "energetic": ["happy", "intense", "confident", "energetic"],
    "chill": ["chill", "relaxed", "mellow"],
    "focused": ["focused"],
    "moody": ["moody", "melancholic", "dark"],
    "nostalgic": ["nostalgic"],
    "romantic": ["romantic"]
}


def compute_genre_points(user_genre: str, song_genre: str) -> Tuple[float, str]:
    """Return +2.0 points for an exact genre match, 0.0 otherwise."""
    if user_genre.lower() == song_genre.lower():
        return 2.0, f"exact genre match ({song_genre})"
    return 0.0, f"genre mismatch (wanted {user_genre}, got {song_genre})"


def compute_mood_points(user_mood: str, song_mood: str) -> Tuple[float, str]:
    """Return 1.0 for exact mood match, 0.8 for same mood group, 0.0 otherwise."""
    if user_mood == song_mood:
        return 1.0, f"exact mood match ({song_mood})"
    
    # Check if both moods are in the same group
    for group, moods in MOOD_GROUPS.items():
        if user_mood in moods and song_mood in moods:
            return 0.8, f"mood group match ({user_mood} ≈ {song_mood})"
    
    return 0.0, f"mood mismatch (wanted {user_mood}, got {song_mood})"


def compute_energy_points(user_energy: float, song_energy: float) -> Tuple[float, str]:
    """
    Compute energy similarity points: 0 to 2.5 based on closeness.
    Formula: (1 - |user_energy - song_energy|) * 2.5
    Returns (points, reason_string)
    """
    similarity = 1 - abs(user_energy - song_energy)
    points = similarity * 2.5
    return points, f"energy similarity ({points:.2f}pts)"


def compute_valence_points(user_valence: float, song_valence: float) -> Tuple[float, str]:
    """
    Compute valence (positivity) similarity points: 0 to 2.0 based on closeness.
    Formula: (1 - |user_valence - song_valence|) * 2.0
    Returns (points, reason_string)
    """
    similarity = 1 - abs(user_valence - song_valence)
    points = similarity * 2.0
    return points, f"valence similarity ({points:.2f}pts)"


def compute_danceability_points(song_danceability: float) -> Tuple[float, str]:
    """
    Compute danceability bonus: 0 to 0.5 proportional to song's danceability.
    Formula: song_danceability * 0.5
    Returns (points, reason_string)
    """
    points = song_danceability * 0.5
    return points, f"danceability bonus ({points:.2f}pts)"


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Calculate total score for a song based on user preferences.
    
    Args:
        user_prefs: Dictionary with keys: genre, mood, energy, target_valence
        song: Dictionary with song data from CSV
    
    Returns:
        Tuple of (total_score, list_of_reasons)
        - total_score: float from 0 to 8.0
        - list_of_reasons: list of strings explaining each component
    
    Scoring breakdown (max 8.0):
    - Genre: +2.0 points
    - Mood: +0.0 to +1.0 points
    - Energy: +0.0 to +2.5 points
    - Valence: +0.0 to +2.0 points
    - Danceability: +0.0 to +0.5 points
    """
    reasons = []
    
    # Extract user preferences (with defaults for missing fields)
    user_genre = user_prefs.get("genre", "pop")
    user_mood = user_prefs.get("mood", "happy")
    user_energy = user_prefs.get("energy", 0.5)
    user_valence = user_prefs.get("target_valence", 0.6)
    
    # Extract song features
    song_genre = song.get("genre", "")
    song_mood = song.get("mood", "")
    song_energy = song.get("energy", 0.5)
    song_valence = song.get("valence", 0.5)
    song_danceability = song.get("danceability", 0.0)
    
    # Compute points for each feature
    genre_pts, genre_reason = compute_genre_points(user_genre, song_genre)
    mood_pts, mood_reason = compute_mood_points(user_mood, song_mood)
    energy_pts, energy_reason = compute_energy_points(user_energy, song_energy)
    valence_pts, valence_reason = compute_valence_points(user_valence, song_valence)
    dance_pts, dance_reason = compute_danceability_points(song_danceability)
    
    # Build reasons list
    reasons.append(genre_reason)
    reasons.append(mood_reason)
    reasons.append(energy_reason)
    reasons.append(valence_reason)
    reasons.append(dance_reason)
    
    # Calculate total score
    total_score = genre_pts + mood_pts + energy_pts + valence_pts + dance_pts
    
    return total_score, reasons


def _format_recommendation(user_prefs: Dict, song: Dict) -> Tuple[Dict, float, str]:
    """
    Helper function to score a song and format it as a recommendation.
    
    Args:
        user_prefs: User preference dictionary
        song: Song dictionary to score
    
    Returns:
        Tuple of (song_dict, score, explanation_string)
    """
    score, reasons = score_song(user_prefs, song)
    explanation = ", ".join(reasons[:3])  # Top 3 reasons
    return (song, score, explanation)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Find the best songs by scoring every track in the catalog using score_song as judge.
    
    Args:
        user_prefs: Dictionary with user preferences (genre, mood, energy, target_valence)
        songs: List of song dictionaries from CSV
        k: Number of top recommendations to return (default: 5)
    
    Returns:
        List of top-k tuples: (song_dict, score, explanation_string)
        sorted from highest to lowest score
    """
    # Score every song using list comprehension (Pythonic approach)
    scored_songs = [_format_recommendation(user_prefs, song) for song in songs]
    
    # Sort by score descending and return top-k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
