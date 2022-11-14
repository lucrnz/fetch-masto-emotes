# fetch-masto-emotes

A script to fetch emoticons from mastodon instances.

# Setup environment and install requirements

For Windows OS: [check this guide](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

# Usage

Specify the instance domain with an environment variable

    INSTANCE="instance.example" python main.py
    ls output

# Use with Docker

This method is more bulletproof since it keeps the same Python version I used for coding this script.

Leave venv if you are there, you do not need it for this.

Build the image

    docker build --build-arg UID=$(id -u) --build-arg GID=$(id -g) -t fetch-masto-emotes .

Fetch the emotes
Replace instance.example with the target instance domain name

    docker run -v $(pwd)/output:/app/output -e "INSTANCE=instance.example" -t fetch-masto-emotes
    ls output

You may clear the images and container

    docker image rm fetch-masto-emotes

    Error response from daemon: conflict: unable to remove repository reference "fetch-masto-emotes" (must force) - container be85a647881c is using its referenced image e24ff7ace9ac

The output will tell you that a container id (copy that id) is using that image, so we must remove it

    docker rm be85a647881c

Repeat the last command

    docker image rm fetch-masto-emotes

# Disclaimer

I made this program for myself, I don't have the intention (for now) to document it and/or give support, so pretty much you are on your own.

This piece of software is barely tested, don't use it on production, or use it at your own risk.
