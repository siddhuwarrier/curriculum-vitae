#!/usr/bin/env python3

import json
import os
import sys
import urllib.error
import urllib.request


def main() -> int:
    token = os.environ["CLOUDFLARE_API_TOKEN"].strip()
    account_id = os.environ["CLOUDFLARE_ACCOUNT_ID"].strip()
    bucket_name = os.environ["R2_BUCKET_NAME"].strip()
    object_key = os.environ["R2_OBJECT_KEY"].strip()
    pdf_path = os.environ.get("CV_PDF_PATH", "cv.pdf").strip()

    for name, value in [
        ("CLOUDFLARE_API_TOKEN", token),
        ("CLOUDFLARE_ACCOUNT_ID", account_id),
        ("R2_BUCKET_NAME", bucket_name),
        ("R2_OBJECT_KEY", object_key),
    ]:
        if not value:
            print(f"Error: {name} is empty or not set.")
            return 1

    with open(pdf_path, "rb") as pdf_file:
        pdf_data = pdf_file.read()

    req = urllib.request.Request(
        (
            "https://api.cloudflare.com/client/v4/"
            f"accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_key}"
        ),
        data=pdf_data,
        method="PUT",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/pdf",
            "Cache-Control": "public, max-age=300",
        },
    )

    try:
        with urllib.request.urlopen(req) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        print("Failed to upload CV PDF to Cloudflare R2.")
        print(details)
        return 1

    if not body.get("success"):
        print("Cloudflare API returned an unsuccessful response.")
        print(json.dumps(body, indent=2))
        return 1

    print(f"Uploaded {pdf_path} to r2://{bucket_name}/{object_key}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
