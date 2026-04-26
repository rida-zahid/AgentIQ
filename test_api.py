import requests

BASE_URL = "http://127.0.0.1:8000"

def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    print(" Home endpoint working!")

def test_analyze():
    payload = {"query": "sports news"}
    response = requests.post(f"{BASE_URL}/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "extracted" in data
    print(" Analyze endpoint working!")
    print("Summary:", data["summary"][:100], "...")

def test_empty_query():
    payload = {"query": ""}
    response = requests.post(f"{BASE_URL}/analyze", json=payload)
    print(" Empty query test done! Status:", response.status_code)

if __name__ == "__main__":
    print("\n Running Tests...\n")
    test_home()
    test_analyze()
    test_empty_query()
    print("\n All Tests Passed!")