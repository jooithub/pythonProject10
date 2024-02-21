import requests

# 수정된 코드
response = requests.post(
    'http://127.0.0.1:8000/aggregation/com2us/salesReset',
    headers={
        'accept': 'application/json',
        'X-Analyitcs-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjk0NTc2NSwianRpIjoiNGUyODE5ZmYtYWFhYy00MWUxLWEzNzktNzlmZGFkOGY5ZGViIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX2lkIjoiYWRtaW4iLCJnYW1lX2lkIjpudWxsLCJjcmVhdGVfZGF0ZXRpbWUiOiIyMDIxLTA3LTIyIDE4OjIyOjQ1IiwicmVmZXJyZXJfdXJsIjoiaHR0cHM6Ly90ZXN0LWFuYWx5dGljcy1hdXRoLmdhbWV2aWxjb20ydXMuY29tL2FkbWluLyJ9LCJuYmYiOjE2MjY5NDU3NjV9.DzX_PFKJ6UK2pS1PJf7mQPqQ9jsMui3yHtDhu47cpdg',
        'Content-Type': 'application/json'
    },
    json={
        "appid_group": "COC",
        "serverid":1,
        "serverid_ori":"QA",
        "release_date":"null"
#        "release_date":"2024-02-20 00:00:00"
    }
)

print(response.text)
print(response.text)
print(response.text)
print(response.text)