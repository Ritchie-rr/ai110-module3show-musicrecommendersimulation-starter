# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Real world recommenders use a mix of Collaboartive filtering (user behavior based) and content based filtering(song atribute).

Our recommender will use a scoring rule that will gauge how much the user will like the song based on user behavior. It will combine that with a ranking rule that will choose the highest scoring rule out of a group of scored songs.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Song: genre, mood, energy, valence, and danceability used for recommonding.

User Profile:  favorite_genre, favorite_mood, target_energy, and target_valence

Recommender: Uses a weighted-sum formula combining energy, valence, mood, genre, and danceability matches to score each song. Then it selects the top-k highest-scoring songs to recommend.

The dataset overrepresents lofi/pop, reinforces stereotypical mood-energy linking (happy→energetic, angry→low-energy), excludes non-Western music, and offers only 18 polarized songs that may systematically disadvantage users seeking mid-energy or genre-diverse recommendations.



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"


## 10 images

```
============================================================
TOP 5 RECOMMENDATIONS — High-Energy Pop
============================================================

1. Gym Hero (7.50 pts)
   exact genre match (pop), mood group match (energetic ~= intense), energy similarity (2.42pts)

2. Sunrise City (7.47 pts)
   exact genre match (pop), mood group match (energetic ~= happy), energy similarity (2.30pts)

3. Neon Dreams (5.74 pts)
   genre mismatch (wanted pop, got electronic), exact mood match (energetic), energy similarity (2.45pts)

4. Rooftop Lights (5.28 pts)
   genre mismatch (wanted pop, got indie pop), mood group match (energetic ~= happy), energy similarity (2.15pts)

5. Urban Pulse (5.10 pts)
   genre mismatch (wanted pop, got hip-hop), mood group match (energetic ~= confident), energy similarity (2.23pts)

============================================================
TOP 5 RECOMMENDATIONS — Chill Lofi
============================================================

1. Library Rain (7.26 pts)
   exact genre match (lofi), exact mood match (chill), energy similarity (2.38pts)

2. Midnight Coding (7.19 pts)
   exact genre match (lofi), exact mood match (chill), energy similarity (2.20pts)

3. Focus Flow (6.17 pts)
   exact genre match (lofi), mood mismatch (wanted chill, got focused), energy similarity (2.25pts)

4. Spacewalk Thoughts (5.16 pts)
   genre mismatch (wanted lofi, got ambient), exact mood match (chill), energy similarity (2.45pts)

5. Coffee Shop Stories (4.78 pts)
   genre mismatch (wanted lofi, got jazz), mood group match (chill ~= relaxed), energy similarity (2.32pts)

============================================================
TOP 5 RECOMMENDATIONS — Deep Intense Rock
============================================================

1. Storm Runner (7.32 pts)
   exact genre match (rock), exact mood match (intense), energy similarity (2.35pts)

2. Urban Pulse (4.80 pts)
   genre mismatch (wanted rock, got hip-hop), mood group match (intense ~= confident), energy similarity (2.35pts)

3. Gym Hero (4.80 pts)
   genre mismatch (wanted rock, got pop), exact mood match (intense), energy similarity (2.30pts)

4. Neon Dreams (4.69 pts)
   genre mismatch (wanted rock, got electronic), mood group match (intense ~= energetic), energy similarity (2.42pts)

5. Crimson Wave (4.54 pts)
   genre mismatch (wanted rock, got metal), mood mismatch (wanted intense, got angry), energy similarity (2.23pts)

============================================================
TOP 5 RECOMMENDATIONS — Energetic but Sad
============================================================

1. Gym Hero (5.42 pts)
   exact genre match (pop), mood mismatch (wanted melancholic, got intense), energy similarity (2.42pts)

2. Sunrise City (5.12 pts)
   exact genre match (pop), mood mismatch (wanted melancholic, got happy), energy similarity (2.30pts)

3. Night Drive Loop (4.41 pts)
   genre mismatch (wanted pop, got synthwave), mood group match (melancholic ~= moody), energy similarity (2.12pts)

4. Whispers In The Dark (4.33 pts)
   genre mismatch (wanted pop, got alternative), mood group match (melancholic ~= dark), energy similarity (1.80pts)

5. Crimson Wave (4.25 pts)
   genre mismatch (wanted pop, got metal), mood mismatch (wanted melancholic, got angry), energy similarity (2.35pts)

============================================================
TOP 5 RECOMMENDATIONS — Perfect Extremes
============================================================

1. Storm Runner (6.57 pts)
   exact genre match (rock), exact mood match (intense), energy similarity (2.27pts)

2. Gym Hero (5.31 pts)
   genre mismatch (wanted rock, got pop), exact mood match (intense), energy similarity (2.33pts)

3. Neon Dreams (4.99 pts)
   genre mismatch (wanted rock, got electronic), mood group match (intense ~= energetic), energy similarity (2.20pts)

4. Sunrise City (4.92 pts)
   genre mismatch (wanted rock, got pop), mood group match (intense ~= happy), energy similarity (2.05pts)

5. Rooftop Lights (4.73 pts)
   genre mismatch (wanted rock, got indie pop), mood group match (intense ~= happy), energy similarity (1.90pts)

============================================================
TOP 5 RECOMMENDATIONS — Dead Zone
============================================================

1. Spacewalk Thoughts (5.71 pts)
   exact genre match (ambient), exact mood match (chill), energy similarity (1.80pts)

2. Library Rain (3.71 pts)
   genre mismatch (wanted ambient, got lofi), exact mood match (chill), energy similarity (1.62pts)

3. Midnight Coding (3.64 pts)
   genre mismatch (wanted ambient, got lofi), exact mood match (chill), energy similarity (1.45pts)

4. Coffee Shop Stories (3.23 pts)
   genre mismatch (wanted ambient, got jazz), mood group match (chill ~= relaxed), energy similarity (1.57pts)

5. Sunset Vibes (2.98 pts)
   genre mismatch (wanted ambient, got reggae), mood group match (chill ~= mellow), energy similarity (1.30pts)

============================================================
TOP 5 RECOMMENDATIONS — Genre Ghost
============================================================

1. Focus Flow (5.12 pts)
   genre mismatch (wanted zydeco, got lofi), exact mood match (focused), energy similarity (2.00pts)

2. Whispers In The Dark (4.37 pts)
   genre mismatch (wanted zydeco, got alternative), mood mismatch (wanted focused, got dark), energy similarity (2.45pts)

3. Midnight Coding (4.24 pts)
   genre mismatch (wanted zydeco, got lofi), mood mismatch (wanted focused, got chill), energy similarity (2.05pts)

4. Soul Serenade (4.16 pts)
   genre mismatch (wanted zydeco, got soul), mood mismatch (wanted focused, got romantic), energy similarity (2.30pts)
```

