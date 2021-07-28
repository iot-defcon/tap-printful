# tap-printful

`tap-printful` is a Singer tap for [Printful](https://www.printful.com).

Built with the Meltano [SDK](https://gitlab.com/meltano/sdk) for Singer Taps.

## Installation

```bash
pipx install tap-printful
```

## Configuration

### Accepted Config Options

- `api_key` - API key to access Printful API

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-printful --about
```

## Usage

You can easily run `tap-printful` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-printful --version
tap-printful --help
tap-printful --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_printful/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-printful` CLI interface directly using `poetry run`:

```bash
poetry run tap-printful --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano==1.77.0
# Initialize meltano within this directory
cd tap-printful
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-printful --version
# OR run a test `elt` pipeline:
meltano elt tap-printful target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
