import requests


def check_website_status():
    """
    Makes a simple GET request to example.com to demonstrate
    the use of the requests library.
    """
    try:
        print("Checking status of http://example.com...")
        response = requests.get("http://example.com")
        print(f"Request successful with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    check_website_status()
