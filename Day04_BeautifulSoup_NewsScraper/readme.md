
---

````markdown
# 📰 Scraping Headlines From News Websites Using BeautifulSoup in Python

## 🧠 Big Picture: What This Script Does

Your goal:
👉 “Visit a news website → read the webpage → pick out headline text → print it.”

So, our Python program does **4 main things**:

1. **Get** the webpage’s HTML (using `requests`)
2. **Parse** the HTML (using `BeautifulSoup`)
3. **Find** all headline tags (like `<h2>` or `<h3>`)
4. **Extract** text and **print** the headlines

---

## 🧩 Let’s Break Down the Code

### 🧱 1. Importing Libraries

```python
import requests
from bs4 import BeautifulSoup
````

* **`requests`** → lets Python visit web pages like a browser.
* **`BeautifulSoup`** → helps Python read and understand the messy HTML code of a webpage.

---

### ⚙️ 2. Defining a Function

```python
def get_news_headlines(url):
    """
    Extracts news headlines from the provided news website URL.
    """
```

* `def` means we are defining a **function** — a reusable block of code.
* The function name is `get_news_headlines`, and it takes one input — the **URL** of the website we want to scrape.
* The triple quotes (`""" """`) define a **docstring** — a short description of what the function does.

Example usage:

```python
get_news_headlines("https://www.bbc.com/news")
```

---

### 🌐 3. Sending a Request to the Website

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching the URL: {e}")
    return []
```

* `requests.get(url)` → sends a GET request (like opening the page in your browser).
* `response.text` → contains the HTML content.
* `response.status_code` → 200 means success, 404 means “not found.”
* `response.raise_for_status()` → automatically throws an error for bad responses.
* `try...except` → prevents your program from crashing if something goes wrong (like no internet or invalid URL).

---

### 🧠 4. Parsing the HTML

```python
soup = BeautifulSoup(response.text, 'lxml')
```

* Converts the HTML code into a **structured format** you can search.
* `'lxml'` is a fast and powerful parser that helps BeautifulSoup read HTML properly.

Example:

```python
soup.find_all('h2')
```

→ Finds all `<h2>` tags.

---

### 📰 5. Finding Headline Elements

```python
headline_elements = soup.find_all(['h2', 'h3'])
```

* `.find_all()` → looks through the HTML and finds all tags matching your list.
* Here, we’re finding all `<h2>` and `<h3>` tags.
* Most news sites (like BBC, CNN, etc.) use these tags for headlines.

---

### ✂️ 6. Extracting Text from Each Tag

```python
headlines = []
for element in headline_elements:
    headline_text = element.get_text(strip=True)
    if headline_text and len(headline_text.split()) > 3:
        headlines.append(headline_text)
```

* Start with an empty list `headlines = []`.
* Loop through each element found in the HTML.
* `element.get_text(strip=True)` removes HTML tags and keeps clean text.
* The `if` condition ensures:

  * It’s not empty (`headline_text`)
  * It has more than 3 words (to skip short labels like “Home”, “Menu”)
* Add valid headlines to the list using `.append()`.

---

### 🚫 7. Removing Duplicates

```python
return list(set(headlines))
```

* Some websites repeat headlines multiple times.
* `set()` removes duplicates.
* `list(set(...))` converts it back to a list before returning it.

---

### 🚀 8. The Main Program

```python
if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"
    headlines = get_news_headlines(news_url)
```

* This block runs only if you **execute** the file directly (not when imported).
* It passes the URL `"https://www.bbc.com/news"` to the function.

---

### 🖨️ 9. Printing the Headlines

```python
if headlines:
    print(f"\n🗞️ Headlines from {news_url}:\n")
    for i, headline in enumerate(headlines[:15], start=1):
        print(f"{i}. {headline}")
else:
    print("⚠️ No headlines found.")
```

* `if headlines:` checks if the list is not empty.
* `enumerate()` gives both index (`i`) and value (`headline`).
* `[:15]` limits output to the first 15 headlines.
* Nicely prints the results in a numbered list.

---

### 🔍 Example Output

```
🗞️ Headlines from https://www.bbc.com/news:

1. World leaders gather for global climate summit
2. India launches new moon mission
3. Tech giants face new privacy laws
```

---

## 💡 Notes

* Works best on **static** news sites (like BBC, Reuters, TechCrunch).
* **Dynamic sites** (like Zee News or Aaj Tak) load data using JavaScript, so BeautifulSoup won’t see the headlines.
* For those, you’d need **Selenium** (a tool that automates a browser).

---

## ✅ Requirements

Install dependencies before running:

```bash
pip install requests beautifulsoup4 lxml
```

---

## 🧑‍💻 Run the Script

```bash
python scrapping.py
```

---

## 🏁 Output

You’ll see something like:

```
🗞️ Headlines from https://www.bbc.com/news:

1. BBC reporter wins international award
2. Global markets show early signs of recovery
3. SpaceX launches new Starlink satellites
```

---

> 🎉 Congratulations — you just built your **first web scraping project** in Python using BeautifulSoup!
> Keep experimenting with other news sites and tags to learn more.

```

---


