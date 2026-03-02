# Simple book recommendation system
from dummy_users import users
from books_db import books

# Recommend books based on user's favorite themes

def recommend_books(user_id, top_n=5):
    user = next((u for u in users if u["user_id"] == user_id), None)
    if not user:
        return []
    # Get themes from user's favorite books
    favorite_book_ids = user["favorite_books"]
    favorite_themes = set([b["theme"] for b in books if b["book_id"] in favorite_book_ids])
    # Recommend books with matching themes, excluding already accessed
    recommended = [b for b in books if b["theme"] in favorite_themes and b["book_id"] not in favorite_book_ids]
    # Sort by book_id for demo, can be improved
    recommended = sorted(recommended, key=lambda x: x["book_id"])
    return recommended[:top_n]

# Example usage
if __name__ == "__main__":
    user_id = 1
    recs = recommend_books(user_id)
    print(f"Rekomendasi untuk user {user_id}:")
    for book in recs:
        print(f"- {book['title']} ({book['theme']})")
