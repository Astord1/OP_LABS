from generator_lib.auth_proxy import AuthProxy, ApiKeyAuth
import json

def log(msg):
    print(msg)

def main():
    api_key = "secret123"
    proxy = AuthProxy(ApiKeyAuth(api_key), "https://httpbin.org", log)

    res = proxy.request("GET", "/get", params={"msg": "hello"})
    print(json.dumps(res.json(), indent=2))

if __name__ == "__main__":
    main()
