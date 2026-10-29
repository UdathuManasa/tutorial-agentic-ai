"""
Reviews API - reads from the `reviews` table in store.db and returns
aggregated rating information for products.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")

def get_product_rating(product_id: int) -> dict:
    """Fetches aggregated rating information for a specific product."""
    if not os.path.exists(DB_PATH):
        return {"product_id": product_id, "average_rating": 0.0, "total_reviews": 0}
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT  AVG(rating),COUNT(*)
        FROM reviews
        WHERE product_id = ?
    """, (product_id,))
    
    row = cursor.fetchone()
    conn.close()
    
    total_reviews = row[1] if row and row[1] is not None else 0
    average_rating = round(row[0], 2) if row and row[0] is not None else 0.0
    
    return {
        "product_id": product_id,
        "average_rating": average_rating,
        "total_reviews": total_reviews
    }

def get_ratings_for_products(products_ids: list[int]) -> list[dict]:
    """Fetches aggregated rating information for a list of product IDs."""
    if not products_ids or not os.path.exists(DB_PATH):
        return []
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Use placeholders (?, ?, ...) for safe parameter substitution in an IN clause
    placeholders = ','.join(['?'] * len(products_ids))
    query = f"""
        SELECT product_id, COUNT(*), AVG(rating)
        FROM reviews
        WHERE product_id IN ({placeholders})
        GROUP BY product_id
    """
    
    cursor.execute(query, products_ids)
    rows = cursor.fetchall()
    conn.close()
    
    # Map results into a dictionary for easy lookup
    ratings_map = {}
    for row in rows:
        p_id, total, avg = row
        ratings_map[p_id] = {
            "product_id": p_id,
            "average_rating": round(avg, 2) if avg is not None else 0.0,
            "total_reviews": total if total is not None else 0
        }
    
    # Ensure every requested product ID is returned, defaulting to 0 if it has no reviews
    result = []
    for p_id in products_ids:
        if p_id in ratings_map:
            result.append(ratings_map[p_id])
        else:
            result.append({
                "product_id": p_id,
                "average_rating": 0.0,
                "total_reviews": 0
            })
            
    return result


if __name__ == "__main__":
    print("--- Testing Single Product Rating ---")
    single_test_id = 1
    single_res = get_product_rating(single_test_id)
    print(single_res)

    print("\n--- Testing Batch Product Ratings ---")
    # Testing existing IDs (1, 2, 3) and a non-existent ID (999) to verify handling
    batch_test_ids = [1, 2, 3, 999]
    batch_res = get_ratings_for_products(batch_test_ids)
    for item in batch_res:
        print(item)