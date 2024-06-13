import requests



def check_express_dev_mode(target):

    # Ensure the target URL starts with either http or https

    if not target.startswith("http://") and not target.startswith("https://"):

        target = "http://" + target  # Default to http if no scheme is provided



    headers = {

        "Host": target.split("//")[-1],  # Extract the host without scheme

        "Connection": "close",

        "s1d6p01nt7@bugcrowdninja.com": "true"  # Custom header for identifying traffic

    }



    # Step 1: Send a GET request to check for the 'X-Powered-By: Express' header

    try:

        response = requests.get(target, headers=headers)

        if 'X-Powered-By' in response.headers and 'express' in response.headers['X-Powered-By'].lower():

            print(f"[INFO] Express detected on {target}")



            # Step 2: Send a malformed GET request to trigger a development mode error

            headers["Content-Type"] = "application/json"

            malformed_response = requests.get(target, headers=headers, data="t")



            if malformed_response.status_code == 400 and 'syntaxerror: unexpected token' in malformed_response.text.lower():

                print(f"[VULNERABLE] {target} is running in development mode!")

                print(f"Response: {malformed_response.text}")

            else:

                print(f"[SECURE] {target} is not running in development mode.")

        else:

            print(f"[INFO] Express not detected on {target}")

    except requests.exceptions.RequestException as e:

        print(f"[ERROR] Failed to connect to {target}: {e}")



if __name__ == "__main__":

    target = input("Enter the target URL (with http/https): ")

    check_express_dev_mode(target)

