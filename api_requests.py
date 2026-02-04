"""
api_requests_demo.py
Demonstrates usage of requests library and public API
"""

# 2. Install and import requests library
# pip install requests   (run once in terminal)

import requests


# -----------------------------
# Function to fetch a random quote
# -----------------------------

def fetch_random_quote():
    url = "https://api.quotable.io/random"

    try:
        # 4. Send GET request
        response = requests.get(url, timeout=5)

        # Inspect status code
        if response.status_code == 200:
            # 5. Parse JSON response
            data = response.json()

            # 6. Extract required fields from nested JSON
            quote = data.get("content")
            author = data.get("author")
            tags = data.get("tags")

            # 8. Format and display clean output
            print("\n📜 Random Quote")
            print("-" * 40)
            print(f"\"{quote}\"")
            print(f"— {author}")
            print(f"Tags: {', '.join(tags)}")

        else:
            # 7. Handle API errors
            print(f"❌ Failed to fetch quote. Status Code: {response.status_code}")

    except requests.exceptions.Timeout:
        print("❌ Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("❌ Network error. Check your internet connection.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Unexpected error occurred: {e}")


# -----------------------------
# Main Program
# -----------------------------

def main():
    print("=== Public API Demo using requests ===")
    fetch_random_quote()


if __name__ == "__main__":
    main()
