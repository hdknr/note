# Client Credentials


## curl 

curl -X POST -u "myClientID:password" -d "grant_type=client_credentials" http://host1.example.com:8080/openam/oauth2/access_token

~~~bash
curl -X POST -u "U6K8PeqBGcSyqOsSjPOF6Ift1tSg6zTJ2dmIWcXD:8p2K3hTRJnXQFsX92nQIqxiTCUEJO1VACL57FHdzI8EdezdSf1twuBHmSOiaRH1LNpSMGaJ2kbikAitQyH6x6wa2K5iVS4LUdyLLuDHxVUsOerOfgPXDAkDvl5650MmY" -d "grant_type=client_credentials" http://localhost:9000/api/rest/accounts/oauth2/token/
~~~

~~~json
{"access_token": "JaceJ25qhublck2E8K6xhNUmA3Wmfb", "expires_in": 36000, "token_type": "Bearer", "scope": "read write"}
~~~

## Django OAuth Tookkit

- [Client Credential](https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html?highlight=client_credentials#client-credential)
- 