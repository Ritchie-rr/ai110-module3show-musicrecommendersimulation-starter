# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
**Vibe commander 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

A song recommender that will recommend songs similar in style and in vibe. It makes the assumption that the user only wants to listen to similar songs songs. This is for classroom exploration.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The user profile describes what kind of music a person likes, how much energy, and how positive the vibe should be. The system then awards points based on how closely a song is to the profile. Genre match is worth the most. Then after getting the scores, they are ranked in order and the highest 5 scores are what gets recommended.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The model uses 18 songs across 15 genres (pop, rock, lofi, jazz, hip-hop, and more) and 14 moods (happy, chill, intense, melancholic, etc.). I added data for more variation of genres. The catalog is small, uneven, and there are some parts of musical that were not included.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well when the user's preferred genre exists in the catalog and their energy level is close to the songs available. In those cases the top results felt very natural and matched was what you'd expect a real playlist to look like.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

Energy is the highest-weighted feature (2.5 pts), so it can override a user's genre and mood preferences, creating a filter bubble for high-energy listeners. Genre scoring is binary therefore a missing or niche genre earns 0 pts every time, pushing those users into energy-only matching that ignores their actual taste. Danceability silently boosts danceable songs for every user, and the "focused" mood has no group neighbors, so focused users can never earn partial mood credit.



---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

Seven profiles were tested — three normal listeners and four tricky edge cases. For normal listeners, results made sense. The surprising case was "Energetic but Sad": this profile wanted sad pop but kept getting Gym Hero, a workout anthem, because the system cares more about how pumped-up a song feels than what emotion it carries.  Asking for extreme preferences (everything maxed to 1.0) actually gave worse results than a normal request, and users whose favorite genre wasn't in the catalog got recommendations that had nothing to do with their taste with no explanation why.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Improve the amount of data that is taken in, add front end/ UI, and allow user input. A feature to decide how close you want the recommendations to be would also be nice or manually putting certain attributes worth different.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I have learned how the data in the recommender system is very important for it to work correctly. Recommending songs is a hard task. I found it very interesting to know how spotify recommends songs.
