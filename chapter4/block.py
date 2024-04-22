from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Check if the request is for TikTok
    if "tiktok.com" in flow.request.pretty_url:
        # Block the request by responding with an error
        flow.response = http.HTTPResponse.make(403, b"Forbidden")
